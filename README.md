# Augur

[![standard-readme compliant](https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


branch | status
   --- | ---
master | [![Build Status](https://travis-ci.com/chaoss/augur.svg?branch=master)](https://travis-ci.com/chaoss/augur)
   dev | [![Build Status](https://travis-ci.com/chaoss/augur.svg?branch=dev)](https://travis-ci.com/chaoss/augur)


[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/2788/badge)](https://bestpractices.coreinfrastructure.org/projects/2788)

## What is Augur?

Augur is a software suite for collecting and measuring structured data
about [free](https://www.fsf.org/about/) and [open-source](https://opensource.org/docs/osd) software (FOSS) communities.

We gather trace data for a group of repositories, normalize
it into our data model, and provide a variety of metrics about said
data. The structure of our data model enables us to synthesize data
across various platforms to provide meaningful context for meaningful
questions about the way these communities evolve.

We are a [CHAOSS](https://chaoss.community) project, and many of our
metrics are implementations of the metrics defined by our awesome community. You
can find more information about [how to get involved on the CHAOSS website](https://chaoss.community/participate/).

## Collecting Data

One of Augur's core tenets is a desire to openly gather data that people can trust, and then provide useful and well-defined metrics that help give important context to the larger stories being told by that data. We do this in a variety of ways, one of which is doing all our own data collection in house. We currently collect data from a few main sources:

1. Raw Git commit logs (commits, contributors)
2. GitHub's API (issues, pull requests, contributors, releases, repository metadata)
3. The Linux Foundation's [Core Infrastructure Initiative](https://www.coreinfrastructure.org/) API (repository metadata)
4. [Succinct Code Counter](https://github.com/boyter/scc), a blazingly fast Sloc, Cloc, and Code tool that also performs COCOMO calculations

This data is collected by dedicated data collection workers controlled by Augur, each of which is responsible for querying some subset of these data sources. We are also hard at work building workers for new data sources. If you have an idea for a new one, [please tell us](https://github.com/chaoss/augur/issues/new?template=feature_request.md) - we'd love your input!


## Getting Started

If you're interested in collecting data with our tool, the Augur team has worked hard to develop a detailed guide to get started with our project which can be found [in our documentation](https://oss-augur.readthedocs.io/en/master/getting-started/toc.html).

If you're looking to contribute to Augur's code, you can find installation instructions, development guides, architecture references (coming soon), best practices and more in our [developer documentation](https://oss-augur.readthedocs.io/en/master/development-guide/toc.html). Please know that while it's still rather sparse right now,
but we are actively adding to it all the time. If you get stuck, please feel free to [ask for help](https://github.com/chaoss/augur/issues/new)!


## Contributors
Thanks to these amazing folks!!
<table>
	<tr>
    <td align="center">
            <a href="https://github.com/sgoggins">
              <img src="https://avatars.githubusercontent.com/u/379847?v=4" width="100px" alt=""/><br />
              <sub><b>Sean P. Goggins</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/ccarterlandis">
              <img src="https://avatars.githubusercontent.com/u/31522931?v=4" width="100px" alt=""/><br />
              <sub><b>Carter Landis</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/gabe-heim">
              <img src="https://avatars.githubusercontent.com/u/20764846?v=4" width="100px" alt=""/><br />
              <sub><b>Gabe Heim</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/howderek">
              <img src="https://avatars.githubusercontent.com/u/835856?v=4" width="100px" alt=""/><br />
              <sub><b>Derek Howard</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/bing0n3">
              <img src="https://avatars.githubusercontent.com/u/15957393?v=4" width="100px" alt=""/><br />
              <sub><b>Bingwen Ma</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/parthsharma2">
              <img src="https://avatars.githubusercontent.com/u/22260291?v=4" width="100px" alt=""/><br />
              <sub><b>Parth Sharma</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/ChristianCme">
              <img src="https://avatars.githubusercontent.com/u/16126661?v=4" width="100px" alt=""/><br />
              <sub><b>Christian Cmehil-Warn</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/ABrain7710">
              <img src="https://avatars.githubusercontent.com/u/61482022?v=4" width="100px" alt=""/><br />
              <sub><b>Andrew Brain</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Nebrethar">
              <img src="https://avatars.githubusercontent.com/u/34951354?v=4" width="100px" alt=""/><br />
              <sub><b>Matt Snell</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/michaelwoodruffdev">
              <img src="https://avatars.githubusercontent.com/u/45110754?v=4" width="100px" alt=""/><br />
              <sub><b>Michael Woodruff</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/abuhman">
              <img src="https://avatars.githubusercontent.com/u/17164838?v=4" width="100px" alt=""/><br />
              <sub><b>abuhman</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/IsaacMilarky">
              <img src="https://avatars.githubusercontent.com/u/24639268?v=4" width="100px" alt=""/><br />
              <sub><b>Isaac Milarsky</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/mrsaicharan1">
              <img src="https://avatars.githubusercontent.com/u/25197147?v=4" width="100px" alt=""/><br />
              <sub><b>Saicharan Reddy</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/jonahz5222">
              <img src="https://avatars.githubusercontent.com/u/23271436?v=4" width="100px" alt=""/><br />
              <sub><b>Jonah Zukosky</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/germonprez">
              <img src="https://avatars.githubusercontent.com/u/656208?v=4" width="100px" alt=""/><br />
              <sub><b>Matt Germonprez</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/NodiraIbrogimova">
              <img src="https://avatars.githubusercontent.com/u/11291840?v=4" width="100px" alt=""/><br />
              <sub><b>Nodira Ibragimova</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/tretrue">
              <img src="https://avatars.githubusercontent.com/u/31676518?v=4" width="100px" alt=""/><br />
              <sub><b>Robert Lincoln Truesdale III</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/sta97">
              <img src="https://avatars.githubusercontent.com/u/45325682?v=4" width="100px" alt=""/><br />
              <sub><b>StuartA</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/aksh555">
              <img src="https://avatars.githubusercontent.com/u/25505971?v=4" width="100px" alt=""/><br />
              <sub><b>Akshara P</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/sarit-adh">
              <img src="https://avatars.githubusercontent.com/u/4488693?v=4" width="100px" alt=""/><br />
              <sub><b>Sarit Adhikari</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/ivanayov">
              <img src="https://avatars.githubusercontent.com/u/4160133?v=4" width="100px" alt=""/><br />
              <sub><b>Ivana Atanasova</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/maxbalk">
              <img src="https://avatars.githubusercontent.com/u/19540348?v=4" width="100px" alt=""/><br />
              <sub><b>Max</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Pogayo">
              <img src="https://avatars.githubusercontent.com/u/39183794?v=4" width="100px" alt=""/><br />
              <sub><b>Perez Ogayo</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/ElitaNelson">
              <img src="https://avatars.githubusercontent.com/u/43044423?v=4" width="100px" alt=""/><br />
              <sub><b>ElitaNelson</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/manangoel99">
              <img src="https://avatars.githubusercontent.com/u/32260633?v=4" width="100px" alt=""/><br />
              <sub><b>Manan Goel</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/abhinavbajpai2012">
              <img src="https://avatars.githubusercontent.com/u/24355881?v=4" width="100px" alt=""/><br />
              <sub><b>Abhinav Bajpai</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/maxhbr">
              <img src="https://avatars.githubusercontent.com/u/1187050?v=4" width="100px" alt=""/><br />
              <sub><b>Maximilian Huber</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/CMPerniciaro">
              <img src="https://avatars.githubusercontent.com/u/47083006?v=4" width="100px" alt=""/><br />
              <sub><b>CMPerniciaro</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/ortonpaul">
              <img src="https://avatars.githubusercontent.com/u/43661107?v=4" width="100px" alt=""/><br />
              <sub><b>ortonpaul</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/kmn5409">
              <img src="https://avatars.githubusercontent.com/u/27737729?v=4" width="100px" alt=""/><br />
              <sub><b>Keanu Nichols</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/GeorgLink">
              <img src="https://avatars.githubusercontent.com/u/8862021?v=4" width="100px" alt=""/><br />
              <sub><b>Georg J.P. Link</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/pratikmishra356">
              <img src="https://avatars.githubusercontent.com/u/43684300?v=4" width="100px" alt=""/><br />
              <sub><b>PRATIK MISHRA</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Nasmasim">
              <img src="https://avatars.githubusercontent.com/u/54024814?v=4" width="100px" alt=""/><br />
              <sub><b>Nasma</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/geekygirldawn">
              <img src="https://avatars.githubusercontent.com/u/1304299?v=4" width="100px" alt=""/><br />
              <sub><b>Dawn Foster</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Dhruv-Sachdev1313">
              <img src="https://avatars.githubusercontent.com/u/56223242?v=4" width="100px" alt=""/><br />
              <sub><b>Dhruv Sachdev</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/vinodkahuja">
              <img src="https://avatars.githubusercontent.com/u/25468243?v=4" width="100px" alt=""/><br />
              <sub><b>Vinod K. Ahuja</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/blaze-fire">
              <img src="https://avatars.githubusercontent.com/u/40532175?v=4" width="100px" alt=""/><br />
              <sub><b>Krishan Singh</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/jakeharding">
              <img src="https://avatars.githubusercontent.com/u/381507?v=4" width="100px" alt=""/><br />
              <sub><b>Jake Harding</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/goern">
              <img src="https://avatars.githubusercontent.com/u/260331?v=4" width="100px" alt=""/><br />
              <sub><b>Christoph Görn</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/QianqianShan">
              <img src="https://avatars.githubusercontent.com/u/14337991?v=4" width="100px" alt=""/><br />
              <sub><b>Qianqian Shan</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/GouravSardana">
              <img src="https://avatars.githubusercontent.com/u/31731827?v=4" width="100px" alt=""/><br />
              <sub><b>Gourav Sardana</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/b-kamangara">
              <img src="https://avatars.githubusercontent.com/u/27910629?v=4" width="100px" alt=""/><br />
              <sub><b>b-kamangara</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/buhmana">
              <img src="https://avatars.githubusercontent.com/u/1380628?v=4" width="100px" alt=""/><br />
              <sub><b>buhmana</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/KIRA009">
              <img src="https://avatars.githubusercontent.com/u/40872556?v=4" width="100px" alt=""/><br />
              <sub><b>Shohan</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/petermart">
              <img src="https://avatars.githubusercontent.com/u/32779280?v=4" width="100px" alt=""/><br />
              <sub><b>petermart</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/Kushal-kothari">
              <img src="https://avatars.githubusercontent.com/u/58383771?v=4" width="100px" alt=""/><br />
              <sub><b>Kush Kothari</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/gordongli">
              <img src="https://avatars.githubusercontent.com/u/21225663?v=4" width="100px" alt=""/><br />
              <sub><b>Gordon Li</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/mHash1m">
              <img src="https://avatars.githubusercontent.com/u/58783659?v=4" width="100px" alt=""/><br />
              <sub><b>Hashim</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/bparish628">
              <img src="https://avatars.githubusercontent.com/u/8492971?v=4" width="100px" alt=""/><br />
              <sub><b>Benjamin Parish</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/sg7801">
              <img src="https://avatars.githubusercontent.com/u/61888364?v=4" width="100px" alt=""/><br />
              <sub><b>Srishti Guleria</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/ajeurkar">
              <img src="https://avatars.githubusercontent.com/u/52557440?v=4" width="100px" alt=""/><br />
              <sub><b>Ajinkya Jeurkar</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Yogita98">
              <img src="https://avatars.githubusercontent.com/u/37609519?v=4" width="100px" alt=""/><br />
              <sub><b>Yogita Bhatia</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/micahswab">
              <img src="https://avatars.githubusercontent.com/u/14929251?v=4" width="100px" alt=""/><br />
              <sub><b>Micah Swab</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/rochisha0">
              <img src="https://avatars.githubusercontent.com/u/45593458?v=4" width="100px" alt=""/><br />
              <sub><b>Rochisha Agarwal</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/mbbroberg">
              <img src="https://avatars.githubusercontent.com/u/1744971?v=4" width="100px" alt=""/><br />
              <sub><b>Matt Broberg</b></sub>
            </a><br/>
   </td>
  </tr>
  <tr>
    <td align="center">
            <a href="https://github.com/jackm357">
              <img src="https://avatars.githubusercontent.com/u/24239857?v=4" width="100px" alt=""/><br />
              <sub><b>Jack</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/Ayushdubey86">
              <img src="https://avatars.githubusercontent.com/u/61616662?v=4" width="100px" alt=""/><br />
              <sub><b>Ayush Dubey</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/nynaalekhya">
              <img src="https://avatars.githubusercontent.com/u/50094420?v=4" width="100px" alt=""/><br />
              <sub><b>nynaalekhya</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/jberkus">
              <img src="https://avatars.githubusercontent.com/u/115146?v=4" width="100px" alt=""/><br />
              <sub><b>Josh Berkus</b></sub>
            </a><br/>
   </td>
   <td align="center">
            <a href="https://github.com/mureinik">
              <img src="https://avatars.githubusercontent.com/u/4173849?v=4" width="100px" alt=""/><br />
              <sub><b>Allon Murienik</b></sub>
            </a><br/>
   </td>
 </tr>
</table>

## Contributing

To contribute to Augur, please follow the guidelines found in our [CONTRIBUTING.md](CONTRIBUTING.md) and our [Code of Conduct](CODE_OF_CONDUCT.md). Augur is a welcoming community that is open to all, regardless if you're working on your 1000th contribution to open source or your 1st. We strongly believe that much of what makes open source so great is the incredible communities it brings together, so we invite you to join us!

## License, Copyright, and Funding

Copyright © 2021 University of Nebraska at Omaha, University of Missouri and the CHAOSS Project.

Augur is free software: you can redistribute it and/or modify it under the terms of the MIT License as published by the Open Source Initiative. See the [LICENSE](LICENSE) file for more details.

This work has been funded through the Alfred P. Sloan Foundation, Mozilla, The Reynolds Journalism Institute, contributions from VMWare, Red Hat Software, Grace Hopper's Open Source Day, GitHub, Microsoft, Twitter, Adobe, the Gluster Project, Open Source Summit (NA/Europe), and the Linux Foundation Compliance Summit. Significant design contributors include Kate Stewart, Dawn Foster, Duane O'Brien, Remy Decausemaker, others omitted due to the  memory limitations of project maintainers, and 12 Google Summer of Code Students.
