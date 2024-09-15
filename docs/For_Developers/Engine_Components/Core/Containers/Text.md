# Text
Provides a dynamically sized, heap allocated, continuous container for text similar to `std::string` or `std::basic_string<TYPE>`.

## Usage
```cpp
auto char_text = bc::Text(); // Creates a `char` text container.
auto c8_text = bc::Text8(); // Creates a `c8` (`char8_t`) text container.
auto c16_text = bc::Text16(); // Creates a `c16` (`char16_t`) text container.
auto c32_text = bc::Text32(); // Creates a `c32` (`char32_t`) text container. (Most used in engine)
```