# Native: development platform for [PlatformIO](http://platformio.org)
[![Build Status](https://travis-ci.org/platformio/platform-native.svg?branch=develop)](https://travis-ci.org/platformio/platform-native)
[![Build status](https://ci.appveyor.com/api/projects/status/bxxdqmovprfd7vsu/branch/develop?svg=true)](https://ci.appveyor.com/project/ivankravets/platform-native/branch/develop)


Native development platform is intended to be used for desktop OS. This platform uses built-in toolchains (preferable based on GCC), frameworks, libs from particular OS where it will be run.

* [Home](https://registry.platformio.org/platforms/platformio/native) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/native.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](https://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:stable]
platform = native
board = ...
...
```

## Development version

```ini
[env:development]
platform = https://github.com/platformio/platform-native.git
board = ...
...
```

# Configuration

Please navigate to [documentation](https://docs.platformio.org/page/platforms/native.html).
