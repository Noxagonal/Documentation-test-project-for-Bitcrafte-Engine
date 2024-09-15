# List
Provides a dynamically sized, heap allocated, continuous container similar to `std::vector`.

---

## Usage
```cpp
auto list = bc::List<int>(); // Create an empty list.
list.Reserve( 64 ); // Reserve space for 64 elements.
list.PushBack( 1 ); // Push an integer to the back, size is now 1.
list.PushFront( 2 ); // Push an integer to the front, size is now 2.
// At this point, list contents look like {2, 1};
```