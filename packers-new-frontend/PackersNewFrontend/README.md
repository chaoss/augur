# PackersNewFrontend

## Setup

Run `npm install` after pulling down the code to install the dependencies. Then run `ng serve` for a dev server. Navigate to `http://localhost:4200/`.

## Sprint 4 Additions

Added bootstrap for a more polished looking webpage. We also added support for multiple metrics to be graphed for each repo. Also included simple error checking for
invalid urls.

The backend url located at `src/app/repo-info.service.ts` line 12 is currently pointing at `http://zephyr.osshealth.io:5222/api/unstable`. 
Can be changed to any augur backend.

## New features not included

- Support for comparing two repos at the same time.
- Support for more metrics using different types of graphs (bar/pie).
- More robust error checking to avoid empty graphs or support for empty repo groups.

## Challenges for augur development

- Data given by api relating to time wasn't evenly dispersed (x axis time gap between each data point varied).
- Api documentation was sometimes confusing.
- Current zephyr frontend did not work and was difficult to compare to.
- Augur api was slow to respond at times.