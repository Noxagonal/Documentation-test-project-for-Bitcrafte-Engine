# Overview
Bitcrafte engine is a modular game engine made of several components.

## Components

---

### Build Configuration
This is primarily a configuration component which is used to detect which OS we're compiling on, which compiler we're using and what features are supported by the compiler.

- Responsibilities:
	- Pre-build configuration.

---

### Core
Core is the foundation of the engine. The core provides essential functionality that everything else is built upon. Core includes containers like List, Array, UniquePtr and others. Core also provides low level functions like conversion functions, exception handling and other diagnostic tools, printing, logging, etc. Core also provides some higher level functionality that the user is unlikely to directly interact with, like memory pool and thread pool.

- Responsibilities:
	- System boot and setup.
	- Containers.
	- Diagnostics.
	- Memory handling.
	- Task scheduling.

---

### RHI
Render Hardware Interface enables rendering to screen, it relies on more specific RHI components to do the actual rendering however.

#### RHI_Vulkan
Render Hardware Interface using Vulkan backend.

---

### Window Manager
Window manager is an interface which enables window creation and HID input. It relies on more specific implementation.

#### Window Manager Win32
Window manager for Windows computers. This is only compiled on Windows computers.

#### Window Manager Wayland
Window manager for Linux computers which support wayland. This is only compiled on Linux computers.

#### Window Manager XLib
Window manager for Linux and other computers which support XOrg. This is only compiled on Linux and other operating systems that use XOrg.

---

### Scene
Scene contains everything related to the 3D world.

---

### UI
UI provides user interface, it keeps track of UI state and outputs rendering data.
