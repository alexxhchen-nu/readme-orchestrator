<!-- CLI tool template. Pattern: bat/ripgrep/httpie (see project-types.md).
     Visual proof is REQUIRED: terminal screenshot or GIF near the top.
     Install is the biggest section — one subsection per OS/package manager,
     but only the ones the project actually supports. -->

# {tool-name}

![CI](https://github.com/{owner}/{repo}/actions/workflows/{ci}.yml/badge.svg?branch=main)
![release](https://img.shields.io/github/v/release/{owner}/{repo})
![license](https://img.shields.io/github/license/{owner}/{repo})

{One sentence: what it does and for whom. ≤120 chars.}

<!-- REQUIRED: demo GIF or screenshot. Alt text always. Absolute URL if the
     README ships anywhere off-GitHub. -->
![{tool-name} demo]({demo.gif})

## Features

- {feature — pair each major one with a screenshot if visual (bat pattern)}
- {feature}

<!-- Optional but high-value (ripgrep pattern): a "When not to use it" line or
     benchmark table with hardware disclosed. Objectivity builds trust. -->

## Install

<!-- One subsection per supported channel. Only channels that actually work. -->
### {OS / package manager}

```sh
{command}
```

### From source

```sh
{build command}
```

## Usage

<!-- Invocation AND output, always (art-of-readme rule for CLIs). -->
```sh
$ {tool} {typical invocation}
{output}
```

{2–4 more real invocations covering the main use cases.}

## Configuration

{Where the config file lives, one example option, link to full docs.}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[{SPDX id}](LICENSE) © {owner}
