# Refreshed Augur UI Components
## Version 0.1.0

## Deployment
Nothing extra has been done to need any other dependency installations.
Deployment is the same as the working version of Augur

## Code Changes
- Tooltip infinite hover bug
   - `./frontent/src/views/Dashboard.vue`
   - tweaked placement of `<d-tooltip>` components according to their
   relative positions so that hovering over the buttons would not cause
   an infinite loop of hover events that impeded UI usability

## Testing Changes
Vue browser tools helps debug and inspect vuex events and mutations,
ultimately leading to tracing components and their properties in a large
codebase