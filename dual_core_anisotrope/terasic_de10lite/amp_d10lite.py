#!/usr/bin/env python3

# Copyright (c) 2022 Florent Kermarrec <florent@enjoy-digital.fr>
# SPDX-License-Identifier: BSD-2-Clause
# Modifications by Joseph Wagane FAYE <joseph-wagane.faye@insa-rennes.fr>
import litex.soc.doc as lxsocdoc

from migen import *
from litex.soc.cores.uart import *
from litex.soc.cores.clock import *
from litex.soc.cores.led import LedChaser
from litex.soc.interconnect import csr_bus
from litex.soc.integration.builder import *
from litex.soc.interconnect import wishbone
from litex.soc.integration.soc_core import *
from litex.soc.integration.doc import AutoDoc
from litex_boards.platforms import terasic_de10lite
from litex.soc.integration.soc import SoCBusHandler, SoCRegion, SoCCSRRegion, SoCError

from litex.build.altera.programmer import USBBlaster


# CRG ----------------------------------------------------------------------------------------------

class _CRG(Module, AutoDoc):
    def __init__(self, platform, sys_clk_freq, with_rst=True):
        self.rst = Signal()
        self.clock_domains.cd_sys = ClockDomain()
        # # #
        # Clk/Rst.
        clk50 = platform.request("clk50")
        # PLL.
        self.submodules.pll = pll = Max10PLL(speedgrade='-7')
        self.comb += pll.reset.eq(self.rst)
        pll.register_clkin(clk50, 50e6)
        pll.create_clkout(self.cd_sys, sys_clk_freq)
        platform.add_false_path_constraints(self.cd_sys.clk, pll.clkin) # Ignore sys_clk to pll.clkin path created by SoC's rst.

# BaseSoC ------------------------------------------------------------------------------------------

class BaseSoC(SoCMini, AutoDoc):
    mem_map = {**SoCCore.mem_map, **{
        "csr": 0x10000000,
    }}
    def __init__(self, platform, platform_name, toolchain="vivado",
                 sys_clk_freq=int(50e6), with_led_chaser=True):

        # CRG --------------------------------------------------------------------------------------
        self.submodules.crg = _CRG(platform, sys_clk_freq)

        # SoCMini ----------------------------------------------------------------------------------
        SoCMini.__init__(self, platform, sys_clk_freq,
                         ident="LiteX standalone SoC generator on {}".format(platform_name))

        # JTAGBone ---------------------------------------------------------------------------------
        self.add_jtagbone()

        # Leds -------------------------------------------------------------------------------------
        if with_led_chaser:
            self.submodules.leds = LedChaser(
                pads         = platform.request_all("user_led"),
                sys_clk_freq = sys_clk_freq)

        self.buses = [self.bus]
        # Standalone SoC Generation/Re-Integration -------------------------------------------------
        contents = [i for i in range(16)]
        # Shared UART.
        uart_pads_1 = platform.request("serial", 0)
        uart_pads_2 = platform.request("serial", 1)
        #uart_sel  = platform.request("user_sw", 0)
        #print("uart_pads : {} ".format(type(uart_pads)))
        #uart_mux_pads = [UARTPads() for _ in range(2)]
        #uart_mux      = UARTMultiplexer(uart_mux_pads, uart_pads)
        #self.comb += uart_mux.sel.eq(uart_sel)
        #self.submodules += uart_mux

        # Shared RAM.
        self.add_ram("shared_ram", 0x0000_0000, 0x00001000, contents=contents)

        # Buses
        self.submodules.bus1 = SoCBusHandler()
        self.buses.append(self.bus1)
        self.submodules.bus2 = SoCBusHandler()
        self.buses.append(self.bus2)

        # Scratchpads Memories Interfaces
        interface_1 = wishbone.Interface(data_width=self.bus1.data_width, bursting=self.bus1.bursting)
        interface_2 = wishbone.Interface(data_width=self.bus2.data_width, bursting=self.bus2.bursting)
        # Scratchpad Memories
        self.submodules.scratch1 = wishbone.SRAM(0x1000, bus=interface_1, init=contents, read_only=False, name='scratchpad1')
        self.submodules.scratch2 = wishbone.SRAM(0x1000, bus=interface_2, init=contents, read_only=False, name='scratchpad2')
        # Integration
        #self.bus1.add_slave('scratchpad1', scratch1.bus, SoCRegion(origin=0x0000_a000, size=0x1000, mode="rw"))
        #self.bus2.add_slave('scratchpad2', scratch2.bus, SoCRegion(origin=0x0000_b000, size=0x1000, mode="rw"))
        # Conveniences | Scratchpad1
        #self.check_if_exists('scratchpad1')
        #self.logger.info("RAM {} {} {}.".format(
        #    colorer('scratchpad1'),
        #    colorer("added", color="green"),
        #    self.bus1.regions['scratchpad1']))
        #setattr(self.submodules, 'scratchpad1', scratch1)
        #if contents:
        #    self.add_config(f"{'scratchpad1'}_INIT", 1)
        # Conveniences | Scratchpad2
        #self.check_if_exists('scratchpad2')
        #self.logger.info("RAM {} {} {}.".format(
        #    colorer('scratchpad2'),
        #    colorer("added", color="green"),
        #    self.bus2.regions['scratchpad2']))
        #setattr(self.submodules, 'scratchpad2', scratch2)
        #if contents:
        #    self.add_config(f"{'scratchpad2'}_INIT", 1)
        # Interfaces to cores

        mmap_sp1 = wishbone.Interface()
        mmap_sp2 = wishbone.Interface()

        r = []

        for name, width, direction in mmap_sp1.layout:
            sig1 = getattr(self.scratch1.bus, name)
            pad1 = getattr(mmap_sp1, name)
            if direction == DIR_S_TO_M:
                r.append(pad1.eq(sig1))
            else:
                r.append(sig1.eq(pad1))

        for name, width, direction in mmap_sp2.layout:
            sig1 = getattr(self.scratch2.bus, name)
            pad1 = getattr(mmap_sp2, name)
            if direction == DIR_S_TO_M:
                r.append(pad1.eq(sig1))
            else:
                r.append(sig1.eq(pad1))

        self.comb += r

        # FemtoRV SoC.
        # ------------
        # Generate standalone SoC.
        #os.system("litex_soc_gen --cpu-type=femtorv --bus-standard=wishbone "
        #          "--sys-clk-freq=50e6 --name=femtorv_soc --integrated-rom-size=0x1000 "
        #          "--integrated-sram-size=0x1000 --integrated-main-ram-size=0x1000 --build")
        os.system("litex_soc_gen --cpu-type=femtorv --bus-standard=wishbone "
                  "--sys-clk-freq=50e6 --n-master-inter=2 --name=femtorv_soc --integrated-main-ram-size=0x4000 "
                  "--build")
        # Add standalone SoC sources.
        platform.add_source("build/femtorv_soc/gateware/femtorv_soc.v")
        platform.add_source("build/femtorv_soc/gateware/femtorv_soc_rom.init", copy=True)

        # Add CPU sources.
        from litex.soc.cores.cpu.femtorv import FemtoRV
        FemtoRV.add_sources(platform, "standard")

        # Do standalone SoC instance.
        mmap_wb = wishbone.Interface()
        self.specials += Instance("femtorv_soc",
            # Clk/Rst.
            i_clk     = ClockSignal("sys"),
            i_rst     = ResetSignal("sys"),

            # UART.
            #o_uart_tx = uart_mux_pads[0].tx,
            #i_uart_rx = uart_mux_pads[0].rx,
            o_uart_tx = uart_pads_1.tx,
            i_uart_rx = uart_pads_1.rx,

            # MMAP.
            o_mmap_m_0_adr   = mmap_wb.adr[:24], # CHECKME/FIXME: Base address
            o_mmap_m_0_dat_w = mmap_wb.dat_w,
            i_mmap_m_0_dat_r = mmap_wb.dat_r,
            o_mmap_m_0_sel   = mmap_wb.sel,
            o_mmap_m_0_cyc   = mmap_wb.cyc,
            o_mmap_m_0_stb   = mmap_wb.stb,
            i_mmap_m_0_ack   = mmap_wb.ack,
            o_mmap_m_0_we    = mmap_wb.we,
            o_mmap_m_0_cti   = mmap_wb.cti,
            o_mmap_m_0_bte   = mmap_wb.bte,
            i_mmap_m_0_err   = mmap_wb.err,

            #MMAP | Scratchpad
            o_mmap_m_1_adr=mmap_sp1.adr[:24],  # CHECKME/FIXME: Base address
            o_mmap_m_1_dat_w=mmap_sp1.dat_w,
            i_mmap_m_1_dat_r=mmap_sp1.dat_r,
            o_mmap_m_1_sel=mmap_sp1.sel,
            o_mmap_m_1_cyc=mmap_sp1.cyc,
            o_mmap_m_1_stb=mmap_sp1.stb,
            i_mmap_m_1_ack=mmap_sp1.ack,
            o_mmap_m_1_we=mmap_sp1.we,
            o_mmap_m_1_cti=mmap_sp1.cti,
            o_mmap_m_1_bte=mmap_sp1.bte,
            i_mmap_m_1_err=mmap_sp1.err,
        )
        self.bus.add_master(master=mmap_wb)
        #self.bus1.add_master(master=mmap_sp1)

        # Litescope.
        from litescope import LiteScopeAnalyzer
        self.submodules.analyzer = LiteScopeAnalyzer([mmap_wb],
            depth        = 512,
            clock_domain = "sys",
            samplerate   = sys_clk_freq,
            csr_csv      = "analyzer.csv"
        )

        self.submodules.bus2 = SoCBusHandler()
        # FireV SoC.
        # ----------

        # Generate standalone SoC.
        os.system("litex_soc_gen --cpu-type=firev --bus-standard=wishbone "
                  "--sys-clk-freq=50e6 --n-master-inter=2 --name=firev_soc --integrated-main-ram-size=0x4000 "
                  "--build")
        # Add standalone SoC sources.
        platform.add_source("build/firev_soc/gateware/firev_soc.v")
        platform.add_source("build/firev_soc/gateware/firev_soc_rom.init", copy=True)

        # Add CPU sources.
        from litex.soc.cores.cpu.firev import FireV
        FireV.add_sources(platform, "standard")

        # Do standalone SoC instance.
        mmap_wb = wishbone.Interface()
        self.specials += Instance("firev_soc",
            # Clk/Rst.
            i_clk     = ClockSignal("sys"),
            i_rst     = ResetSignal("sys"),

            # UART.
            #o_uart_tx = uart_mux_pads[1].tx,
            #i_uart_rx = uart_mux_pads[1].rx,
            o_uart_tx = uart_pads_2.tx,
            i_uart_rx = uart_pads_2.rx,


            # MMAP.
            o_mmap_m_0_adr   = mmap_wb.adr[:24], # CHECKME/FIXME: Base address.
            o_mmap_m_0_dat_w = mmap_wb.dat_w,
            i_mmap_m_0_dat_r = mmap_wb.dat_r,
            o_mmap_m_0_sel   = mmap_wb.sel,
            o_mmap_m_0_cyc   = mmap_wb.cyc,
            o_mmap_m_0_stb   = mmap_wb.stb,
            i_mmap_m_0_ack   = mmap_wb.ack,
            o_mmap_m_0_we    = mmap_wb.we,
            o_mmap_m_0_cti   = mmap_wb.cti,
            o_mmap_m_0_bte   = mmap_wb.bte,
            i_mmap_m_0_err   = mmap_wb.err,

            #MMAP | Scratchpad

            o_mmap_m_1_adr=mmap_sp2.adr[:24],  # CHECKME/FIXME: Base address
            o_mmap_m_1_dat_w=mmap_sp2.dat_w,
            i_mmap_m_1_dat_r=mmap_sp2.dat_r,
            o_mmap_m_1_sel=mmap_sp2.sel,
            o_mmap_m_1_cyc=mmap_sp2.cyc,
            o_mmap_m_1_stb=mmap_sp2.stb,
            i_mmap_m_1_ack=mmap_sp2.ack,
            o_mmap_m_1_we=mmap_sp2.we,
            o_mmap_m_1_cti=mmap_sp2.cti,
            o_mmap_m_1_bte=mmap_sp2.bte,
            i_mmap_m_1_err=mmap_sp2.err,
        )
        self.bus.add_master(master=mmap_wb)
        #self.bus2.add_master(master=mmap_sp2)

        #  Manual finalisation for buses interconnect.
        # Add csr brdige
        #csr_bridge_cls = wishbone.Wishbone2CSR
        #csr_bridge = csr_bridge_cls(
        #    bus_csr=csr_bus.Interface(
        #        address_width=self.csr.address_width,
        #        data_width=self.csr.data_width),
        #    register=False)
        # csr_size = 2 ** (self.csr.address_width + 2)
        # csr_region = SoCRegion(origin=self.mem_map["csr"], size=csr_size, cached=True, decode=self.cpu.csr_decode)
        # bus_cls = getattr(csr_bridge, "wishbone")
        # self.bus1.add_slave(name="csr_bridge", slave=bus_cls, region=csr_region)
        # self.bus2.add_slave(name="csr_bridge", slave=bus_cls, region=csr_region)

        # Interconnect
        #interconnect_p2p_cls = wishbone.InterconnectPointToPoint
        #interconnect_shared_cls = wishbone.InterconnectShared
        #interconnect_crossbar_cls = wishbone.Crossbar

        # Bus1
        #if len(self.bus1.masters) and len(self.bus1.slaves):
            # If 1 bus_master, 1 bus_slave and no address translation, use InterconnectPointToPoint.
        #    if ((len(self.bus1.masters) == 1)  and
        #        (len(self.bus1.slaves)  == 1)  and
        #        (next(iter(self.bus1.regions.values())).origin == 0)):
        #        self.submodules.bus_interconnect1 = interconnect_p2p_cls(
        #            master = next(iter(self.bus1.masters.values())),
        #            slave  = next(iter(self.bus1.slaves.values())))
            # Otherwise, use InterconnectShared/Crossbar.
        #    else:
        #        interconnect_cls = {
        #            "shared": interconnect_shared_cls,
        #            "crossbar": interconnect_crossbar_cls,
        #        }[self.bus1.interconnect]
        #        self.submodules.bus_interconnect1 = interconnect_cls(
        #            masters=list(self.bus1.masters.values()),
        #           slaves=[(self.bus1.regions[n].decoder(self.bus1), s) for n, s in self.bus1.slaves.items()],
        #            register=True,
        #            timeout_cycles=self.bus1.timeout)
        #        if hasattr(self, "ctrl") and self.bus1.timeout is not None:
        #            if hasattr(self.ctrl, "bus_error") and hasattr(self.bus_interconnect1, "timeout"):
        #                self.comb += self.ctrl.bus_error.eq(self.bus_interconnect1.timeout.error)
        #    self.bus1.logger.info("Interconnect: {} ({} <-> {}).".format(
        #        colorer(self.bus_interconnect1.__class__.__name__),
        #        colorer(len(self.bus1.masters)),
        #        colorer(len(self.bus1.slaves))))

        # Bus 2
        # if len(self.bus1.masters) and len(self.bus1.slaves):
        #    # If 1 bus_master, 1 bus_slave and no address translation, use InterconnectPointToPoint.
        #    if ((len(self.bus2.masters) == 1) and
        #        (len(self.bus2.slaves) == 1) and
        #        (next(iter(self.bus2.regions.values())).origin == 0)):
        #        self.submodules.bus_interconnect2 = interconnect_p2p_cls(
        #            master=next(iter(self.bus2.masters.values())),
        #            slave=next(iter(self.bus2.slaves.values())))
        #    # Otherwise, use InterconnectShared/Crossbar.
        #    else:
        #        interconnect_cls = {
        #                "shared": interconnect_shared_cls,
        #                "crossbar": interconnect_crossbar_cls,
        #            }[self.bus2.interconnect]
        #        self.submodules.bus_interconnect2 = interconnect_cls(
        #            masters=list(self.bus2.masters.values()),
        #            slaves=[(self.bus2.regions[n].decoder(self.bus2), s) for n, s in self.bus2.slaves.items()],
        #            register=True,
        #            timeout_cycles=self.bus2.timeout)
        #        if hasattr(self, "ctrl") and self.bus2.timeout is not None:
        #            if hasattr(self.ctrl, "bus_error") and hasattr(self.bus_interconnect2, "timeout"):
        #                self.comb += self.ctrl.bus_error.eq(self.bus_interconnect2.timeout.error)
        #    self.bus2.logger.info("Interconnect: {} ({} <-> {}).".format(
        #        colorer(self.bus_interconnect2.__class__.__name__),
        #        colorer(len(self.bus2.masters)),
        #        colorer(len(self.bus2.slaves))))


# Build --------------------------------------------------------------------------------------------

def main():
    from litex.soc.integration.soc import LiteXSoCArgumentParser
    parser = LiteXSoCArgumentParser(description="LiteX standalone SoC generator on De10Lite")
    target_group = parser.add_argument_group(title="Target options")
    target_group.add_argument("--platform", default=terasic_de10lite.Platform())
    target_group.add_argument("--toolchain",    default="quartus",    help="FPGA toolchain (vivado, symbiflow or yosys+nextpnr).")
    target_group.add_argument("--build",        action="store_true", help="Build bitstream.")
    target_group.add_argument("--load",         action="store_true", help="Load bitstream.")
    #target_group.add_argument("--flash",        action="store_true", help="Flash bitstream.")
    #target_group.add_argument("--variant",      default="a7-35",     help="Board variant (a7-35 or a7-100).")
    target_group.add_argument("--sys-clk-freq", default=50e6,       help="System clock frequency.")
    builder_args(parser)
    #vivado_build_args(parser)
    args = parser.parse_args()

    soc = BaseSoC(
        platform_name='De10Lite',
        platform=args.platform,
        toolchain      = args.toolchain,
        sys_clk_freq   = int(float(args.sys_clk_freq)),
    )

    builder = Builder(soc, **builder_argdict(args))
    builder_kwargs = {}
    builder.build(**builder_kwargs, run=args.build)

    if args.load:
        prog = soc.platform.create_programmer()
        prog.load_bitstream(builder.get_bitstream_filename(mode="sram"))

    lxsocdoc.generate_docs(soc, "build/documentation/", project_name="Assymetric Multi-Processing SoC",
                           author="Joseph W. FAYE")


if __name__ == "__main__":
    main()