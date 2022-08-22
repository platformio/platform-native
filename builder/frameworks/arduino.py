# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://arduino.cc/en/Reference/HomePage
"""

import os

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()
core = board.get("build.core")

FRAMEWORK_DIR = platform.get_package_dir("framework-portduino")
assert os.path.isdir(FRAMEWORK_DIR)

env.Append(
    CPPDEFINES=[
        ("ARDUINO", 4403), # FIXME, find how these numbers are assigned!
        "PORTDUINO" # FIXME, should we use some different convention?
        # ("CONFIG_MANUFACTURER", '\\"ASR\\"'),
        # ("CONFIG_DEVICE_MODEL", '\\"6501\\"'),
        # ("CONFIG_VERSION", '\\"v4.0\\"'),
    ],

    CCFLAGS=[
        "-w",
        "-Wall",
        "-ggdb"
    ],

    CXXFLAGS=[
        # "-fno-exceptions",
    ],

    LINKFLAGS=[
        "-ggdb"
    ],

    CPPPATH=[
        os.path.join(FRAMEWORK_DIR, "cores", "portduino"),
        os.path.join(FRAMEWORK_DIR, "cores", "portduino", "FS"),
        os.path.join(FRAMEWORK_DIR, "cores", "arduino", "api")
        # os.path.join(FRAMEWORK_DIR, "cores", core),
        # os.path.join(FRAMEWORK_DIR, "cores", core, "cores"),
        # os.path.join(FRAMEWORK_DIR, "cores", core, "Serial"),
        # os.path.join(FRAMEWORK_DIR, "cores", core, "Wire"),
        # os.path.join(FRAMEWORK_DIR, "cores", core, "SPI"),
    ],

    LIBS=[
        "stdc++",
        "m"
    ],

    LIBSOURCE_DIRS=[
        os.path.join(FRAMEWORK_DIR, "libraries")
    ]
)

#
# Target: Build Core Library
#

libs = []

if "build.variant" in env.BoardConfig():
    variants_dir = os.path.join(
        "$PROJECT_DIR", board.get("build.variants_dir")) if board.get(
            "build.variants_dir", "") else os.path.join(FRAMEWORK_DIR, "variants")
    env.Append(
        CPPPATH=[
            os.path.join(variants_dir, board.get("build.variant"))
        ]
    )
    libs.append(env.BuildLibrary(
        os.path.join("$BUILD_DIR", "FrameworkArduinoVariant"),
        os.path.join(variants_dir, board.get("build.variant"))
    ))

libs.append(env.BuildLibrary(
    os.path.join("$BUILD_DIR", "FrameworkArduino"),
    os.path.join(FRAMEWORK_DIR, "cores"),
    src_filter=[
        "+<*>",
        "-<%s/projects/PSoC4/CyBootAsmIar.s>" % core,
        "-<%s/projects/PSoC4/CyBootAsmRv.s>" % core
    ]
))

env.Prepend(LIBS=libs)
