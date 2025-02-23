# HyperFetch: Asynchronous HTTP Downloader

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)

HyperFetch is a feature-rich, asynchronous HTTP downloader, designed for high-performance parallel
downloads. It offers a wide range of features including retry logic, rate limiting, chunked downloads, progress
tracking, and more.

## Features

* **Asynchronous Parallel Downloads:** Download multiple URLs concurrently for maximum efficiency.
* **Retry Logic:** Configurable retry mechanism with exponential backoff for handling transient errors.
* **Timeout Control:** Granular control over connection and read timeouts.
* **Rate Limiting:** Prevent server overload with configurable rate limiting.
* **Chunked Downloads:** Support for downloading large files in chunks using HTTP Range requests.
* **Progress Tracking:** Monitor download progress with progress callbacks.
* **Content Validation:** Verify downloaded content using checksums.
* **Caching:** Avoid redundant downloads with a built-in caching mechanism.
* **Redirect Handling:** Control redirect behavior.
* **SSL/TLS Verification:** Configurable SSL/TLS verification settings.
* **Custom Headers & User-Agent:** Customize request headers and User-Agent.
* **Cookies:** Support for storing and sending cookies.
* **Authentication:** Support for basic and other forms of HTTP authentication.
* **Download Queues:** Manage large numbers of URLs with download queues.
* **Download Scheduling:** Schedule downloads for specific times.
* **Plugin System:** Extend functionality with custom plugins.
* **Logging:** Comprehensive logging for debugging and monitoring.
* **Proxy Support:** HTTP/HTTPS and SOCKS5 proxy support.
* **Skip URL functionality:** Skip specific URLs based on a callback.

## Installation

```bash
pip install hyperfetch-py
```

## Configuration

You can configure HyperFetch using the following classes:

* `RetryConfig`: Configure retry behavior.
* `TimeoutConfig`: Configure connection and read timeouts.
* `RateLimiter`: Configure rate limiting.
* `AsyncDownloader`: Main downloader class with various configuration options.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

```
