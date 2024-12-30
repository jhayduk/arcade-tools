# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased - Breaking change - planned for 1.0.0]

- Refactor GameElement so that it has a rect property of type pygame.Rect instead of being a sub-class of pygame.Rect. This can break calling code that expects GameElement to be a subclass of pygame.Rect. To migrate code, change "_object_._attribute_" to "_object_**.rect**._attribute_"


## [0.1.1] - 2024-12-29
### Added
- GameElement class.
