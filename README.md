# Native: development platform for [PlatformIO](https://platformio.org)
[![Build Status](https://github.com/platformio/platform-native/workflows/Examples/badge.svg)](https://github.com/platformio/platform-native/actions)

Native development platform is intended to be used for desktop OS. This platform uses built-in toolchains (preferable based on GCC), frameworks, libs from particular OS where it will be run.

* [Home](https://registry.platformio.org/platforms/platformio/native) (home page in the PlatformIO Registry)
* [Documentation](https://docs.platformio.org/page/platforms/native.html) (advanced usage, packages, boards, frameworks, etc.)

# Usage

1. [Install PlatformIO](https://platformio.org)
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
