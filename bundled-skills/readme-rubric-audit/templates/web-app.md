<!-- Web app / self-hosted template. Pattern: immich/uptime-kuma/posthog
     (see project-types.md). UI screenshot REQUIRED before any setup.
     Docker-first install. Live demo link if one exists — with credentials
     table (immich gold standard). -->

# {app-name}

![CI](https://github.com/{owner}/{repo}/actions/workflows/{ci}.yml/badge.svg?branch=main)
![release](https://img.shields.io/github/v/release/{owner}/{repo})
![license](https://img.shields.io/github/license/{owner}/{repo})

{One sentence: what it does and for whom. ≤120 chars.}

<!-- REQUIRED: current UI screenshot. Use <picture> dark/light variant if the
     UI is theme-sensitive. -->
![{app-name} screenshot]({screenshot.png})

## Try it

{Live demo URL if any.}
<!-- If the demo needs a login, give it (immich pattern):
| Field | Value |
|---|---|
| Email | demo@example.com |
| Password | demo | -->

## Features

- {feature}
- {feature}
<!-- Multi-platform apps: a capability matrix (rows features, columns Web/Mobile). -->

## Deploy

<!-- Docker-first (observed norm). Real, tested compose content only. -->
```sh
docker compose up -d
```

{Link to full install docs for reverse proxy/TLS/backup specifics.}

> [!WARNING]
> {The one thing that loses user data if skipped — backups, volume mounts.
>  Delete this block if there is none. Alerts degrade to plain blockquotes
>  off-GitHub — acceptable here.}

## Update

```sh
{update command}
```

## Status

{Actively developed / maintenance / archived — honest, one line. Roadmap link if real.}

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[{SPDX id}](LICENSE) © {owner}
