# Generated by the tools/gen_goopcode.py. DO NOT EDIT.
# This conversion list acquired from https://github.com/zchee/Opcodes/raw/go-avx/opcodes/x86_64.xml

from typing import List, Dict


class go(object):
    symbols: List[Dict] = [
        {
            "word": "FP",
            "abbr": "FP",
            "kind": "Frame pointer: arguments and locals.",
            "info": "FP Frame pointer: arguments and locals.",
            "dup": 1,
        },
        {
            "word": "PC",
            "abbr": "PC",
            "kind": "Program counter: jumps and branches.",
            "info": "PC Program counter: jumps and branches.",
            "dup": 1,
        },
        {
            "word": "SB",
            "abbr": "SB",
            "kind": "Static base pointer: global symbols.",
            "info": "SB Static base pointer: global symbols.",
            "dup": 1,
        },
        {
            "word": "SP",
            "abbr": "SP",
            "kind": "Stack pointer: top of stack.",
            "info": "SP Stack pointer: top of stack.",
            "dup": 1,
        },
        {
            "word": "DATA",
            "abbr": "DATA",
            # TODO(zchee):
            # "kind": ,
            # "info": ,
            "dup": 1,
        },
        {
            "word": "GLOBL",
            "abbr": "GLOBL",
            # TODO(zchee):
            # "kind": ,
            # "info": ,
            "dup": 1,
        },
        {
            "word": "FUNCDATA",
            "abbr": "FUNCDATA",
            # TODO(zchee):
            # "kind": ,
            # "info": ,
            "dup": 1,
        },
        {
            "word": "PCDATA",
            "abbr": "PCDATA",
            # TODO(zchee):
            # "kind": ,
            # "info": ,
            "dup": 1,
        },
        {
            "word": "TEXT",
            "abbr": "TEXT",
            # TODO(zchee):
            # "kind": ,
            # "info": ,
            "dup": 1,
        },
    ]

    mnemonics = dict(
        {
            "adcb": "ADCB",
            "adcw": "ADCW",
            "adcl": "ADCL",
            "adcq": "ADCQ",
            "adcxl": "ADCXL",
            "adcxq": "ADCXQ",
            "addb": "ADDB",
            "addw": "ADDW",
            "addl": "ADDL",
            "addq": "ADDQ",
            "addpd": "ADDPD",
            "addps": "ADDPS",
            "addsd": "ADDSD",
            "addss": "ADDSS",
            "addsubpd": "ADDSUBPD",
            "addsubps": "ADDSUBPS",
            "adoxl": "ADOXL",
            "adoxq": "ADOXQ",
            "aesdec": "AESDEC",
            "aesdeclast": "AESDECLAST",
            "aesenc": "AESENC",
            "aesenclast": "AESENCLAST",
            "aesimc": "AESIMC",
            "aeskeygenassist": "AESKEYGENASSIST",
            "andb": "ANDB",
            "andw": "ANDW",
            "andl": "ANDL",
            "andq": "ANDQ",
            "andnl": "ANDNL",
            "andnq": "ANDNQ",
            "andnpd": "ANDNPD",
            "andnps": "ANDNPS",
            "andpd": "ANDPD",
            "andps": "ANDPS",
            "blendpd": "BLENDPD",
            "blendps": "BLENDPS",
            "blendvpd": "BLENDVPD",
            "blendvps": "BLENDVPS",
            "bsfw": "BSFW",
            "bsfl": "BSFL",
            "bsfq": "BSFQ",
            "bsrw": "BSRW",
            "bsrl": "BSRL",
            "bsrq": "BSRQ",
            "bswapl": "BSWAPL",
            "bswapq": "BSWAPQ",
            "btw": "BTW",
            "btl": "BTL",
            "btq": "BTQ",
            "btcw": "BTCW",
            "btcl": "BTCL",
            "btcq": "BTCQ",
            "btrw": "BTRW",
            "btrl": "BTRL",
            "btrq": "BTRQ",
            "btsw": "BTSW",
            "btsl": "BTSL",
            "btsq": "BTSQ",
            "call": "CALL",
            "cbtw": "CBW",
            "cltd": "CDQ",
            "cltq": "CDQE",
            "clc": "CLC",
            "cld": "CLD",
            "clflush": "CLFLUSH",
            "clflushopt": "CLFLUSHOPT",
            "cmc": "CMC",
            "cmovc": "CMOVC",
            "cmovna": "CMOVNA",
            "cmovnae": "CMOVNAE",
            "cmovnb": "CMOVNB",
            "cmovnbe": "CMOVNBE",
            "cmovnc": "CMOVNC",
            "cmovng": "CMOVNG",
            "cmovnge": "CMOVNGE",
            "cmovnl": "CMOVNL",
            "cmovnle": "CMOVNLE",
            "cmovnz": "CMOVNZ",
            "cmovpe": "CMOVPE",
            "cmovpo": "CMOVPO",
            "cmovz": "CMOVZ",
            "cmpb": "CMPB",
            "cmpw": "CMPW",
            "cmpl": "CMPL",
            "cmpq": "CMPQ",
            "cmppd": "CMPPD",
            "cmpps": "CMPPS",
            "cmpsd": "CMPSD",
            "cmpss": "CMPSS",
            "cmpxchgb": "CMPXCHGB",
            "cmpxchgw": "CMPXCHGW",
            "cmpxchgl": "CMPXCHGL",
            "cmpxchgq": "CMPXCHGQ",
            "cmpxchg16b": "CMPXCHG16B",
            "cmpxchg8b": "CMPXCHG8B",
            "comisd": "COMISD",
            "comiss": "COMISS",
            "cpuid": "CPUID",
            "cqto": "CQO",
            "crc32b": "CRC32B",
            "crc32w": "CRC32W",
            "crc32l": "CRC32L",
            "crc32q": "CRC32Q",
            "cvtdq2pd": "CVTPL2PD",
            "cvtdq2ps": "CVTPL2PS",
            "cvtpd2dq": "CVTPD2PL",
            "cvtpd2ps": "CVTPD2PS",
            "cvtps2dq": "CVTPS2PL",
            "cvtps2pd": "CVTPS2PD",
            "cvtsd2si": "CVTSD2SL",
            "cvtsd2si": "CVTSD2SQ",
            "cvtsd2ss": "CVTSD2SS",
            "cvtsi2sd": "CVTSL2SD",
            "cvtsi2sd": "CVTSQ2SD",
            "cvtsi2ss": "CVTSL2SS",
            "cvtsi2ss": "CVTSQ2SS",
            "cvtss2sd": "CVTSS2SD",
            "cvtss2si": "CVTSS2SL",
            "cvtss2si": "CVTSS2SQ",
            "cvttpd2dq": "CVTTPD2PL",
            "cvttps2dq": "CVTTPS2PL",
            "cvttsd2si": "CVTTSD2SL",
            "cvttsd2si": "CVTTSD2SQ",
            "cvttss2si": "CVTTSS2SL",
            "cvttss2si": "CVTTSS2SQ",
            "cwtd": "CWD",
            "cwtl": "CWDE",
            "decb": "DECB",
            "decw": "DECW",
            "decl": "DECL",
            "decq": "DECQ",
            "divb": "DIVB",
            "divw": "DIVW",
            "divl": "DIVL",
            "divq": "DIVQ",
            "divpd": "DIVPD",
            "divps": "DIVPS",
            "divsd": "DIVSD",
            "divss": "DIVSS",
            "dppd": "DPPD",
            "dpps": "DPPS",
            "emms": "EMMS",
            "extractps": "EXTRACTPS",
            "haddpd": "HADDPD",
            "haddps": "HADDPS",
            "hsubpd": "HSUBPD",
            "hsubps": "HSUBPS",
            "idivb": "IDIVB",
            "idivw": "IDIVW",
            "idivl": "IDIVL",
            "idivq": "IDIVQ",
            "imulb": "IMULB",
            "imulw": "IMULW",
            "imull": "IMULL",
            "imulq": "IMULQ",
            "imulq": "IMUL3Q",
            "incb": "INCB",
            "incw": "INCW",
            "incl": "INCL",
            "incq": "INCQ",
            "insertps": "INSERTPS",
            "int": "INT",
            "ja": "JHI",
            "jae": "JCC",
            "jb": "JCS",
            "jbe": "JLS",
            "je": "JEQ",
            "jecxz": "JCXZL",
            "jg": "JGT",
            "jge": "JGE",
            "jl": "JLT",
            "jle": "JLE",
            "jmp": "JMP",
            "jne": "JNE",
            "jno": "JOC",
            "jnp": "JPC",
            "jns": "JPL",
            "jo": "JOS",
            "jp": "JPS",
            "jrcxz": "JCXZQ",
            "js": "JMI",
            "lddqu": "LDDQU",
            "ldmxcsr": "LDMXCSR",
            "leaw": "LEAW",
            "leal": "LEAL",
            "leaq": "LEAQ",
            "lfence": "LFENCE",
            "lzcntw": "LZCNTW",
            "lzcntl": "LZCNTL",
            "lzcntq": "LZCNTQ",
            "maskmovdqu": "MASKMOVOU",
            "maskmovq": "MASKMOVQ",
            "maxpd": "MAXPD",
            "maxps": "MAXPS",
            "maxsd": "MAXSD",
            "maxss": "MAXSS",
            "mfence": "MFENCE",
            "minpd": "MINPD",
            "minps": "MINPS",
            "minsd": "MINSD",
            "minss": "MINSS",
            "monitor": "MONITOR",
            "movb": "MOVB",
            "movw": "MOVW",
            "movl": "MOVL",
            "movq": "MOVQ",
            "movapd": "MOVAPD",
            "movaps": "MOVAPS",
            "movd": "MOVD",
            "movddup": "MOVDDUP",
            "movdqa": "MOVO",
            "movdqu": "MOVOU",
            "movhlps": "MOVHLPS",
            "movhpd": "MOVHPD",
            "movhps": "MOVHPS",
            "movlhps": "MOVLHPS",
            "movlpd": "MOVLPD",
            "movlps": "MOVLPS",
            "movmskpd": "MOVMSKPD",
            "movmskps": "MOVMSKPS",
            "movntdq": "MOVNTO",
            "movntdqa": "MOVNTDQA",
            "movntil": "MOVNTIL",
            "movntiq": "MOVNTIQ",
            "movntpd": "MOVNTPD",
            "movntps": "MOVNTPS",
            "movntq": "MOVNTQ",
            "movntsd": "MOVNTSD",
            "movntss": "MOVNTSS",
            "movq2dq": "MOVQOZX",
            "movsd": "MOVSD",
            "movshdup": "MOVSHDUP",
            "movsldup": "MOVSLDUP",
            "movss": "MOVSS",
            "movsbw": "MOVBWSX",
            "movsbl": "MOVBLSX",
            "movswl": "MOVWLSX",
            "movsbq": "MOVBQSX",
            "movswq": "MOVWQSX",
            "movslq": "MOVLQSX",
            "movupd": "MOVUPD",
            "movups": "MOVUPS",
            "movzbw": "MOVBWZX",
            "movzbl": "MOVBLZX",
            "movzwl": "MOVWLZX",
            "movzbq": "MOVBQZX",
            "movzwq": "MOVWQZX",
            "mpsadbw": "MPSADBW",
            "mulb": "MULB",
            "mulw": "MULW",
            "mull": "MULL",
            "mulq": "MULQ",
            "mulpd": "MULPD",
            "mulps": "MULPS",
            "mulsd": "MULSD",
            "mulss": "MULSS",
            "mulxl": "MULXL",
            "mulxq": "MULXQ",
            "mwait": "MWAIT",
            "negb": "NEGB",
            "negw": "NEGW",
            "negl": "NEGL",
            "negq": "NEGQ",
            "nop": "NOP",
            "notb": "NOTB",
            "notw": "NOTW",
            "notl": "NOTL",
            "notq": "NOTQ",
            "orb": "ORB",
            "orw": "ORW",
            "orl": "ORL",
            "orq": "ORQ",
            "orpd": "ORPD",
            "orps": "ORPS",
            "pabsb": "PABSB",
            "pabsd": "PABSD",
            "pabsw": "PABSW",
            "packssdw": "PACKSSLW",
            "packsswb": "PACKSSWB",
            "packusdw": "PACKUSDW",
            "packuswb": "PACKUSWB",
            "paddb": "PADDB",
            "paddd": "PADDL",
            "paddq": "PADDQ",
            "paddsb": "PADDSB",
            "paddsw": "PADDSW",
            "paddusb": "PADDUSB",
            "paddusw": "PADDUSW",
            "paddw": "PADDW",
            "palignr": "PALIGNR",
            "pand": "PAND",
            "pandn": "PANDN",
            "pause": "PAUSE",
            "pavgb": "PAVGB",
            "pavgw": "PAVGW",
            "pblendvb": "PBLENDVB",
            "pblendw": "PBLENDW",
            "pclmulqdq": "PCLMULQDQ",
            "pcmpeqb": "PCMPEQB",
            "pcmpeqd": "PCMPEQL",
            "pcmpeqq": "PCMPEQQ",
            "pcmpeqw": "PCMPEQW",
            "pcmpestri": "PCMPESTRI",
            "pcmpestrm": "PCMPESTRM",
            "pcmpgtb": "PCMPGTB",
            "pcmpgtd": "PCMPGTL",
            "pcmpgtq": "PCMPGTQ",
            "pcmpgtw": "PCMPGTW",
            "pcmpistri": "PCMPISTRI",
            "pcmpistrm": "PCMPISTRM",
            "pextrb": "PEXTRB",
            "pextrd": "PEXTRD",
            "pextrq": "PEXTRQ",
            "pextrw": "PEXTRW",
            "pf2iw": "PF2IW",
            "pfacc": "PFACC",
            "pfadd": "PFADD",
            "pfcmpeq": "PFCMPEQ",
            "pfcmpge": "PFCMPGE",
            "pfcmpgt": "PFCMPGT",
            "pfmax": "PFMAX",
            "pfmin": "PFMIN",
            "pfmul": "PFMUL",
            "pfnacc": "PFNACC",
            "pfpnacc": "PFPNACC",
            "pfrcp": "PFRCP",
            "pfrcpit1": "PFRCPIT1",
            "pfrsqit1": "PFRSQIT1",
            "pfrsqrt": "PFRSQRT",
            "pfsub": "PFSUB",
            "pfsubr": "PFSUBR",
            "phaddd": "PHADDD",
            "phaddsw": "PHADDSW",
            "phaddw": "PHADDW",
            "phminposuw": "PHMINPOSUW",
            "phsubd": "PHSUBD",
            "phsubsw": "PHSUBSW",
            "phsubw": "PHSUBW",
            "pi2fw": "PI2FW",
            "pinsrb": "PINSRB",
            "pinsrd": "PINSRD",
            "pinsrq": "PINSRQ",
            "pinsrw": "PINSRW",
            "pmaddubsw": "PMADDUBSW",
            "pmaddwd": "PMADDWL",
            "pmaxsb": "PMAXSB",
            "pmaxsd": "PMAXSD",
            "pmaxsw": "PMAXSW",
            "pmaxub": "PMAXUB",
            "pmaxud": "PMAXUD",
            "pmaxuw": "PMAXUW",
            "pminsb": "PMINSB",
            "pminsd": "PMINSD",
            "pminsw": "PMINSW",
            "pminub": "PMINUB",
            "pminud": "PMINUD",
            "pminuw": "PMINUW",
            "pmovmskb": "PMOVMSKB",
            "pmovsxbd": "PMOVSXBD",
            "pmovsxbq": "PMOVSXBQ",
            "pmovsxbw": "PMOVSXBW",
            "pmovsxdq": "PMOVSXDQ",
            "pmovsxwd": "PMOVSXWD",
            "pmovsxwq": "PMOVSXWQ",
            "pmovzxbd": "PMOVZXBD",
            "pmovzxbq": "PMOVZXBQ",
            "pmovzxbw": "PMOVZXBW",
            "pmovzxdq": "PMOVZXDQ",
            "pmovzxwd": "PMOVZXWD",
            "pmovzxwq": "PMOVZXWQ",
            "pmuldq": "PMULDQ",
            "pmulhrsw": "PMULHRSW",
            "pmulhrw": "PMULHRW",
            "pmulhuw": "PMULHUW",
            "pmulhw": "PMULHW",
            "pmulld": "PMULLD",
            "pmullw": "PMULLW",
            "pmuludq": "PMULULQ",
            "popw": "POPW",
            "popq": "POPQ",
            "popcntw": "POPCNTW",
            "popcntl": "POPCNTL",
            "popcntq": "POPCNTQ",
            "por": "POR",
            "prefetchnta": "PREFETCHNTA",
            "prefetcht0": "PREFETCHT0",
            "prefetcht1": "PREFETCHT1",
            "prefetcht2": "PREFETCHT2",
            "prefetchw": "PREFETCHW",
            "prefetchwt1": "PREFETCHWT1",
            "psadbw": "PSADBW",
            "pshufb": "PSHUFB",
            "pshufd": "PSHUFL",
            "pshufhw": "PSHUFHW",
            "pshuflw": "PSHUFLW",
            "pshufw": "PSHUFW",
            "psignb": "PSIGNB",
            "psignd": "PSIGND",
            "psignw": "PSIGNW",
            "pslld": "PSLLL",
            "pslldq": "PSLLO",
            "psllq": "PSLLQ",
            "psllw": "PSLLW",
            "psrad": "PSRAL",
            "psraw": "PSRAW",
            "psrld": "PSRLL",
            "psrldq": "PSRLO",
            "psrlq": "PSRLQ",
            "psrlw": "PSRLW",
            "psubb": "PSUBB",
            "psubd": "PSUBL",
            "psubq": "PSUBQ",
            "psubsb": "PSUBSB",
            "psubsw": "PSUBSW",
            "psubusb": "PSUBUSB",
            "psubusw": "PSUBUSW",
            "psubw": "PSUBW",
            "ptest": "PTEST",
            "punpckhbw": "PUNPCKHBW",
            "punpckhdq": "PUNPCKHLQ",
            "punpckhqdq": "PUNPCKHQDQ",
            "punpckhwd": "PUNPCKHWL",
            "punpcklbw": "PUNPCKLBW",
            "punpckldq": "PUNPCKLLQ",
            "punpcklqdq": "PUNPCKLQDQ",
            "punpcklwd": "PUNPCKLWL",
            "pushq": "PUSHQ",
            "pushw": "PUSHW",
            "pxor": "PXOR",
            "rclb": "RCLB",
            "rclw": "RCLW",
            "rcll": "RCLL",
            "rclq": "RCLQ",
            "rcpps": "RCPPS",
            "rcpss": "RCPSS",
            "rcrb": "RCRB",
            "rcrw": "RCRW",
            "rcrl": "RCRL",
            "rcrq": "RCRQ",
            "rdrand": "RDRAND",
            "rdseed": "RDSEED",
            "rdtsc": "RDTSC",
            "rdtscp": "RDTSCP",
            "ret": "RET",
            "rolb": "ROLB",
            "rolw": "ROLW",
            "roll": "ROLL",
            "rolq": "ROLQ",
            "rorb": "RORB",
            "rorw": "RORW",
            "rorl": "RORL",
            "rorq": "RORQ",
            "rorxl": "RORXL",
            "rorxq": "RORXQ",
            "roundpd": "ROUNDPD",
            "roundps": "ROUNDPS",
            "roundsd": "ROUNDSD",
            "roundss": "ROUNDSS",
            "rsqrtps": "RSQRTPS",
            "rsqrtss": "RSQRTSS",
            "salb": "SALB",
            "salw": "SALW",
            "sall": "SALL",
            "salq": "SALQ",
            "sarb": "SARB",
            "sarw": "SARW",
            "sarl": "SARL",
            "sarq": "SARQ",
            "sarxl": "SARXL",
            "sarxq": "SARXQ",
            "sbbb": "SBBB",
            "sbbw": "SBBW",
            "sbbl": "SBBL",
            "sbbq": "SBBQ",
            "seta": "SETHI",
            "setae": "SETCC",
            "setb": "SETCS",
            "setbe": "SETLS",
            "sete": "SETEQ",
            "setg": "SETGT",
            "setge": "SETGE",
            "setl": "SETLT",
            "setle": "SETLE",
            "setne": "SETNE",
            "setno": "SETOC",
            "setnp": "SETPC",
            "setns": "SETPL",
            "seto": "SETOS",
            "setp": "SETPS",
            "sets": "SETMI",
            "sfence": "SFENCE",
            "shlb": "SHLB",
            "shlw": "SHLW",
            "shll": "SHLL",
            "shlq": "SHLQ",
            "shlxl": "SHLXL",
            "shlxq": "SHLXQ",
            "shrb": "SHRB",
            "shrw": "SHRW",
            "shrl": "SHRL",
            "shrq": "SHRQ",
            "shrxl": "SHRXL",
            "shrxq": "SHRXQ",
            "shufpd": "SHUFPD",
            "shufps": "SHUFPS",
            "sqrtpd": "SQRTPD",
            "sqrtps": "SQRTPS",
            "sqrtsd": "SQRTSD",
            "sqrtss": "SQRTSS",
            "stc": "STC",
            "std": "STD",
            "stmxcsr": "STMXCSR",
            "subb": "SUBB",
            "subw": "SUBW",
            "subl": "SUBL",
            "subq": "SUBQ",
            "subpd": "SUBPD",
            "subps": "SUBPS",
            "subsd": "SUBSD",
            "subss": "SUBSS",
            "syscall": "SYSCALL",
            "testb": "TESTB",
            "testw": "TESTW",
            "testl": "TESTL",
            "testq": "TESTQ",
            "tzcntw": "TZCNTW",
            "tzcntl": "TZCNTL",
            "tzcntq": "TZCNTQ",
            "ucomisd": "UCOMISD",
            "ucomiss": "UCOMISS",
            "ud2": "UD2",
            "unpckhpd": "UNPCKHPD",
            "unpckhps": "UNPCKHPS",
            "unpcklpd": "UNPCKLPD",
            "unpcklps": "UNPCKLPS",
            "vaddpd": "VADDPD",
            "vaddps": "VADDPS",
            "vaddsd": "VADDSD",
            "vaddss": "VADDSS",
            "vaddsubpd": "VADDSUBPD",
            "vaddsubps": "VADDSUBPS",
            "vaesdec": "VAESDEC",
            "vaesdeclast": "VAESDECLAST",
            "vaesenc": "VAESENC",
            "vaesenclast": "VAESENCLAST",
            "vaesimc": "VAESIMC",
            "vaeskeygenassist": "VAESKEYGENASSIST",
            "vandnpd": "VANDNPD",
            "vandnps": "VANDNPS",
            "vandpd": "VANDPD",
            "vandps": "VANDPS",
            "vblendpd": "VBLENDPD",
            "vblendps": "VBLENDPS",
            "vblendvpd": "VBLENDVPD",
            "vblendvps": "VBLENDVPS",
            "vbroadcastf128": "VBROADCASTF128",
            "vbroadcasti128": "VBROADCASTI128",
            "vbroadcastsd": "VBROADCASTSD",
            "vbroadcastss": "VBROADCASTSS",
            "vcmppd": "VCMPPD",
            "vcmpps": "VCMPPS",
            "vcmpsd": "VCMPSD",
            "vcmpss": "VCMPSS",
            "vcomisd": "VCOMISD",
            "vcomiss": "VCOMISS",
            "vcvtdq2pd": "VCVTDQ2PD",
            "vcvtdq2ps": "VCVTDQ2PS",
            "vcvtph2ps": "VCVTPH2PS",
            "vcvtps2dq": "VCVTPS2DQ",
            "vcvtps2pd": "VCVTPS2PD",
            "vcvtps2ph": "VCVTPS2PH",
            "vcvtsd2si": "VCVTSD2SI",
            "vcvtsd2ss": "VCVTSD2SS",
            "vcvtss2sd": "VCVTSS2SD",
            "vcvtss2si": "VCVTSS2SI",
            "vcvttps2dq": "VCVTTPS2DQ",
            "vcvttsd2si": "VCVTTSD2SI",
            "vcvttss2si": "VCVTTSS2SI",
            "vdivpd": "VDIVPD",
            "vdivps": "VDIVPS",
            "vdivsd": "VDIVSD",
            "vdivss": "VDIVSS",
            "vdppd": "VDPPD",
            "vdpps": "VDPPS",
            "vextractf128": "VEXTRACTF128",
            "vextracti128": "VEXTRACTI128",
            "vextractps": "VEXTRACTPS",
            "vfmadd132pd": "VFMADD132PD",
            "vfmadd132ps": "VFMADD132PS",
            "vfmadd132sd": "VFMADD132SD",
            "vfmadd132ss": "VFMADD132SS",
            "vfmadd213pd": "VFMADD213PD",
            "vfmadd213ps": "VFMADD213PS",
            "vfmadd213sd": "VFMADD213SD",
            "vfmadd213ss": "VFMADD213SS",
            "vfmadd231pd": "VFMADD231PD",
            "vfmadd231ps": "VFMADD231PS",
            "vfmadd231sd": "VFMADD231SD",
            "vfmadd231ss": "VFMADD231SS",
            "vfmaddsub132pd": "VFMADDSUB132PD",
            "vfmaddsub132ps": "VFMADDSUB132PS",
            "vfmaddsub213pd": "VFMADDSUB213PD",
            "vfmaddsub213ps": "VFMADDSUB213PS",
            "vfmaddsub231pd": "VFMADDSUB231PD",
            "vfmaddsub231ps": "VFMADDSUB231PS",
            "vfmsub132pd": "VFMSUB132PD",
            "vfmsub132ps": "VFMSUB132PS",
            "vfmsub132sd": "VFMSUB132SD",
            "vfmsub132ss": "VFMSUB132SS",
            "vfmsub213pd": "VFMSUB213PD",
            "vfmsub213ps": "VFMSUB213PS",
            "vfmsub213sd": "VFMSUB213SD",
            "vfmsub213ss": "VFMSUB213SS",
            "vfmsub231pd": "VFMSUB231PD",
            "vfmsub231ps": "VFMSUB231PS",
            "vfmsub231sd": "VFMSUB231SD",
            "vfmsub231ss": "VFMSUB231SS",
            "vfmsubadd132pd": "VFMSUBADD132PD",
            "vfmsubadd132ps": "VFMSUBADD132PS",
            "vfmsubadd213pd": "VFMSUBADD213PD",
            "vfmsubadd213ps": "VFMSUBADD213PS",
            "vfmsubadd231pd": "VFMSUBADD231PD",
            "vfmsubadd231ps": "VFMSUBADD231PS",
            "vfnmadd132pd": "VFNMADD132PD",
            "vfnmadd132ps": "VFNMADD132PS",
            "vfnmadd132sd": "VFNMADD132SD",
            "vfnmadd132ss": "VFNMADD132SS",
            "vfnmadd213pd": "VFNMADD213PD",
            "vfnmadd213ps": "VFNMADD213PS",
            "vfnmadd213sd": "VFNMADD213SD",
            "vfnmadd213ss": "VFNMADD213SS",
            "vfnmadd231pd": "VFNMADD231PD",
            "vfnmadd231ps": "VFNMADD231PS",
            "vfnmadd231sd": "VFNMADD231SD",
            "vfnmadd231ss": "VFNMADD231SS",
            "vfnmsub132pd": "VFNMSUB132PD",
            "vfnmsub132ps": "VFNMSUB132PS",
            "vfnmsub132sd": "VFNMSUB132SD",
            "vfnmsub132ss": "VFNMSUB132SS",
            "vfnmsub213pd": "VFNMSUB213PD",
            "vfnmsub213ps": "VFNMSUB213PS",
            "vfnmsub213sd": "VFNMSUB213SD",
            "vfnmsub213ss": "VFNMSUB213SS",
            "vfnmsub231pd": "VFNMSUB231PD",
            "vfnmsub231ps": "VFNMSUB231PS",
            "vfnmsub231sd": "VFNMSUB231SD",
            "vfnmsub231ss": "VFNMSUB231SS",
            "vhaddpd": "VHADDPD",
            "vhaddps": "VHADDPS",
            "vhsubpd": "VHSUBPD",
            "vhsubps": "VHSUBPS",
            "vinsertf128": "VINSERTF128",
            "vinserti128": "VINSERTI128",
            "vinsertps": "VINSERTPS",
            "vlddqu": "VLDDQU",
            "vldmxcsr": "VLDMXCSR",
            "vmaskmovdqu": "VMASKMOVDQU",
            "vmaskmovpd": "VMASKMOVPD",
            "vmaskmovps": "VMASKMOVPS",
            "vmaxpd": "VMAXPD",
            "vmaxps": "VMAXPS",
            "vmaxsd": "VMAXSD",
            "vmaxss": "VMAXSS",
            "vminpd": "VMINPD",
            "vminps": "VMINPS",
            "vminsd": "VMINSD",
            "vminss": "VMINSS",
            "vmovapd": "VMOVAPD",
            "vmovaps": "VMOVAPS",
            "vmovd": "VMOVD",
            "vmovddup": "VMOVDDUP",
            "vmovdqa": "VMOVDQA",
            "vmovdqu": "VMOVDQU",
            "vmovhlps": "VMOVHLPS",
            "vmovhpd": "VMOVHPD",
            "vmovhps": "VMOVHPS",
            "vmovlhps": "VMOVLHPS",
            "vmovlpd": "VMOVLPD",
            "vmovlps": "VMOVLPS",
            "vmovmskpd": "VMOVMSKPD",
            "vmovmskps": "VMOVMSKPS",
            "vmovntdq": "VMOVNTDQ",
            "vmovntdqa": "VMOVNTDQA",
            "vmovntpd": "VMOVNTPD",
            "vmovntps": "VMOVNTPS",
            "vmovq": "VMOVQ",
            "vmovsd": "VMOVSD",
            "vmovshdup": "VMOVSHDUP",
            "vmovsldup": "VMOVSLDUP",
            "vmovss": "VMOVSS",
            "vmovupd": "VMOVUPD",
            "vmovups": "VMOVUPS",
            "vmpsadbw": "VMPSADBW",
            "vmulpd": "VMULPD",
            "vmulps": "VMULPS",
            "vmulsd": "VMULSD",
            "vmulss": "VMULSS",
            "vorpd": "VORPD",
            "vorps": "VORPS",
            "vpabsb": "VPABSB",
            "vpabsd": "VPABSD",
            "vpabsw": "VPABSW",
            "vpackssdw": "VPACKSSDW",
            "vpacksswb": "VPACKSSWB",
            "vpackusdw": "VPACKUSDW",
            "vpackuswb": "VPACKUSWB",
            "vpaddb": "VPADDB",
            "vpaddd": "VPADDD",
            "vpaddq": "VPADDQ",
            "vpaddsb": "VPADDSB",
            "vpaddsw": "VPADDSW",
            "vpaddusb": "VPADDUSB",
            "vpaddusw": "VPADDUSW",
            "vpaddw": "VPADDW",
            "vpalignr": "VPALIGNR",
            "vpand": "VPAND",
            "vpandn": "VPANDN",
            "vpavgb": "VPAVGB",
            "vpavgw": "VPAVGW",
            "vpblendd": "VPBLENDD",
            "vpblendvb": "VPBLENDVB",
            "vpblendw": "VPBLENDW",
            "vpbroadcastb": "VPBROADCASTB",
            "vpbroadcastd": "VPBROADCASTD",
            "vpbroadcastq": "VPBROADCASTQ",
            "vpbroadcastw": "VPBROADCASTW",
            "vpclmulqdq": "VPCLMULQDQ",
            "vpcmpeqb": "VPCMPEQB",
            "vpcmpeqd": "VPCMPEQD",
            "vpcmpeqq": "VPCMPEQQ",
            "vpcmpeqw": "VPCMPEQW",
            "vpcmpestri": "VPCMPESTRI",
            "vpcmpestrm": "VPCMPESTRM",
            "vpcmpgtb": "VPCMPGTB",
            "vpcmpgtd": "VPCMPGTD",
            "vpcmpgtq": "VPCMPGTQ",
            "vpcmpgtw": "VPCMPGTW",
            "vpcmpistri": "VPCMPISTRI",
            "vpcmpistrm": "VPCMPISTRM",
            "vperm2f128": "VPERM2F128",
            "vperm2i128": "VPERM2I128",
            "vpermd": "VPERMD",
            "vpermilpd": "VPERMILPD",
            "vpermilps": "VPERMILPS",
            "vpermpd": "VPERMPD",
            "vpermps": "VPERMPS",
            "vpermq": "VPERMQ",
            "vpextrb": "VPEXTRB",
            "vpextrd": "VPEXTRD",
            "vpextrq": "VPEXTRQ",
            "vpextrw": "VPEXTRW",
            "vphaddd": "VPHADDD",
            "vphaddsw": "VPHADDSW",
            "vphaddw": "VPHADDW",
            "vphminposuw": "VPHMINPOSUW",
            "vphsubd": "VPHSUBD",
            "vphsubsw": "VPHSUBSW",
            "vphsubw": "VPHSUBW",
            "vpinsrb": "VPINSRB",
            "vpinsrd": "VPINSRD",
            "vpinsrq": "VPINSRQ",
            "vpinsrw": "VPINSRW",
            "vpmaddubsw": "VPMADDUBSW",
            "vpmaddwd": "VPMADDWD",
            "vpmaskmovd": "VPMASKMOVD",
            "vpmaskmovq": "VPMASKMOVQ",
            "vpmaxsb": "VPMAXSB",
            "vpmaxsd": "VPMAXSD",
            "vpmaxsw": "VPMAXSW",
            "vpmaxub": "VPMAXUB",
            "vpmaxud": "VPMAXUD",
            "vpmaxuw": "VPMAXUW",
            "vpminsb": "VPMINSB",
            "vpminsd": "VPMINSD",
            "vpminsw": "VPMINSW",
            "vpminub": "VPMINUB",
            "vpminud": "VPMINUD",
            "vpminuw": "VPMINUW",
            "vpmovmskb": "VPMOVMSKB",
            "vpmovsxbd": "VPMOVSXBD",
            "vpmovsxbq": "VPMOVSXBQ",
            "vpmovsxbw": "VPMOVSXBW",
            "vpmovsxdq": "VPMOVSXDQ",
            "vpmovsxwd": "VPMOVSXWD",
            "vpmovsxwq": "VPMOVSXWQ",
            "vpmovzxbd": "VPMOVZXBD",
            "vpmovzxbq": "VPMOVZXBQ",
            "vpmovzxbw": "VPMOVZXBW",
            "vpmovzxdq": "VPMOVZXDQ",
            "vpmovzxwd": "VPMOVZXWD",
            "vpmovzxwq": "VPMOVZXWQ",
            "vpmuldq": "VPMULDQ",
            "vpmulhrsw": "VPMULHRSW",
            "vpmulhuw": "VPMULHUW",
            "vpmulhw": "VPMULHW",
            "vpmulld": "VPMULLD",
            "vpmullw": "VPMULLW",
            "vpmuludq": "VPMULUDQ",
            "vpor": "VPOR",
            "vpsadbw": "VPSADBW",
            "vpshufb": "VPSHUFB",
            "vpshufd": "VPSHUFD",
            "vpshufhw": "VPSHUFHW",
            "vpshuflw": "VPSHUFLW",
            "vpsignb": "VPSIGNB",
            "vpsignd": "VPSIGND",
            "vpsignw": "VPSIGNW",
            "vpslld": "VPSLLD",
            "vpslldq": "VPSLLDQ",
            "vpsllq": "VPSLLQ",
            "vpsllvd": "VPSLLVD",
            "vpsllvq": "VPSLLVQ",
            "vpsllw": "VPSLLW",
            "vpsrad": "VPSRAD",
            "vpsravd": "VPSRAVD",
            "vpsraw": "VPSRAW",
            "vpsrld": "VPSRLD",
            "vpsrldq": "VPSRLDQ",
            "vpsrlq": "VPSRLQ",
            "vpsrlvd": "VPSRLVD",
            "vpsrlvq": "VPSRLVQ",
            "vpsrlw": "VPSRLW",
            "vpsubb": "VPSUBB",
            "vpsubd": "VPSUBD",
            "vpsubq": "VPSUBQ",
            "vpsubsb": "VPSUBSB",
            "vpsubsw": "VPSUBSW",
            "vpsubusb": "VPSUBUSB",
            "vpsubusw": "VPSUBUSW",
            "vpsubw": "VPSUBW",
            "vptest": "VPTEST",
            "vpunpckhbw": "VPUNPCKHBW",
            "vpunpckhdq": "VPUNPCKHDQ",
            "vpunpckhqdq": "VPUNPCKHQDQ",
            "vpunpckhwd": "VPUNPCKHWD",
            "vpunpcklbw": "VPUNPCKLBW",
            "vpunpckldq": "VPUNPCKLDQ",
            "vpunpcklqdq": "VPUNPCKLQDQ",
            "vpunpcklwd": "VPUNPCKLWD",
            "vpxor": "VPXOR",
            "vrcpps": "VRCPPS",
            "vrcpss": "VRCPSS",
            "vroundpd": "VROUNDPD",
            "vroundps": "VROUNDPS",
            "vroundsd": "VROUNDSD",
            "vroundss": "VROUNDSS",
            "vrsqrtps": "VRSQRTPS",
            "vrsqrtss": "VRSQRTSS",
            "vshufpd": "VSHUFPD",
            "vshufps": "VSHUFPS",
            "vsqrtpd": "VSQRTPD",
            "vsqrtps": "VSQRTPS",
            "vsqrtsd": "VSQRTSD",
            "vsqrtss": "VSQRTSS",
            "vstmxcsr": "VSTMXCSR",
            "vsubpd": "VSUBPD",
            "vsubps": "VSUBPS",
            "vsubsd": "VSUBSD",
            "vsubss": "VSUBSS",
            "vtestpd": "VTESTPD",
            "vtestps": "VTESTPS",
            "vucomisd": "VUCOMISD",
            "vucomiss": "VUCOMISS",
            "vunpckhpd": "VUNPCKHPD",
            "vunpckhps": "VUNPCKHPS",
            "vunpcklpd": "VUNPCKLPD",
            "vunpcklps": "VUNPCKLPS",
            "vxorpd": "VXORPD",
            "vxorps": "VXORPS",
            "vzeroall": "VZEROALL",
            "vzeroupper": "VZEROUPPER",
            "xaddb": "XADDB",
            "xaddw": "XADDW",
            "xaddl": "XADDL",
            "xaddq": "XADDQ",
            "xchgb": "XCHGB",
            "xchgw": "XCHGW",
            "xchgl": "XCHGL",
            "xchgq": "XCHGQ",
            "xgetbv": "XGETBV",
            "xorb": "XORB",
            "xorw": "XORW",
            "xorl": "XORL",
            "xorq": "XORQ",
            "xorpd": "XORPD",
            "xorps": "XORPS",
        }
    )