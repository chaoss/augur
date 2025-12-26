# Augur NEW Release v0.91.0

Augur is primarily a data engineering tool that makes it possible for data scientists to gather open source software community data - less data carpentry for everyone else! 

**New to Augur?** Start with the “What is Augur?” and “How to Access Augur” sections below.

The primary way of looking at Augur data is through [8Knot](https://github.com/oss-aspen/8knot), a public instance of 8Knot is available [here](https://metrix.chaoss.io) - this is tied to a public instance of [Augur](https://ai.chaoss.io). 

[![first-timers-only](https://img.shields.io/badge/first--timers--only-friendly-blue.svg?style=flat-square)](https://www.firsttimersonly.com/)
We follow the [First-Timers-Only](https://www.firsttimersonly.com/) philosophy of tagging issues for first timers only, and walking one newcomer through the resolution process weekly. You can find these issues tagged with [first-timers-only](https://github.com/chaoss/augur/labels/first-timers-only) on our issues list.

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme) [![Build Docker images](https://github.com/chaoss/augur/actions/workflows/build_docker.yml/badge.svg)](https://github.com/chaoss/augur/actions/workflows/build_docker.yml) [![Hits-of-Code](https://hitsofcode.com/github/chaoss/augur?branch=release)](https://hitsofcode.com/github/chaoss/augur/view?branch=release) [![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2788/badge)](https://bestpractices.coreinfrastructure.org/projects/2788)

## NEW RELEASE ALERT!
**If you want to jump right in, you can find updated installation instructions for Docker, Docker Compose, and bare-metal setups [here](docs/new-install.md).**

Augur is now releasing a dramatically improved new version. It is also available [here](https://github.com/chaoss/augur/releases/tag/v0.91.0).


- The `release` branch is a stable version of our new architecture, which features:
  - Dramatic improvement in the speed of large-scale data collection (100,000+ repos). All data is obtained for 100k+ repos within 2 weeks.
  - A new job management architecture that uses Celery and Redis to manage queues, and enables users to run a Flower job monitoring dashboard.
  - Materialized views to increase the responsiveness of APIs and frontends on large-scale data.
  - Changes to primary keys, which now employ a UUID strategy that ensures unique keys across all Augur instances.
  - Support for [8Knot](https://github.com/oss-aspen/8knot) dashboards (view a sample [here](https://eightknot.osci.io/)).
  *Dashboard beautification coming soon!*
  - Data collection completeness assurance is enabled by a structured, relational data set that is easily compared with the platform API Endpoints.
- **The next release will include a hosted version of Augur where users can create accounts and add repositories they care about.**
If the hosted instance already contains a requested organization or repository, it will be added to the user’s view. If the repository or organization is new, the user will be notified that data collection will take time, depending on the scale of the request. 

## What is Augur?
Augur is a software suite for collecting and measuring structured data
about [free](https://www.fsf.org/about/) and [open-source](https://opensource.org/docs/osd) software (FOSS) communities.

We gather trace data from a group of repositories, normalize it into a unified data model, and provide a variety of metrics to help answer questions about how open source communities evolve.

Augur’s main focus is measuring the overall health and sustainability of open source projects — which are system-critical for nearly every software organization today.

At a high level, Augur collects data from multiple platforms, normalizes it into a common data model, and exposes it through APIs and dashboards such as 8Knot for analysis and visualization.

For example, one of our metrics is *burstiness*. Burstiness – how are short timeframes of intense activity, followed by a corresponding return to a typical pattern of activity, observed in a project? 
This can paint a picture of a project’s focus and gain insight into the potential stability of a project and how its typical cycle of updates occurs. 

We are a [CHAOSS](https://chaoss.community) project, and many of our
metrics are implementations of the metrics defined by our awesome community. You can find a full list of them [here](https://chaoss.community/metrics/).

For more information on [how to get involved on the CHAOSS website](https://chaoss.community/participate/).

## How to Access Augur

Augur can be accessed in different ways depending on your goals:

- **Explore existing data**: A public Augur instance powers the 8Knot dashboard available at https://metrix.chaoss.io.
- **Run Augur yourself**: Augur can be deployed locally or on a server using Docker, Docker Compose, or bare-metal setups.
- **Develop or contribute**: Developers can set up Augur locally to contribute code, experiment with metrics, or extend data collection.

Detailed setup, installation, and usage instructions are maintained in the [official documentation](https://oss-augur.readthedocs.io/en/main/).

## Collecting Data

Augur supports ```Python3.7``` through ```Python3.11``` on all platforms. ```Python3.12``` and above do not yet work because of machine learning worker dependencies. On macOS, you can create a ```Python3.11``` environment by running:
```
$ python3.11 -m venv path/to/venv
```

Augur's main focus is to measure the overall health and sustainability of open source projects. It collects more data about open source software projects than any other available software. 

One of Augur's core tenets is a desire to openly gather data that people can trust, and then provide useful and well-defined metrics that help give important context to the larger stories being told by that data.

We do this in a variety of ways, one of which is doing all our own data collection in-house. We currently collect data from a few main sources:

1. Raw Git commit logs (commits, contributors)
2. GitHub's API (issues, pull requests, contributors, releases, repository metadata)
3. The Linux Foundation's [Core Infrastructure Initiative](https://www.coreinfrastructure.org/) API (repository metadata)
4. [Succinct Code Counter](https://github.com/boyter/scc), a blazingly fast Sloc, Cloc, and Code tool that also performs COCOMO calculations

This data is normalized into a unified data model and made available for analysis and visualization.

Data collection is performed by dedicated data collection workers managed by Augur, each responsible for querying some subset of these data sources. New data source workers are actively being developed. If you have an idea for a new one, [please tell us](https://github.com/chaoss/augur/issues/new?template=feature_request.md) - we'd love your input!


## Getting Started

If you're interested in collecting data with our tool, the Augur team has worked hard to develop a detailed guide to get started with our project, which can be found [in our documentation](https://oss-augur.readthedocs.io/en/main/getting-started/toc.html).

If you're looking to contribute to Augur's code, you can find installation instructions, development guides, architecture references (coming soon), best practices, and more in our [developer documentation](https://oss-augur.readthedocs.io/en/main/development-guide/toc.html). 

Please know that while it's still rather sparse right now, we are actively adding to it all the time.

If you get stuck, please feel free to [ask for help](https://github.com/chaoss/augur/issues/new)!

## Contributing

To contribute to Augur, please follow the guidelines found in our [CONTRIBUTING.md](CONTRIBUTING.md) and the CHAOSS [Code of Conduct](https://github.com/chaoss/.github/blob/main/CODE_OF_CONDUCT.md). Augur is a welcoming community that is open to all, regardless of whether you're working on your 1000th contribution to open source or your 1st.
We strongly believe that much of what makes open source so great is the incredible communities it brings together, so we invite you to join us!

## License, Copyright, and Funding

Copyright © 2025 University of Nebraska at Omaha, University of Missouri, Brian Warner, and the CHAOSS Project.

Augur is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the [LICENSE](LICENSE) file for more details.

This work has been funded through the Alfred P. Sloan Foundation, Mozilla, The Reynolds Journalism Institute, contributions from VMWare, Red Hat Software, Grace Hopper's Open Source Day, GitHub, Microsoft, Twitter, Adobe, the Gluster Project, Open Source Summit (NA/Europe), and the Linux Foundation Compliance Summit.

Significant design contributors include Kate Stewart, Dawn Foster, Duane O'Brien, Remy Decausemaker, others omitted due to the memory limitations of project maintainers, and 15 Google Summer of Code Students. 
## Maintainers & Contributors

Refer to [CONTRIBUTORS.md](./CONTRIBUTORS.md) for detailed information about project maintainers, contributors, and GSoC participants.
