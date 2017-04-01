file_mappings = {
    'dio' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Dio.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Dio.arxml",
        "drivers/Dio/dio.mod.mk" : "drivers/dio.mod.mk",
        "generators/mcal/zynq/Dio.expt" : "generators/mcal/zynq/Dio.expt",
        "generators/mcal/zynq/Dio.echk" : "generators/mcal/zynq/Dio.echk",
        "generators/utils/DioHelpersZynq.eext":"generators/utils/DioHelpersZynq.eext",
        "stylesheets/dio.yaml" : "stylesheets/dio.yaml",
        "arch/arm/armv7_ar/drivers/Dio.c" : "arch/arm/armv7_ar/drivers/Dio.c",
        "drivers/Dio/Dio.h" : "include/Dio.h"
    },
    'mcu' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Mcu.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Mcu.arxml",
        "drivers/Mcu/mcu.mod.mk" : "drivers/Mcu/mcu.mod.mk",
        "generators/mcal/zynq/Mcu.echk" : "generators/mcal/zynq/Mcu.echk",
        "generators/mcal/zynq/Mcu.expt" : "generators/mcal/zynq/Mcu.expt",
        "generators/utils/McuHelpers.eext" : "generators/utils/McuHelpers.eext",
        "stylesheets/mcu.yaml" : "stylesheets/mcu.yaml",
        "arch/arm/armv7_ar/drivers/Mcu.c" : "arch/arm/armv7_ar/drivers/Mcu.c",
        "arch/arm/armv7_ar/drivers/zynq.h" : "arch/arm/armv7_ar/drivers/zynq.h",
        "drivers/Mcu/Mcu.h" : "include/arm/Mcu.h",
        "arch/arm/armv7_ar/integration/Mcu_Arc_Zynq.c" : "arch/arm/armv7_ar/integration/Mcu_Arc_Zynq.c",
        "include/io.h" : "include/io.h",
        "include/Mcu_Arc.h" : "include/Mcu_Arc.h",
        "include/arm/Cpu.h" : "include/arm/Cpu.h",
        "system/SchM/SchM_Mcu.h" : "system/SchM/SchM_Mcu.h",
        "include/irq.h" : "include/irq.h",
        "include/bit.h" : "include/bit.h",
    },
    'port' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Port.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Port.arxml",
        "drivers/port.mod.mk" : "drivers/port.mod.mk",
        "arxml/zynq/PortPins_zynq.yaml" : "arxml/zynq/PortPins_zynq.yaml",
        "generators/mcal/zynq/Port.expt" : "generators/mcal/zynq/Port.expt",
        "generators/mcal/zynq/Port.echk" : "generators/mcal/zynq/Port.echk",
        "generators/utils/PortHelpersZynq.eext":"generators/utils/PortHelpersZynq.eext",
        "stylesheets/port.yaml" : "stylesheets/port.yaml",
        "arch/arm/armv7_ar/drivers/Port.c" : "arch/arm/armv7_ar/drivers/Port.c",
        "include/Port.h" : "include/Port.h",
        "include/PortDefs.h" : "include/PortDefs.h",
        "arch/arm/armv7_ar/drivers/zynq_portdefs.h" : "arch/arm/armv7_ar/drivers/zynq_portdefs.h",
        "system/SchM/SchM_Port.h":"system/SchM/SchM_Port.h",
    },
    'can' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Can.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Can.arxml",
        "generators/mcal/zynq/Can.expt" : "generators/mcal/zynq/Can.expt",
        "generators/mcal/zynq/Can.echk" : "generators/mcal/zynq/Can.echk",
        "generators/utils/CanHelpersZynq.eext" : "generators/utils/CanHelpersZynq.eext",
        "stylesheets/can.yaml" : "stylesheets/can.yaml",
        "arch/arm/armv7_ar/drivers/Can_zynq.c" : "arch/arm/armv7_ar/drivers/Can_zynq.c",
        "drivers/Can/Can.c" : "drivers/Can/Can.c",
        "drivers/Can/Can_Internal.h" : "drivers/Can/Can_Internal.h",
        "drivers/Can/Can_GeneralTypes.h" : "include/Can_GeneralTypes.h",
        "drivers/Can/Can.h" : "include/Can.h",
        "drivers/Can/can.mod.mk" : "drivers/Can/can.mod.mk",
   },
    'kernel' : {
        "arch/arm/armv7_ar/kernel/arch_krn.sx" : "arch/arm/armv7_ar/kernel/arch_krn.sx",
        "arch/arm/armv7_ar/kernel/arch_offset.c" : "arch/arm/armv7_ar/kernel/arch_offset.c",
        "arch/arm/armv7_ar/kernel/arch_stack.h" : "arch/arm/armv7_ar/kernel/arch_stack.h",
        "arch/arm/armv7_ar/kernel/arch.c" : "arch/arm/armv7_ar/kernel/arch.c",
        "arch/arm/armv7_ar/kernel/core_cr4.h" : "arch/arm/armv7_ar/kernel/core_cr4.h",
        "arch/arm/armv7_ar/kernel/irq_zynq.h" : "arch/arm/armv7_ar/kernel/irq_zynq.h",
        "arch/arm/armv7_ar/kernel/irq_types.h" : "arch/arm/armv7_ar/kernel/irq_types.h",
        "arch/arm/armv7_ar/kernel/irq.c" : "arch/arm/armv7_ar/kernel/irq.c",
        "arch/arm/armv7_ar/kernel/stack.h" : "arch/arm/armv7_ar/kernel/stack.h",
        "arch/arm/armv7_ar/kernel/startup_armv7-ar.sx" : "arch/arm/armv7_ar/kernel/startup_armv7-ar.sx",
        "arch/arm/armv7_ar/kernel/sys_tick.c" : "arch/arm/armv7_ar/kernel/sys_tick.c",
    },
    'icu' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Icu.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Icu.arxml",
        "drivers/Fls/fls.mod.mk" : "drivers/fls.mod.mk",
        "generators/mcal/zynq/Icu.expt" : "generators/mcal/zynq/Icu.expt",
        "generators/mcal/zynq/Icu.echk" : "generators/mcal/zynq/Icu.echk",
        "generators/utils/IcuHelpersZynq.eext":"generators/utils/IcuHelpersZynq.eext",
        "stylesheets/icu.yaml" : "stylesheets/icu.yaml",
        "arch/arm/armv7_ar/drivers/Icu.c" : "arch/arm/armv7_ar/drivers/Icu.c",
        "include/Icu.h" : "include/Icu.h",
        "include/Icu_Internal.h" : "include/Icu_Internal.h",
   },
   'pwm' : {
        "drivers/Pwm/Pwm.mod.mk": "drivers/Pwm.mod.mk",
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Pwm.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Pwm.arxml",
        "generators/mcal/zynq/Pwm.expt" : "generators/mcal/zynq/Pwm.expt",
        "generators/mcal/zynq/Pwm.echk" : "generators/mcal/zynq/Pwm.echk",
        "generators/utils/PwmHelpers.eext":"generators/utils/PwmHelpers.eext",
        "stylesheets/pwm.yaml" : "stylesheets/pwm.yaml",
        "arch/arm/armv7_ar/drivers/Pwm.c" : "arch/arm/armv7_ar/drivers/Pwm.c",
        "drivers/Pwm/Pwm.h" : "include/Pwm.h",
        "system/SchM/SchM_Pwm.h":"system/SchM/SchM_Pwm.h",
    },
    'adc' : {
        "drivers/Adc/adc.mod.mk" : "drivers/Adc/adc.mod.mk",
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Adc.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Adc.arxml",
        "generators/mcal/zynq/Adc.expt" : "generators/mcal/zynq/Adc.expt",
        "generators/mcal/zynq/Adc.echk" : "generators/mcal/zynq/Adc.echk",
        "generators/utils/AdcHelpersZynq.eext":"generators/utils/AdcHelpersZynq.eext",
        "stylesheets/Adc.yaml" : "stylesheets/Adc.yaml",
        "arch/arm/armv7_ar/drivers/Adc.c" : "arch/arm/armv7_ar/drivers/Adc.c",
        "drivers/Adc/Adc.h" : "include/Adc.h",
        "include/arm/armv7_ar/Adc_ConfigTypes.h" : "include/arm/armv7_ar/Adc_ConfigTypes.h",
        "drivers/Adc/Adc_Internal.c" : "drivers/Adc/Adc_Internal.c",
        "drivers/Adc/Adc_Internal.h" : "drivers/Adc/Adc_Internal.h",
    },
    'spi' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Spi.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Spi.arxml",
        "generators/mcal/zynq/Spi.expt" : "generators/mcal/zynq/Spi.expt",
        "generators/mcal/zynq/Spi.echk" : "generators/mcal/zynq/Spi.echk",
        "stylesheets/spi.yaml" : "stylesheets/spi.yaml",
        "arch/arm/armv7_ar/drivers/Spi_zynq.c" : "arch/arm/armv7_ar/drivers/Spi_zynq.c",
        "drivers/Spi/Spi.c" : "drivers/Spi/Spi.c",
        "include/Spi.h" : "include/Spi.h",
        "drivers/Spi/Spi_Internal.h" : "drivers/Spi/Spi_Internal.h",
        "drivers/Spi/spi.mod.mk" : "drivers/Spi/spi.mod.mk",
    },
    'wdg' : {
        "drivers/Wdg/wdg.mod.mk" : "drivers/Wdg/wdg.mod.mk",
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Wdg.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Wdg.arxml",
        "generators/mcal/zynq/Wdg.expt" : "generators/mcal/zynq/Wdg.expt",
        "generators/mcal/zynq/Wdg.echk" : "generators/mcal/zynq/Wdg.echk",
        "stylesheets/wdg.yaml" : "stylesheets/wdg.yaml",
        "arch/arm/armv7_ar/drivers/Wdg.c" : "arch/arm/armv7_ar/drivers/Wdg.c",
        "drivers/Wdg/Wdg.h" : "include/Wdg.h",
    },
    'gpt' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Gpt.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Gpt.arxml",
        "drivers/Gpt/gpt.mod.mk" : "drivers/Gpt/gpt.mod.mk",
        "generators/mcal/zynq/Gpt.expt" : "generators/mcal/zynq/Gpt.expt",
        "generators/mcal/zynq/Gpt.echk" : "generators/mcal/zynq/Gpt.echk",
        "generators/utils/GptHelpersZynq.eext":"generators/utils/GptHelpersZynq.eext",
        "stylesheets/Gpt.yaml" : "stylesheets/Gpt.yaml",
        "arch/arm/armv7_ar/drivers/Gpt.c" : "arch/arm/armv7_ar/drivers/Gpt.c",
        "include/Gpt.h" : "include/Gpt.h",
        "include/Gpt_ConfigTypes.h" : "include/Gpt_ConfigTypes.h",
        "include/isr.h" : "include/isr.h",
    },
    'fls' : {
        "arch/arm/armv7_ar/drivers/Fls.c" : "arch/arm/armv7_ar/drivers/Fls.c",
        "drivers/Fls/fls.mod.mk" : "drivers/fls.mod.mk",
        "drivers/Fls/Fls.h" : "include/Fls.h",
        "include/MemIf_Types.h" : "include/MemIf_Types.h",
        "drivers/Fls/Fls_ConfigTypes.h" : "include/Fls_ConfigTypes.h",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/xqspi_types.h" : "arch/arm/armv7_ar/drivers/qspips_v3_1/xqspi_types.h",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/QspiIf/QspiIf.h" : "arch/arm/armv7_ar/drivers/qspips_v3_1/QspiIf/QspiIf.h",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/QspiIf/QspiIf.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/QspiIf/QspiIf.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips.h" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips.h",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_hw.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_hw.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_hw.h" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_hw.h",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_g.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_g.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_options.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_options.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_selftest.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_selftest.c",
        "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_sinit.c" : "arch/arm/armv7_ar/drivers/qspips_v3_1/src/xqspips_sinit.c",
    },
   'eth' : {
        "stylesheets/Eth.yaml" : "stylesheets/Eth.yaml",
        "arch/arm/armv7_ar/drivers/Eth_zc702.c" : "arch/arm/armv7_ar/drivers/Eth_zc702.c",
        "communication/Eth/Eth.c" : "communication/Eth/Eth.c",
        "communication/Eth/Eth.h" : "include/Eth.h",
        "include/EthIf_Cbk.h" : "include/EthIf_Cbk.h",
        "include/Eth_GeneralTypes.h" : "include/Eth_GeneralTypes.h",
        "communication/Eth/Eth_Internal.h" : "communication/Eth/Eth_Internal.h",
        "communication/Eth/eth.mod.mk" : "communication/Eth/eth.mod.mk",
   },
   'lin' : {
        "arxml/zynq/ArcCore_EcucDefs_Zynq_Lin.arxml" : "arxml/zynq/ArcCore_EcucDefs_Zynq_Lin.arxml",
        "drivers/lin.mod.mk" : "drivers/lin.mod.mk",
        "generators/mcal/zynq/Lin.expt" : "generators/mcal/zynq/Lin.expt",
        "generators/mcal/zynq/Lin.echk" : "generators/mcal/zynq/Lin.echk",
        "generators/utils/LinHelpers.eext" : "generators/utils/LinHelpers.eext",
        "stylesheets/Lin.yaml" : "stylesheets/Lin.yaml",
        "arch/arm/armv7_ar/drivers/Lin.c" : "arch/arm/armv7_ar/drivers/Lin.c",
        "include/Lin.h" : "include/Lin.h",
        "include/Lin_GeneralTypes.h" : "include/Lin_GeneralTypes.h",
        "include/Lin_ConfigTypes.h" : "include/Lin_ConfigTypes.h",
        "include/Lin_Types.h" : "include/Lin_Types.h",
   },
   'common' : {
        "arxml/McalDefinitions.yaml" : "arxml/McalDefinitions.yaml",
        "arxml/autosar/ECUConfigurationParameters_412.arxml" : "arxml/autosar/ECUConfigurationParameters_412.arxml",
        "arxml/zynq/McalImplementations_zynq.arxml" : "arxml/zynq/McalImplementations_zynq.arxml",
        "generators/utils/Helpers.eext" : "generators/utils/Helpers.eext",
        "include/Arc_Types.h" : "include/Arc_Types.h",
        "include/Std_Types.h" : "include/Std_Types.h",
        "base/compiler/Compiler.h" : "base/compiler/Compiler.h",
        "include/Platform_Types.h" : "include/Platform_Types.h",
    },
    'buildsystem' : {
        "makefile" : "makefile",
        "boards/board_common.mk" : "boards/board_common.mk",
        "arch/arm/armv7_ar/scripts/gcc.mk" : "arch/arm/armv7_ar/scripts/gcc.mk",
        "arch/arm/armv7_ar/scripts/linkscript_gcc.ldf" : "arch/arm/armv7_ar/scripts/linkscript_gcc.ldf",
        "scripts/project_defaults.mk" : "scripts/project_defaults.mk",
        "scripts/rules.mk" : "scripts/rules.mk",
        "scripts/version_check.mk" : "scripts/version_check.mk",
        "scripts/cc_gcc.mk" : "scripts/cc_gcc.mk",
        "boards/zynq_zc702/board_info.txt":"boards/zynq_zc702/board_info.txt",
        "boards/zynq_zc702/build_config.mk":"boards/zynq_zc702/build_config.mk",
        "boards/generic/Mcu_Arc_Cfg.h":"boards/zynq_zc702/config/Mcu_Arc_Cfg.h",
        "boards/generic/Mcu_Arc_Cfg.c":"boards/zynq_zc702/config/Mcu_Arc_Cfg.c",
        "boards/zynq_zc702/config/Fls_Cfg.c" : "boards/zynq_zc702/config/Fls_Cfg.c",
        "boards/zynq_zc702/config/Fls_Cfg.h" : "boards/zynq_zc702/config/Fls_Cfg.h",
        "boards/zynq_zc702/memory.ldf":"boards/zynq_zc702/memory.ldf",
        "boards/board_common.mk":"boards/board_common.mk",
    },
    'os' : {
        "system/Os/makefile" : "system/Os/makefile",
    },

    'Misc' : {
        "include/timer.h" : "include/timer.h",
        "include/sys/queue.h" : "include/sys/queue.h",
        "common/init.c" : "common/init.c",
        "clib/printf.c" : "clib/printf.c",
        "clib/assert.h" : "clib/assert.h",
        "include/ComStack_Types.h" : "include/ComStack_Types.h",
        "arch/arm/armv7_ar/drivers/timer_global.c": "arch/arm/armv7_ar/drivers/timer_global.c",
        #=======================================================================
        # "system/Os/asm_offset.c":"system/Os/asm_offset.c",
        # "system/Os/include/os_i.h":"system/Os/include/os_i.h",
        # "system/Os/include/os_internal.h":"system/Os/include/os_internal.h",
        # "system/Os/include/os_sys.h":"system/Os/include/os_sys.h",
        # "integration/MemMap.h" : "integration/MemMap.h",
        # "integration/Arc_MemMap.h" : "integration/Arc_MemMap.h",
        #=======================================================================
    },
    'project_files' : {
        ".project" : ".project",
        ".cproject" : ".cproject",
        ".settings/com.arccore.prefs" : ".settings/com.arccore.prefs",
        ".settings/org.eclipse.core.resources.prefs" : ".settings/org.eclipse.core.resources.prefs",
    }

}
patch_file_mappings = {
    'patch' : {
        "build_config.mk" : "boards/zynq_zc702/build_config.mk",
    },
}