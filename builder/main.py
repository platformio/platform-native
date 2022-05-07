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
    Builder for native platform
"""

from SCons.Script import COMMAND_LINE_TARGETS, AlwaysBuild, Default, DefaultEnvironment

env = DefaultEnvironment()

# Remove generic C/C++ tools
for k in ("CC", "CXX"):
    if k in env:
        del env[k]

# Preserve C and C++ build flags
backup_cflags = env.get("CFLAGS", [])
backup_cxxflags = env.get("CXXFLAGS", [])

# Scan for GCC compiler
env.Tool("gcc")
env.Tool("g++")

# Reload "compilation_db" tool
if "compiledb" in COMMAND_LINE_TARGETS:
    env.Tool("compilation_db")

# Restore C/C++ build flags as they were overridden by env.Tool
env.Append(CFLAGS=backup_cflags, CXXFLAGS=backup_cxxflags)

#
# Target: Build executable program
#

target_bin = env.BuildProgram()

#
# Target: Execute binary
#

exec_action = env.VerboseAction(
    "$SOURCE $PROGRAM_ARGS", "Executing $SOURCE")

AlwaysBuild(env.Alias("exec", target_bin, exec_action))
AlwaysBuild(env.Alias("upload", target_bin, exec_action))

#
# Target: Print binary size
#

target_size = env.Alias("size", target_bin, env.VerboseAction(
    "$SIZEPRINTCMD", "Calculating size $SOURCE"))
AlwaysBuild(target_size)

#
# Default targets
#

Default([target_bin])
