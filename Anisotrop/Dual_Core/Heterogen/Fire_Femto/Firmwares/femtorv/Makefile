BUILD_DIR?=../build_dir/femtorv_soc/

include $(BUILD_DIR)/software/include/generated/variables.mak
include $(SOC_DIRECTORY)/software/common.mak


OBJDIR = ./obj
EXT_LIBDIR = ../ext_lib
MBED_LIB = $(EXT_LIBDIR)/mbedtls/library

TINY_CRYPT_OBJ := $(OBJDIR)/aes_decrypt.o \
				$(OBJDIR)/aes_encrypt.o \
				$(OBJDIR)/ctr_mode.o \
				$(OBJDIR)/ctr_prng.o \
				$(OBJDIR)/ccm_mode.o \
				$(OBJDIR)/cmac_mode.o \
				$(OBJDIR)/utils.o

OBJECTS := $(TINY_CRYPT_OBJ) \
		  $(OBJDIR)/amp_aes.o \
		  $(OBJDIR)/main.o \
		  $(OBJDIR)/crt0.o

INCLUDES += -I$(EXT_LIBDIR)/tinycrypt \
			-I$(EXT_LIBDIR)/tinycrypt/lib/include \
			-I$(EXT_LIBDIR)/tinycrypt/lib/tinycrypt \
			-I$(EXT_LIBDIR)/mbedtls \
			-I$(EXT_LIBDIR)/mbedtls/include \

ifdef WITH_CXX
	OBJECTS += hellocpp.o
endif

all: demo.bin


%.bin: %.elf
	$(OBJCOPY) -O binary $< $@
ifneq ($(OS),Windows_NT)
	chmod -x $@
endif

vpath %.a $(PACKAGES:%=../%)

demo.elf: $(OBJECTS)
	$(CC) $(LDFLAGS) -T linker.ld -N -o $@ \
		$(OBJECTS) \
		$(PACKAGES:%=-L$(BUILD_DIR)/software/%) \
		-L$(EXT_LIBDIR)/tinycrypt/lib \
		-L$(MBED_LIB) \
		$(LIBS:lib%=-l%) \
		-ltinycrypt \
		-lmbedcrypto \
		-lgcc

ifneq ($(OS),Windows_NT)
	chmod -x $@
endif

# pull in dependency info for *existing* .o files
-include $(OBJECTS:.o=.d)

VPATH = $(BIOS_DIRECTORY):$(BIOS_DIRECTORY)/cmds:$(CPU_DIRECTORY)

$(OBJDIR)/main.o: main.c $(MBED_LIB)/libmbedcrypto.a $(EXT_LIBDIR)/tinycrypt/lib/libtinycrypt.a
	@mkdir -p $(@D)
	$(compile)

$(OBJDIR)/crt0.o: $(CPU_DIRECTORY)/crt0.S
	@mkdir -p $(@D)
	$(assemble)

$(OBJDIR)/%.o: %.cpp
	@mkdir -p $(@D)
	$(compilexx)

$(OBJDIR)/%.o: %.c
	@mkdir -p $(@D)
	$(compile)

$(OBJDIR)/%.o: $(EXT_LIBDIR)/tinycrypt/lib/source/%.c
	@mkdir -p $(@D)
	$(compile)

$(EXT_LIBDIR)/tinycrypt/lib/libtinycrypt.a: $(TINY_CRYPT_OBJ)
	$(AR) $(ARFLAGS) $@ $^

$(OBJDIR)/%.o: %.S
	@mkdir -p $(@D)
	$(assemble)

clean:
	$(RM) $(OBJECTS) demo.elf demo.bin .*~ *~

.PHONY: all clean