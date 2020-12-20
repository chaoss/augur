##Profanity Check Log#### Completed on December 20, 2020



###Profanity Found
**Text**
## references
 [edit item - manage resource policies / roles](https://github.com/dspace/dspace-angular/issues/601)

## description
this is an initial pr to implement manage of resource policies. the unit tests are not yet done. 


## instructions for reviewers

- added a link to the item policies page to the item status tab
- created the policies page component
- show the current policies for the item, and each bundle and bitstream within the item
- added the ability to edit or remove each exiting policy
- added a link to their edit group page
- added the ability to add a new policy for the item and each bundle and bitstream within the item
- added methods to the `resourcepolicyservice` to retrieve all policies for a resource and to support crud for policies

known problems due to https://github.com/dspace/dspace-angular/issues/644 :

- in the resource policy page eperson/group related to the policy should disappear from view
![schermata da 2020-04-06 20-53-52](https://user-images.githubusercontent.com/2486489/78595350-2b719b00-784a-11ea-9fc4-53d3fee3d113.png)

- in the resource policy create page the list of eperson/group should be empty after the first time you access the page
![schermata da 2020-04-06 20-54-20](https://user-images.githubusercontent.com/2486489/78595338-27457d80-784a-11ea-8540-c78a30b4a479.png)

- editing fields for policytype and action are disabled because replace operations are not yet implemented https://jira.lyrasis.org/browse/ds-4477

## checklist
_this checklist provides a reminder of what we are going to look for when reviewing your pr. you need not complete this checklist prior to creating your pr (draft prs are always welcome). if you are unsure about an item in the checklist, don't hesitate to ask. we're here to help!_

- [ ] my pr is small in size (e.g. less than 1,000 lines of code, not including comments & specs/tests), or i have provided reasons as to why that's not possible.
- [x] my pr passes [tslint](https://palantir.github.io/tslint/) validation using `yarn run lint`
- [x] my pr includes [typedoc](https://typedoc.org/) comments for _all new (or modified) public methods and classes_. it also includes typedoc for large or complex private methods.
- [x] my pr passes all specs/tests and includes new/updated specs for any bug fixes, improvements or new features. a few reminders about what constitutes good tests:
    * include tests for different user types (if behavior differs), including: (1) anonymous user, (2) logged in user (non-admin), and (3) administrator.
    * include tests for error scenarios, e.g. when errors/warnings should appear (or buttons should be disabled).
    * for bug fixes, include a test that reproduces the bug and proves it is fixed. for clarity, it may be useful to provide the test in a separate commit from the bug fix.
- [ ] if my pr includes new, third-party dependencies (in `package.json`), i've made sure their licenses align with the [dspace bsd license](https://github.com/dspace/dspace/blob/master/license) based on the [licensing of contributions](https://wiki.lyrasis.org/display/dspace/code+contribution+guidelines#codecontributionguidelines-licensingofcontributions) documentation.


##Repo ID: 22117

##Contributer ID: 85859

##Pull Request ID: 279028

###Profanity Found
**Text**
add decimal support to parseablebbox regexp; thanks and ht to @nihiliad

the b1g geoportal bounding box data attributes include decimals, ex:
"-97.991522 42.891013 -87.177541 49.892443".  as such, the 1.4.0
release parseablebbox regexp pattern could not parse any of our bboxes.

geoblacklight.viewer.map now adds a data-js-map-render-bbox attribute
upon valid bboxes, so specs can verify search result sets render an
appropriate initial map view bbox.

##Repo ID: 25217

##Contributer ID: 79968

##Pull Request ID: 183677

###Profanity Found
**Text**
added initial tests for importformatreader. now, seven different formats are imported without specifying the format and the number of imported entries is checked. should avoid bugs like #1134.

i also removed unused methods and moved a totally unrelated method to a better home.


##Repo ID: 25219

##Contributer ID: 80089

##Pull Request ID: 195728

###Profanity Found
**Text**
this is my initial pass at #89.  happy to start iterating.

the main source of uncertainty for me is around `check_hostname` on the ssl context.  i tested without that set and then fretted about it for 3 weeks now, then added it as something you could configure.  i looked at both what jupyterhub and dask distributed do, and they both have actual opinions.  i went with making the default look like what dask does because that's closest to our set of assumptions.  i'm not sure the "true" case has everything else needed to work.

##Repo ID: 25456

##Contributer ID: 129930

##Pull Request ID: 260253

###Profanity Found
**Text**
delivers https://jira.sakaiproject.org/browse/sak-32769 and also has patches for sak-32751 and extends upon sak-32737 to better handle locales in parsing and formatting locale specific input (periods vs commas).

in short, the new approach replaces the wicket `datatable` with a progressive rendering html table provided by a javascript library handsontable (https://handsontable.com/). instead of delivering all of the html on the initial request (which was taking quite a while to serve from the backend, render in the browser and then parse with javascript) we now deliver a compressed json blob in the html which we decompress in the javascript and deliver to the handsontable plugin.

there are many changes in `gradebookpage.java`.  we’ve dropped the `datatable` and all the associated renderers, panels and comparators.  this is replaced with a new custom component `gbgradetable.java` which is passed a detachable model `gbgradetabledata.java`.  the `gbgradetable` component provides the basic panel for the new html table (an empty div) plus a bunch of trimpath javascript templates which are used when rendering the new table cells, popovers and actions.  `gbgradetabledata.java` takes the `gradebookngbusinessservice` and the current session’s settings and gathers up all the data required for the table. previously this data gathering was done here and there, in the page and various panels and sometimes multiple times.  this moves it into a single spot.  

the `gbgradetable`’s model is the `gbgradetabledata`.  it pulls out the data from the model and passes to `gbgradebookdata.java`, which is a json serialisable object.  the gbgradetable
serializes `gbgradebookdata` in its `renderhead` to a json string now accessible to the javascript.  to keep the size of this json from blowing out, the scores are being compressed and packed as base64 into 3 bytes.  the javascript then unpacks these values back into decimals before passing to the handsontable plugin.

we’ve dropped the old `gradebook-grades.js`, which had all the weird and wonderful custom javascript we wrote to work with the wicket `datatable`.  much of the behaviours are now handled by the plugin which simplifies the javascript drastically.  the new file `gradebook-gbgrade-table.js` provides all the javascript to drive the handsontable plugin.  similarly, there’s a new css
file targeting the new table, `gradebook-gbgrade-table.css`.

many of the interactions with the table are still wicket events/callbacks.  as we’ve dropped many of the panels that once defined these callbacks, we’ve introduced a new set of
`action`’s which are bound to the new table component.  we can trigger these callbacks from the javascript and retain much of the previous wicket-backend behaviours. these actions are defined under the namespace `org.sakaiproject.gradebookng.tool.actions` and redefine many of the callbacks defined in the actions of the wicket panels we have replaced.

some interactions with the table are now handled by the handsontable plugin.  this includes things like sorting of column data which is all client-side now and a textual search for filtering all the of the students in the site.

nyu has been running this version of the table in production from the beginning of the summer term.

##Repo ID: 25229

##Contributer ID: 79386

##Pull Request ID: 209468

###Profanity Found
**Text**
modify federated file system connector to use initial sha1 as the basis for comparison as per the fixity check behaviour described in https://wiki.duraspace.org/display/fedora40/how+to+audit+fixity+in+a+filesystem+federation


##Repo ID: 25216

##Contributer ID: 80805

##Pull Request ID: 183380

###Profanity Found
**Text**
this is only needed if you are setting up multiple node
pools - which isn't a common case. even then, you can create
an additional nodepool for your core then - and you most likely
want to, since it should be sized differently. removing it
makes the initial setup page fully explainable.

##Repo ID: 25462

##Contributer ID: 128381

##Pull Request ID: 264587

###Profanity Found
**Text**
- use itemid for mapping items to collections on import
  not entirely sure why there was such an implicit distinction between itemid for items and id when adding collections. for an example, see http://www.zotero.org/support/dev/translators/coding#creating_collections
  
  this would now be:

``` javascript
    var item = new zotero.item("book");
    item.itemid = "my-item-id"; // any string or number
    item.complete();

    var collection = new zotero.collection();
    collection.name = "test collection";
    collection.type = "collection"; //it's also not clear to me why this is not set automatically in the zotero.collections constructor
    collection.children = [item];
    collection.complete();
```
- don't add all items to base collection on import
  i never really noticed the problem here, because i always use recursive collections. but basically, if somebody's organization strategy involves having uncatergorized items in the root of the library (or a collection that is being exported), when importing those items would be mixed in with the items in subcollections.
  
  i don't particularly like the idea of performing and additional db lookup for every single item that's being imported, but i don't currently have a better solution. i was going to keep track of items that are being assigned to collections in the "collectiondone" handler, but unfortunately there is no way to map items between those passed to `collection.complete` and those that are in the translator object passed to the "done" handler. my initial attempt was to use itemid, but itemid is not preserved when the item is saved and is actually internally redirected to `item.id`.


##Repo ID: 22063

##Contributer ID: 85207

##Pull Request ID: 194142

###Profanity Found
**Text**
bumps [mysql-connector-java](https://github.com/mysql/mysql-connector-j) from 8.0.13 to 8.0.14.
<details>
<summary>changelog</summary>

*sourced from [mysql-connector-java's changelog](https://github.com/mysql/mysql-connector-j/blob/release/8.0/changes).*

> # changelog
> # https://dev.mysql.com/doc/relnotes/connector-j/8.0/en/
> 
> version 8.0.14
> 
>   - wl#12298, connectors: expose metadata about source and binaries in unified way.
> 
>   - fix for bug#93111 (28894344), connectionurl.java contains char u+00a7 (section sign).
> 
>   - wl#12621, devapi: handling of default schema.
> 
>   - fix for bug#93340 (28970166), c/j build script is too verbose
> 
>   - wl#12462, devapi: be prepared for initial notice on connection.
> 
>   - fix for bug#28924137, wl#12463:if collection doesn't exist, coll.count() is giving a wrong error message.
> 
>   - wl#12463, devapi: standardize count method.
> 
>   - fix for bug#92508 (28747636), mysql-connector in bootclasspath causing memory leak.
> 
>   - fix for bug#25650514, updaterow() call fails with npe when ssps=true and table has multi-fld key.
> 
>   - fix for bug#25650482, refreshrow() call after updaterow() api fails when useserverprepstmts=true.
> 
>   - fix for bug#92536 (28692243), updateing server side prepstmts resultset fail.
> 
>   - fix for bug#92625 (28731795), contribution: fix observed npe in clearinputstream.
>     thanks to henning schmiedehausen for his contribution.
> 
>   - fix for bug#23045642, adding no-doc (mysqlconnj-696) results in exception.
> 
>   - fix for bug#91065 (28101003), zerodatetimebehavior=convert_to_null should not apply to 00:00:00 time columns.
> 
>   - fix for bug#92574 (28706219), when converting from varchar to java boolean, 'n' is not supported.
> 
>   - fix for bug#25642226, changeuser() not setting the database properly with sha user.
> 
>   - fix for bug#28606708, named pipe connection for x protocol returns npe, expected proper error message.
> 
> version 8.0.13
> 
>   - fix for bug#91317 (28207422), wrong defaults on collation mappings.
> 
>   - wl#12245, devapi: implement connect timeout.
> 
>   - fix for bug#21774249, unit test fails with error " 'cest' is unrecognized time zone".
> 
>   - wl#11857, devapi: implement connection pooling for xprotocol.
> 
></tr></table> ... (truncated)
</details>
<details>
<summary>commits</summary>

- [`36534fa`](https://github.com/mysql/mysql-connector-j/commit/36534fa273b4d7824a8668ca685465cf8eaeadd9) debian package copyright year update.
- [`146cea2`](https://github.com/mysql/mysql-connector-j/commit/146cea2db6e8ee530b186a1884ba5af195392799) hard-code year in debian package copyright file.
- [`36f68de`](https://github.com/mysql/mysql-connector-j/commit/36f68de51bb14193ba4c6dab95436cfc36f5ad10) gpl license book and copyright year update.
- [`ffb66d0`](https://github.com/mysql/mysql-connector-j/commit/ffb66d0affda6d559f5f2673cb6de886b949435c) wl#12298, connectors: expose metadata about source and binaries in unified way.
- [`9b2ed97`](https://github.com/mysql/mysql-connector-j/commit/9b2ed97d6358d7752a55e755321e796465a7a7a8) fix for outofrange test case.
- [`63e91a4`](https://github.com/mysql/mysql-connector-j/commit/63e91a4a1665fdc90aa4efcaa1916b5732c8402e) fix for testbug21934573.
- [`e0f4c5c`](https://github.com/mysql/mysql-connector-j/commit/e0f4c5c09c2a531ce4c2e447b7b66acdd6f77122) fix for sequentialbalancestrategy.
- [`6268b4b`](https://github.com/mysql/mysql-connector-j/commit/6268b4bc6d75c4abad5a60a4000fcb8c267af7e2) fix for outofrange test case.
- [`3467237`](https://github.com/mysql/mysql-connector-j/commit/3467237e7a8fe22194b3dcd4649e6b49b3167876) fix for bug#93111 (28894344), connectionurl.java contains char u+00a7 (sectio...
- [`b234a88`](https://github.com/mysql/mysql-connector-j/commit/b234a881baeb92a1c387630445ad8b50a0eb0376) wl#12621, devapi: handling of default schema.
- additional commits viewable in [compare view](https://github.com/mysql/mysql-connector-j/compare/8.0.13...8.0.14)
</details>
<br />

[![dependabot compatibility score](https://api.dependabot.com/badges/compatibility_score?dependency-name=mysql:mysql-connector-java&package-manager=gradle&previous-version=8.0.13&new-version=8.0.14)](https://dependabot.com/compatibility-score.html?dependency-name=mysql:mysql-connector-java&package-manager=gradle&previous-version=8.0.13&new-version=8.0.14)

dependabot will resolve any conflicts with this pr as long as you don't alter it yourself. you can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>dependabot commands and options</summary>
<br />

you can trigger dependabot actions by commenting on this pr:
- `@dependabot rebase` will rebase this pr
- `@dependabot recreate` will recreate this pr, overwriting any edits that have been made to it
- `@dependabot merge` will merge this pr after your ci passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
- `@dependabot reopen` will reopen this pr if it is closed
- `@dependabot ignore this [patch|minor|major] version` will close this pr and stop dependabot creating any more for this minor/major version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this pr and stop dependabot creating any more for this dependency (unless you reopen the pr or upgrade to it yourself)
- `@dependabot use these labels` will set the current labels as the default for future prs for this repo and language
- `@dependabot use these reviewers` will set the current reviewers as the default for future prs for this repo and language
- `@dependabot use these assignees` will set the current assignees as the default for future prs for this repo and language
- `@dependabot use this milestone` will set the current milestone as the default for future prs for this repo and language
- `@dependabot badge me` will comment on this pr with code to add a "dependabot enabled" badge to your readme

additionally, you can set the following in your dependabot [dashboard](https://app.dependabot.com):
- update frequency (including time of day and day of week)
- automerge options (never/patch/minor, and dev/runtime dependencies)
- pull request limits (per update run and/or open at any time)
- out-of-range updates (receive only lockfile updates, if desired)
- security updates (receive only security updates, if desired)

finally, you can contact us by mentioning @dependabot.

</details>

##Repo ID: 25219

##Contributer ID: 79282

##Pull Request ID: 260670

###Profanity Found
**Text**
this commit includes all of the initial work done to support versioning based on a split between submissions and publications. all submission data related to publication, such as title, abstract, citations, authors and galleys, has been moved to a new publication entity.

submissions have a "one to many" relationship to publications. each submission may have one or more publications attached to it. each publication is treated as a new version. published version data can not be modified.

- new publication entity split from submissions
- new api endpoints for publications
- workflow ui changes to support versions (publications)
- pre-publication validation checks
- new status_scheduled for publications scheduled for publication in a future issue
- deprecated many methods on the submission object
- upgrade scripts written from 3.1.x.
- tests updated to work, except for issue import.

some code is commented out or has not been updated yet. progress on remaining support for versioning will be tracked in github.

see: https://github.com/pkp/pkp-lib/projects/15

##Repo ID: 25226

##Contributer ID: 80814

##Pull Request ID: 200296

###Profanity Found
**Text**
bumps [mysql-connector-java](https://github.com/mysql/mysql-connector-j) from 8.0.14 to 8.0.15.
<details>
<summary>changelog</summary>

*sourced from [mysql-connector-java's changelog](https://github.com/mysql/mysql-connector-j/blob/release/8.0/changes).*

> # changelog
> # https://dev.mysql.com/doc/relnotes/connector-j/8.0/en/
> 
> version 8.0.15
> 
>   - fix for bug#94051 (29261254), not recommended default for 'allowloadlocalinfile'.
> 
> version 8.0.14
> 
>   - wl#12298, connectors: expose metadata about source and binaries in unified way.
> 
>   - fix for bug#93111 (28894344), connectionurl.java contains char u+00a7 (section sign).
> 
>   - wl#12621, devapi: handling of default schema.
> 
>   - fix for bug#93340 (28970166), c/j build script is too verbose
> 
>   - wl#12462, devapi: be prepared for initial notice on connection.
> 
>   - fix for bug#28924137, wl#12463:if collection doesn't exist, coll.count() is giving a wrong error message.
> 
>   - wl#12463, devapi: standardize count method.
> 
>   - fix for bug#92508 (28747636), mysql-connector in bootclasspath causing memory leak.
> 
>   - fix for bug#25650514, updaterow() call fails with npe when ssps=true and table has multi-fld key.
> 
>   - fix for bug#25650482, refreshrow() call after updaterow() api fails when useserverprepstmts=true.
> 
>   - fix for bug#92536 (28692243), updateing server side prepstmts resultset fail.
> 
>   - fix for bug#92625 (28731795), contribution: fix observed npe in clearinputstream.
>     thanks to henning schmiedehausen for his contribution.
> 
>   - fix for bug#23045642, adding no-doc (mysqlconnj-696) results in exception.
> 
>   - fix for bug#91065 (28101003), zerodatetimebehavior=convert_to_null should not apply to 00:00:00 time columns.
> 
>   - fix for bug#92574 (28706219), when converting from varchar to java boolean, 'n' is not supported.
> 
>   - fix for bug#25642226, changeuser() not setting the database properly with sha user.
> 
>   - fix for bug#28606708, named pipe connection for x protocol returns npe, expected proper error message.
> 
> version 8.0.13
> 
>   - fix for bug#91317 (28207422), wrong defaults on collation mappings.
> 
>   - wl#12245, devapi: implement connect timeout.
> 
></tr></table> ... (truncated)
</details>
<details>
<summary>commits</summary>

- [`79a4336`](https://github.com/mysql/mysql-connector-j/commit/79a4336f140499bd22dd07f02b708e163844e3d5) fix for bug#94051 (29261254), not recommended default for 'allowloadlocalinfi...
- [`76adb77`](https://github.com/mysql/mysql-connector-j/commit/76adb77ec3d11c0c34b08acbf21c700b702726a3) merge tag '8.0.14' into 'release/8.0.15'.
- [`d11fc1f`](https://github.com/mysql/mysql-connector-j/commit/d11fc1ff0d8d77562ec60c340b8f030e86643fff) post-release changes.
- see full diff in [compare view](https://github.com/mysql/mysql-connector-j/compare/8.0.14...8.0.15)
</details>
<br />

[![dependabot compatibility score](https://api.dependabot.com/badges/compatibility_score?dependency-name=mysql:mysql-connector-java&package-manager=gradle&previous-version=8.0.14&new-version=8.0.15)](https://dependabot.com/compatibility-score.html?dependency-name=mysql:mysql-connector-java&package-manager=gradle&previous-version=8.0.14&new-version=8.0.15)

dependabot will resolve any conflicts with this pr as long as you don't alter it yourself. you can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>dependabot commands and options</summary>
<br />

you can trigger dependabot actions by commenting on this pr:
- `@dependabot rebase` will rebase this pr
- `@dependabot recreate` will recreate this pr, overwriting any edits that have been made to it
- `@dependabot merge` will merge this pr after your ci passes on it
- `@dependabot cancel merge` will cancel a previously requested merge
- `@dependabot reopen` will reopen this pr if it is closed
- `@dependabot ignore this [patch|minor|major] version` will close this pr and stop dependabot creating any more for this minor/major version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this pr and stop dependabot creating any more for this dependency (unless you reopen the pr or upgrade to it yourself)
- `@dependabot use these labels` will set the current labels as the default for future prs for this repo and language
- `@dependabot use these reviewers` will set the current reviewers as the default for future prs for this repo and language
- `@dependabot use these assignees` will set the current assignees as the default for future prs for this repo and language
- `@dependabot use this milestone` will set the current milestone as the default for future prs for this repo and language
- `@dependabot badge me` will comment on this pr with code to add a "dependabot enabled" badge to your readme

additionally, you can set the following in your dependabot [dashboard](https://app.dependabot.com):
- update frequency (including time of day and day of week)
- automerge options (never/patch/minor, and dev/runtime dependencies)
- pull request limits (per update run and/or open at any time)
- out-of-range updates (receive only lockfile updates, if desired)
- security updates (receive only security updates, if desired)

finally, you can contact us by mentioning @dependabot.

</details>

##Repo ID: 25219

##Contributer ID: 79282

##Pull Request ID: 260686

###Profanity Found
**Text**
[codetriage](https://www.codetriage.com/) is an app i have maintained
for the past 4-5 years with the goal of getting people involved in
open source projects like this one. the app sends subscribers a random
open issue for them to help "triage". for some languages you can also
suggested areas to add documentation.

the initial approach was inspired by seeing the work of the small
core team spending countless hours asking "what version was
this in" and "can you give us an example app". the idea is to
outsource these small interactions to a huge team of volunteers
and let the core team focus on their work.

i want to add a badge to the readme of this project. the idea is to
provide an easy link for people to get started contributing to this
project. a badge indicates the number of people currently subscribed
to help the repo. the color is based off of open issues in the project.

here are some examples of other projects that have a badge in their
readme:

- https://github.com/crystal-lang/crystal
- https://github.com/rails/rails
- https://github.com/codetriage/codetriage

thanks for building open source software, i would love to help you find some helpers.

##Repo ID: 25219

##Contributer ID: 167748

##Pull Request ID: 197096

###Profanity Found
**Text**
adds an optional options argument to the geoblacklight function. the
bbox property can be used to set the initial map view. fixes #98.


##Repo ID: 25217

##Contributer ID: 164737

##Pull Request ID: 183457

###Profanity Found
**Text**
## removing rubocop violation

@132cbc391d01a6b858dcdc06f55df747dbc4a720

in removing the violation, i'm also exposing a method that can be
overridden or extended in a downstream implementation.

## removing exclusion that no longer applies

@b8c1aa9504f873c358f301ba4aa9e7152ea1b9dc


## removing duplicate rubocop key

@32dae1a1a4485357e82d5ccdd2b82517d1a4fd4d

with the key being declared twice, the last declaration was overriding
the initial declaration. so i'm taking the later declaration and moving
it up.

@projecthydra-labs/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 164558

##Pull Request ID: 191349

###Profanity Found
**Text**
an initial stab at https://github.com/jupyter/notebook/issues/1778. 

i've enabled "allow edits from maintainers" so feel free to push to this pr...


##Repo ID: 25237

##Contributer ID: 128403

##Pull Request ID: 220992

###Profanity Found
**Text**
**jira ticket**: https://jira.duraspace.org/browse/islandora-1857

# what does this pull request do?

closes up a race condition which could cause http timeouts for datastream byte-range requests.

# what's new?

introduces some file locking to ensure that the temporary files used in the byte-range response are not used before they are completely downloaded from fedora. 

# how should this be tested?

really, this should just get a regression test; make sure datastream byte-range requests still work.

if one want to try to see the present issue in action, firing up a pair of browser instances and attempting to play the same video with jwplayer may be able to produce the error, particularly with larger videos:

1. the first should load fine (if slowly, due to the large file)
2. the second, trying to load after the first was started while the first is still in progress (downloading the datastream to the temp directory), will likely see a shorter version of the file, and likely throw an error when hitting the end of the content it understands to be available.

with this pull request, this should no longer be possible... the second should now just wait until the file is complete, likely starting to play at approximately the same time as the first.

# additional notes:
* **does this change require documentation to be updated?** no
* **does this change add any new dependencies?** no.
* **does this change require any other modifications to be made to the repository (ie. regeneration activity, etc.)?** no
* **could this change impact execution of existing code?** `islandora_view_datastream_retrieve_file_uri()` now may throw exceptions if it is unable to reliably grab datastream content.

at some point in the future, we may want to look at doing at conditionally piping through byte-range requests to fedora, for those versions which support it... this could avoid the temp copies of files, possibly allowing the initial response to be delivered faster.

# interested parties
@diegopino @willtp87 

##Repo ID: 25218

##Contributer ID: 80031

##Pull Request ID: 250087

###Profanity Found
**Text**

**jira ticket**: [islandora-2153](https://jira.duraspace.org/browse/islandora-2153)

* other relevant links
  - https://groups.google.com/forum/#!topic/islandora/mqelsn1p0cu
  - https://github.com/islandora-labs/islandora_binary_object/issues/29

# what does this pull request do?
allows unrestricted mime type datastream replacement for those dsids/cmodels that allow so. it fixes a problem with [```function islandora_get_extensions_for_datastream(abstractobject $object, $dsid)```](https://github.com/islandora/islandora/blob/7.x/includes/mimetype.utils.inc#l75) that returns only the already in place datatream's mime type if no restrictions in the ds-composite-model are found for a given datastream, forcing people to stick to its initial ingest choice in sp like binary object (where obj is on purpose left unrestricted).
means you create an object with a zip file, you have to stick to zip. also on objects that have dsids not defined in their cmodels but ingested by some creative derivative/external code to get the unrestricted replacement option.

# what's new?
the expected behavior is restored. if your cmodel does not restrict a certain dsdi to be of certain mime type, you can freely replace existing content with any. this is also consistent with the original ingest, where that is allowed.

# how should this be tested?

install https://github.com/islandora-labs/islandora_binary_object
ingest an object using any file type as main binary (obj)
try to replace the recently ingested dsdi with a different file type
won't work

apply this pull, 
try to replace the recently ingested dsdi with a different file type
will  work

# additional notes:

* could this change impact execution of existing code?
if you are extending islandora and using ```function islandora_get_extensions_for_datastream``` as an expensive replacement for $object[$dsid]->mimetype; this won't work anymore for you. on restricted to mime types dsdi you will still get as bonus the existing $object[$dsid]->mimetype; in the response. if you need $object[$dsid]->mimetype; then please use $object[$dsid]->mimetype;

* it came to my attention that the dsid label is never replaced on ds replacement, maybe it could be beneficial to allow that somewhere.

# interested parties
@islandora/7-x-1-x-committers @mjordan @jordandukart @jonathangreen @axfelix (because he found the issue, opened the ticket and tested this fix)

##Repo ID: 25218

##Contributer ID: 80039

##Pull Request ID: 250126

###Profanity Found
**Text**
<!-- describe the changes you have made here: what, why, ... 
     link issues by using the following pattern: [#333](https://github.com/jabref/jabref/issues/333) or [koppor#49](https://github.com/koppor/jabref/issues/47).
     the title of the pr must not reference an issue, because github does not support autolinking there. -->
a rough but working initial flatpak manifest. 

the idea of this pull request is that it can be reviewed early in the development process. also i will need some help as a couple of things will needed to be decided on. i attached a list of todos, but i haven't put too much thought in to it. further i'm learning by doing here as i have only little experience with creating flatpaks. 

what are your comments? how should this be approached? my questions are:

- what build pipeline should be used?
- what identifier (app-id) should be used? 
  it must have the form of `org.developer.programm` but `org.jabref.jabref` seems a bit strange to me.
- should there be daily/beta builds hooked into flathub (documentation is not too big on that feature https://blogs.gnome.org/alexl/2019/02/19/changes-in-flathub-land/)

----

- [ ] change in changelog.md described
- [ ] tests created for changes
- [x] manually tested changed features in running jabref
- ~screenshots added in pr description (for bigger ui changes)~
- ~ensured that [the git commit message is a good one](https://github.com/joelparkerhenderson/git_commit_message)~
- [ ] check documentation status (issue created for outdated help page at [help.jabref.org](https://github.com/jabref/help.jabref.org/issues)?)
- [x] desktop file
- [ ] icon file
- [x] correct app-id
- [ ] build pipeline
  - [ ] flathub 
  - [ ] beta builds
  - [ ] stable builds
- [ ] github actions
- [x] sandbox permissions
- [x] automatic source download


##Repo ID: 25219

##Contributer ID: 120240

##Pull Request ID: 261169

###Profanity Found
**Text**
currently a `start=0` has to be passed in order to get the first page for a general search.
the problem with this is that the ui doesn't have enough context to determine which type of paging data to send along.

for example the paging on my library looks like `/api/user/content?start=lastmodified:contentid`.
while the paging for general searches looks like `/api/search/general?start=0`.

the infinite scrolling plugin gets the paging key off of the last item in the initial list it has rendered.

having an optional first page paging parameter would solve the issue.


##Repo ID: 25206

##Contributer ID: 79268

##Pull Request ID: 247001

###Profanity Found
**Text**
the proposed changes address the silent failing of adding a link to an unrecognized uri. they allow the user to correct any potential mistakes made to the initial address through a prompt dialogue. 


##Repo ID: 22063

##Contributer ID: 85249

##Pull Request ID: 194216

###Profanity Found
**Text**
https://jira.sakaiproject.org/browse/sak-34062

the initial load of the membership page can be quite lengthy, especially if the user has a lot of memberships. there is an obvious performance improvement opportunity:

- the code is asking for all the site objects twice; once for display purposes and once for obtaining the size of the list
- changing the latter to call countsites() rather than getsites() equates to large performance gains

there is also a bug in the code where the page size would be incorrect if you had used the filter results functionality. the search term needs to be input into the api call to determine the size of the list.

##Repo ID: 25229

##Contributer ID: 81000

##Pull Request ID: 210238

###Profanity Found
**Text**
i have opened a feature branch on dspace to allow easy review and improvement of the proposed patch to fix our lacking definition of private item.
https://wiki.duraspace.org/display/~bollini/dspace+item+state+definitions

the initial pr has been tested using both solr browse dao and postgresql dao (the oracle porting has been done and it was very trivial so probably no need to test it...).
the following tests have been performed:
- item submission as a generic submitter without workflow enabled using both xmlui and jspui marking the item as private
- make an existent item as private
- make public an existent private item
- widthdrawn and reinstantiate an item

what is missing?
we need to agree about the upgrade path for users that could have private items in their database. my first idea is to wirte a simple sql update statement to set withdrawn=false, in_archive= true for all the discoverable=false item that are not in workflow/workspace.
with this change the item will be unsearcheable and unaccessible to all, as in the previous version make an item private also withdrawn the item so no resoucepolicy are present for such items


##Repo ID: 22104

##Contributer ID: 79682

##Pull Request ID: 244722

###Profanity Found
**Text**
this pr makes several changes to the logic around how dspace assigns "dc.date.issued":
1. dspace no longer auto-assigns a "dc.date.issued=[today]" when missing (except as described below)
2. however, when "initial questions" are enabled from the ui, dspace will still assume "dc.date.issued=[today]" when a user says a work is "unpublished". this allows some form of backwards compatibility. institutions who have a lot of gray literature in dspace can enable "initial questions" for one or more collections to have dspace auto-assign issued dates again. (please note that "initial questions" are disabled by default in 4.0, see ds-1655)
3. also adds a new option (for sword or bulk ingest tools, etc) to pass in the literal value dc.date.issued="today" to tell dspace to set 'dc.date.issued=dc.date.accessioned". this means that you can now decide (in your import metadata) whether you want dspace to auto-assign issued dates when performing a bulk import. 
4. added new iteminstall unit tests to support this new logic

finally, i've tested this for all these scenarios:
- issued date is not specified - item will still be accepted into dspace but appears last in "browse by issue date" 
- issued date is literal "today" - dspace will auto-assign today's date
- issued date is set via ui (no initial questions) - user is required to fill out an issued date
- issued date is not set via ui (initial questions enabled + "unpublished") - dspace will still auto-assign today's date (for backwards compatibility)

this logic all seems to be working right. i'd recommend adding this to 4.0/master immediately, assuming no immediate objections.


##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 244735

###Profanity Found
**Text**
improve performance by:
- caching fields as keywordlist
- remove duplicate change listener
- remove preference access in loop

with these changes, the mega huge library of @aegit works without too much delays (the initial loading of the database is a bit slow but still ok). thus, this pr is a potential fix for #4430 and for https://github.com/jabref/jabref/issues/5071.

<!-- describe the changes you have made here: what, why, ... 
     link issues by using the following pattern: [#333](https://github.com/jabref/jabref/issues/333) or [koppor#49](https://github.com/koppor/jabref/issues/47).
     the title of the pr must not reference an issue, because github does not support autolinking there. -->


----

- [ ] change in changelog.md described
- [ ] tests created for changes
- [ ] manually tested changed features in running jabref
- [ ] screenshots added in pr description (for bigger ui changes)
- [ ] ensured that [the git commit message is a good one](https://github.com/joelparkerhenderson/git_commit_message)
- [ ] check documentation status (issue created for outdated help page at [help.jabref.org](https://github.com/jabref/help.jabref.org/issues)?)


##Repo ID: 25219

##Contributer ID: 80088

##Pull Request ID: 261246

###Profanity Found
**Text**
included are two implementations of filesystemhandler for storage of content resources in cloud services, using the jclouds libraries: one for openstack swift using its explicit api and one using the generalized blobstore api (primarily aimed at aws s3). the readme includes much more detail.

the initial swift implementation came from opencollab za (https://github.com/opencollabza/sakai-openstack-swift) and i repackaged it, made some upgrades, and built out the blobstore handler. i also made a subtree merge to pull this into the sakai source tree for this pull request.

note that licensing information must be added before this can be merged.


##Repo ID: 25229

##Contributer ID: 81009

##Pull Request ID: 205831

###Profanity Found
**Text**
... proj. gutenberg - fix some import categories; proquest - fix tags; pion - callback; google patents - fix initial capitalization. the others should just be test updates (and running them through js-beautify)


##Repo ID: 22053

##Contributer ID: 81860

##Pull Request ID: 193579

###Profanity Found
**Text**
updating to rdf parser v0.8 from http://dig.csail.mit.edu/hg/tabulator/

there are a couple improvements over the old parser. some discussion at https://groups.google.com/d/topic/zotero-dev/-l6pkcigwks/discussion

applied many of simon's modifications to the rdf parser from 3 years ago, but may have missed several that were made to the initial commit.

from my testing, the serialization seems to be identical to what we had before.

i tested several sites with embedded metadata and it doesn't seem to break anything.

this does not include rdfa support, since i think that's still somewhat experimental, but the code is there in the tabulator repo and merging it in should not be a big deal. i'm up for doing it after the base code is approved.

i'm not really sure if my ideas for rdf/init.js and rdf.js are great, so comments would be appreciated.


##Repo ID: 22063

##Contributer ID: 85207

##Pull Request ID: 194035

###Profanity Found
**Text**
in  #1755, i asked if the spawner state could be passed through the api.  my use case is `cull_idle_servers.py`, where i have profilespawner and cull things differently depending on what resources are used (this will require a custom culler, but that's just a fact of life).  right now, i hack it by making a separate independent database connection to read this state.

this is an initial implementation of this, adding the attribute 'state' to servers, or 'server_state' to the user model (unnamed servers).  only admin users can get this state, since it might be confidential for some spawners.  it seems to work for me, but there is probably more work to do.

currently, at least two tests fail because the state is non-deterministic, but i'd rather get feedback before going deeper to save myself effort in case this isn't wanted.  (and some tests that pass could start failing later, and other tests could start failing later so that needs fixing).

what do you think?

(another option would be a spawner option for lifetime that gets passed through.  i use batchspawner, which has a maximum total life but doesn't use recent activity.  this option seems like one of the cleanest separations.)

##Repo ID: 25439

##Contributer ID: 142785

##Pull Request ID: 254537

###Profanity Found
**Text**
theoretically this should be simple to test, but my initial attempt so far hasn't been great.

here i mimic the tests used in [dockerspawner](https://github.com/jupyterhub/dockerspawner/blob/master/tests/test_dockerspawner.py) to do an integrated test with a mocked jupyterhub. this unfortunately hangs somewhere, and its not in my code. i suspect i'm using the mocked hub incorrectly.

i can confirm that everything works fine in a production setting, the issue here is just getting a test environment running.

##Repo ID: 25484

##Contributer ID: 166684

##Pull Request ID: 256549

###Profanity Found
**Text**
updated pr (to replace pr #636). this one provides a couple of extra fixes around unit testing which seemingly help avoid travis ci "killed" messages. these fixes include:
- first, just enabling mirage2 build process for travis ci. i chose to preinstall mirage2 prerequisites via our .travis.yml (in the `before_install` settings) to speed up the mirage 2 build. see https://github.com/tdonohue/dspace/commit/a0f44f618244964df5caf7402452fd0511d153da
- improve the memory management of unit tests. namely, ensure any context objects are fully closed and set to null, to try to decrease memory usage of individual unit tests. see https://github.com/tdonohue/dspace/commit/d4d63083bbca66dcf506ff5dc437f109680ab013
- minor pom reorganization which _disables_ all unit testing related maven plugins by default (i.e. they are only enabled when unit testing is being performed). this is needed to enable the next travis ci tweak.. see https://github.com/tdonohue/dspace/commit/bd98997dd69996139a051e5d0fcc045ff07af12a
- change travis ci settings to run `mvn install -p !dspace` prior to the actual build & test. the idea is to split up the downloading of dependencies from the build & test, to hopefully help keep our memory usage lower. therefore, this setting ensures most dspace maven dependencies are downloaded, but it _skips_ building the 'dspace' module (so dspace isn't actually packaged up), which speeds up this initial build. the "-p !dspace" setting required the pom reorg mentioned above. see https://github.com/tdonohue/dspace/commit/8b53258b5ee8ba7ddf76e505f5b65aa6b6dfa57f

this all seems to be working much better on my own travis ci builds. let's see what travis says about this new pr though.


##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 244995

###Profanity Found
**Text**
https://jira.sakaiproject.org/browse/sak-40345

this patch fixes two issues with announcement sorting, one bug and one usability feature:
1.  a bug where the first time clicking on a sorting header, the sort will take any 'overflow' (based on the number of items being viewed) from the top of the list first, making the 'first x items' of a list actually be the _last_ x items, though sorted correctly on-screen
* example: in a list of items named 1-250 (created in ascending order), viewing 200 items, the first click of "modified by" would show items 50-250, correctly sorted by date, while items 1-49 (which should be the earliest and thus on the initial screen) are pushed off to first overflow page.
2. if you were looking at a subset in the middle of the list (say, announcments 21-40 out of 60), doing a re-sort by clicking a column header would leave you looking at 21-40 of the new sort order, rather than re-sorting then showing you the first 20 of whatever you wanted.

##Repo ID: 25229

##Contributer ID: 81000

##Pull Request ID: 210594

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-2231
uses console.readpassword(), to not echo the user's password when they create a user on the command line with `/dspace/bin/dspace create-administrator`

```
peterdietz:dspace5 peterdietz$ /dspace/bin/dspace create-administrator
creating an initial administrator account
e-mail address: peter2@domain.com
first name: peter2
last name: dietz2
password will not display on screen.
password: 
again to confirm: 
is the above data correct? (y or n): y
administrator account created
```


##Repo ID: 22104

##Contributer ID: 171236

##Pull Request ID: 245074

###Profanity Found
**Text**
when setting up a development server rake db:seed will create initial accounts for testing. uses the emails from role_map.yml.

##Repo ID: 22049

##Contributer ID: 85055

##Pull Request ID: 190790

###Profanity Found
**Text**
this is a stub for a work in progress.  the goal is to provide a module for efficiently and easily applying algorithms for inferring the hidden state of a system, denoted `x`, generated from the following bit of code,

``` python
x[0] = np.random.multivariate_normal(mu_0, sigma_0)
for t in range(t)
  e1[t] = np.random.multivariate_normal(0, q)
  e2[t] = np.random.multivariate_normal(0, r)
  x[t+1] = a.dot(x[t]) + b[t] + e1[t]
  z[t] = c.dot(x[t]) + d[t] + e2[t]
e2[t-1] = np.random.multivariate_normal(0, r)
z[t-1] = c.dot(z[t-1]) + d[t-1] +  e2[t-1]
```

the initial goal is to provide 3 algorithms.  the first two, the [kalman filter](http://en.wikipedia.org/wiki/kalman_filter) and [kalman smoother](http://inst.eecs.berkeley.edu/~cs294-40/fa08/scribes/lecture14.pdf), are for estimating `x` given observations `z`, state transition matrix `a`, transition offsets `b`, observation matrix `c`, observation offsets `d`, and covariance matrices `q` and `r`.  the two algorithms differ in one aspect: while the filter estimates `x[t]` using `z[0:t]`, the smoother estimates the same using `z[0:t]` at additional computational cost.  the third algorithm, the [em algorithm](http://en.wikipedia.org/wiki/expectation%e2%80%93maximization_algorithm) as applied to the linear-gaussian system, iteratively approximates `a`, `c`, `b`, `d`, `q`, `r`, `mu_0`, and `sigma_0` by maximizing the likelihood of the observations.

current progress:
- kalman filter, kalman smoother implemented, tested
- example provided
- test dataset added
- estimation of all model parameters, including transition matrices, offsets, covariance matrices, and initial state distribution.
- handle missing observations
- user's guide documentation

future:
- cython implementation
- handle multiple independent observation sequences.
- get module reference documentation working
- implement extended kalman filter or unscented kalman filter

all comments and suggestions are appreciated.  this is my first significant contribution to an open source project, so i can use all the help i can get!


##Repo ID: 25240

##Contributer ID: 129204

##Pull Request ID: 223503

###Profanity Found
**Text**
sort of an initial commit, to see what you guys think of this.

i think it's probably somewhat slower than the original way of doing things, since it involves quite a few more `document.evaluate` calls, but imo it makes the translator cleaner and easier to maintain. we can probably keep the former structure if you guys want.

localization is not complete. it's a little tedious and takes a bit of time. if someone cares to contribute, it's just a bunch of copy-pasting. all you have to do is use the test case pages and copy the corresponding labels from different languages. the localization table is towards the end of the translator. i'll probably do a couple languages at a time. two are done sort of as a proof of concept.


##Repo ID: 22053

##Contributer ID: 85207

##Pull Request ID: 193706

###Profanity Found
**Text**
prior to this, colours and labels for jobs in the two dag graphs were
jumbled up.

the code incorrectly assumed that iterating over a dict would iterate in
the order that the entries appear in a hard-coded literal dict in the
source tree.

for example:

the code assumed that the first element added to the node_traces list, and
thus the element referred to by node_traces[0], would be the element in
groups_list with value (0,...)

this incorrect assumption led to adding dag nodes to the wrong scatter
object.

this patch changes the way that the node_traces list is constructed by
populating it with marker places and then using index notation to set the
appropriate entry in the list based on hard-coded index.

further, that wrong scatter object then had its colour mutated. this patch
sets the colour correctly on initial creation and does not change it again.

for the dag coloured by state plot, the naming if-statement had no final
else: case, leading to some nodes being incorrectly labelled. this patch
adds an 'unknown' case which is reached, for example, in jobs which are
never launched due to dependency failure.

##Repo ID: 25238

##Contributer ID: 128900

##Pull Request ID: 265525

###Profanity Found
**Text**
thanks for the update of the nzz translator after site redesign.

i've reviewed and tested the translator.
i've made some improvements:
- use titleprefix
- fix teaser
- set language
- discover 'nzzas'
- change label to nzz after site redesign

(i'm the initial author this translator, but i'm using another nickname on github.)


##Repo ID: 22053

##Contributer ID: 85253

##Pull Request ID: 193710

###Profanity Found
**Text**
i've reworked the newsnet translator:
- add 24heures.ch and berner oberländer which are form the same group and using the same content management framework
- rename translator file and label
- add title prefix
- add language

(i'm the initial author of this translator, but i'm using another nickname on github.)


##Repo ID: 22053

##Contributer ID: 85253

##Pull Request ID: 193711

###Profanity Found
**Text**
some initial changes to bring this up to date with prism 2.0 spec.

also added some missing items from the 1.2 spec. a couple items were rearranged to prefer prism, og, and eprints over dc.

prism 2.0 adds prism:role attribute to the dc:creator and dc:contributor tags, which we can use to set proper roles. this might need extensive modifications to how creators are handled inside rdf.

prism 2.0 introduces xml:lang attribute to many of the tags. we might want to consider preparing the translator for localization.

we can also use prism:genre and prism:aggregatortype just like we do in em to determine itemtype. it might be safe to mostly just copy-paste.


##Repo ID: 22053

##Contributer ID: 85207

##Pull Request ID: 193648

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-2146

this change was discussed in the 11/12 dspace meeting.  submitting an initial solution for this ticket.


##Repo ID: 22104

##Contributer ID: 85805

##Pull Request ID: 245102

###Profanity Found
**Text**
this is the initial implementation.

##Repo ID: 25229

##Contributer ID: 80628

##Pull Request ID: 210794

###Profanity Found
**Text**
this branch addresses some of the initial issues that showed up during the jspui review, these include:
- usage of the old 0 & 1 identifiers to retrieve groups. on new installations these identifiers will not be present, best to use findbyname().
- reenabling the "gen_random_uuid()", this function is only available from postgres 9.4 but is required to generate uuid for the dspace objects. (we should change the postgres version in the docs as soon as this pull request is merged in master).
- over eager search & replace that altered the path of a jsp file


##Repo ID: 22104

##Contributer ID: 85802

##Pull Request ID: 245411

###Profanity Found
**Text**
1. setup ng2-translate
2. added initial en.json
3. translate some static content

i included some examples of using data and also manually translating from code.

##Repo ID: 22117

##Contributer ID: 85818

##Pull Request ID: 194736

###Profanity Found
**Text**
this pr begins to add the needed logic to allow authenticators to provide groups to the hub. this includes:

* added a new optional key, `groups`, to the user model that is a list of groups (in addition to `name` and `auth_state`).
* if provided, the authenticator will make sure those groups are added to the hub's db and that the user is part of those groups.

additional follow on work:

- [ ] decide if any of the authenticators we maintain should populate the `groups` key from the upstream identity providers.
- [ ] work through the details of when the hub should re-query the authenticator for updates group membership. the main usage case for this is if a user logs in, and it later removed from a group. we want to make sure we can invalidate that group membership while they are still logged in. this same update question will also apply to `auth_state`.

the design of this was informed by some initial work we did this week integrating keycloak with jupyterhub. keycloak makes it really easy to popular the users groups and customize the `auth_state`.

@yuvipanda @minrk @zsailer @townsenddw

@zsailer can you take this over and add tests?




##Repo ID: 25439

##Contributer ID: 128303

##Pull Request ID: 254660

###Profanity Found
**Text**
trying to close #2816

i'd like some quick, initial feedback on this. 

i am checking the tests. the ui needs some work too (maybe a directory picker instead of a text box?) 

thanks.


##Repo ID: 25237

##Contributer ID: 128542

##Pull Request ID: 221476

###Profanity Found
**Text**
`:dependent => :restrict` with a `has_many` throws a `activerecord::deleterestrictionerror` exception when `destroy` is called on the object. 

my initial intuition was that it would return a false with errors in the base object. my intuition was wrong, but i wish it was documented better so i can rescue from the exception.


##Repo ID: 1

##Contributer ID: 84715

##Pull Request ID: 232607

###Profanity Found
**Text**
fixes issue with scroll wrapping in initial viewport: https://github.com/sourcelair/xterm.js/pull/768

##Repo ID: 25237

##Contributer ID: 128601

##Pull Request ID: 221276

###Profanity Found
**Text**
if init_spawners takes too long (default: 10 seconds) to complete, app start will be allowed to continue while finishing in the background.

adds new `check` pending state for the initial check.

checking lots of spawners can take a long time, so allowing this to be async limits the impact on startup time at the expense of starting the hub in a not-quite-fully-ready state.

if we determine that this is super reliable, we can reduce the default timeout to zero.

closes #2525

##Repo ID: 25439

##Contributer ID: 128296

##Pull Request ID: 254876

###Profanity Found
**Text**
removes osd and instead uses leaflet-iiif

leaflet-iiif still has some funky stuff about centering the initial image, but i believe that will get smoothed out once we have more images to test.

also renames `leaflet` submodule to `map`. i felt that was more appropriate now, but open to suggestions.


##Repo ID: 25217

##Contributer ID: 79473

##Pull Request ID: 183479

###Profanity Found
**Text**
at the jupyterhub/binderhub workshop, one of our ideas was to make a conceptual intro to jupyterhub so that people could know what it does, and in particular what it doesn't do (what is handled by other components).  we get many issues that end up misdirected or that have a root cause of not understanding what the components are.

this pr is my initial draft - comments welcome.  i've written it informally and with a certain opinion - it's supposed to be like a teaching giving a first lesson, and not technical reference.  it goes far beyond just jupyterhub, but the reason for having it here is that you *really* need to start knowing this stuff once you start administrating a jupyterhub, before that you can sort of get by without a perfect mental model.

issues i know of:
- [ ] what is a proper title?
- [x] where should it go under the table of contents?
- [ ] i used the very verbose "single-user notebook server", i'd like a shorter term that still avoids ambiguity.
- [ ] all parts need fact-checking, because i haven't done that yet
- [x] after the content is somewhat stable, we need to add links and references.
- [x] intro needs improvement and we should make sure it explains the purpose well
- [ ] conclusion needs improvement and guides to what is next

##Repo ID: 25439

##Contributer ID: 142785

##Pull Request ID: 254879

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-2777

this pr officially fixes oai-pmh to work properly (at least at a minimal level) after the service api refactor.  note: i have not tested every feature in oai-pmh, but oai-pmh now loads properly and functions at a basic level.

involved the following:
- updates oai-pmh to use the same 'applicationcontext.xml' as all other webapps (to initialize dspace services)
- stops attempting to inject `handleservice` and just loads it via its provided factory
- restores `dspacesetrepository` classes (accidentally removed during the initial refactor). they are required for oai-pmh sets to work.
- adds a new `communityservice.findall()` method that supports limit/offset. i based this off the method of the same name/type in the `collectionservice`. this was required to support the `dspacesetrepository`.

@kevinvdv , if you have a moment, can you give this a sanity check?  it all seems to work, but i'd like your opinion as the service-based api creator/expert.


##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 245455

###Profanity Found
**Text**


this pr connects to #17 

i rewrote the collapsing of the header using ngrx, and everything seems to work fine with ngrx and universal.

### a little bit of an explanation:
- all actions having to do with the header can be found in `header.actions.ts`
  - they are `collapse`, `expand`, and `toggle`
  - the actions class contains an action type, and a function to create it, for each action. this is my take on https://github.com/erikras/ducks-modular-redux
- `header.reducer.ts` contains an interface to represent the state of the header, an initial state, and the reducer function:
  - the state is simply an object containing the boolean `navreduced`
  - on collapse it's set to true, on expand it's set to false, on toggle it's flipped
  - `object.assign({}, state, {…})` is used to create a new state object, containing the required change without altering the original state object
- the contents of the collapse, expand and toggle functions in header.component.ts have been replaced with `this.store.dispatch(…)` calls with actions of the corresponding type
- in the `ngoninit` function of the header component a new observable `isnavbarcollapsed` is initialized.
  - this is done by selecting the correct reducer from the store and mapping it to fit an `observable<boolean>`.
- in `header.component.html` the `isnavbarcollapsed` observable is used instead of the function that was there before.

when a user clicks the toggle button:
- the header component dispatches the toggle action
- the reducer receives the action, and updates the state
- this triggers a new event for the `isnavbarcollapsed` observable, which updates the ui

### effects
the navbar also collapsed when the window was resized or when the route chagned. to do these things i added another reducer: the `hostwindowreducer`.  this only has a single action: `resize`. it contains the new width and height of the window as its payload. when angular detects a window resize in `appcomponent` a `resize` action is dispatched.

the response to a `resize` action should be that the header's `collapse` action is dispatched, after that, the ui will take care of itself. 
the same thing happens in response to an `update_location` from the router (provided by the [@ngrx/router-store module](https://github.com/ngrx/router-store)) 
these reactions are specified in header.effects.ts.

effects (short for _side effects_) listen for actions, can transform their payloads and can dispatch new actions as a result. they can be used in this simple case to respond to the route changing or the window resizing, but they're more commonly used to fetch data from the rest api for example:
- an action is dispatched to initiate a call: e.g. `find_all_users`
- the reducer changes the state accordingly: e.g. sets `isloading` to true
- the effect picks up on the `find_all_users` action, and does an http call to the rest api
- when the call returns, the effect can use rxjs operators on the result to get the payload: a list of user objects for a `find_all_success` action. 
- and in it's catch block the effect can dispatch a `find_all_error` action with the error message as its payload
- to either of those actions, the reducer responds by setting `isloading` to false and either adding the list of users to the state, or adding the error message to the state
- a component subscribed to the list of users will update when it changes, so will a component subscribed to the error message.

### aggregator files
- i've also added the files app.reducers.ts and app.effects.ts to aggregate all reducers and effects and prevent them having to be added to app.module seperately. 
- these aggregator files should be made at the level of each module

##Repo ID: 22117

##Contributer ID: 85848

##Pull Request ID: 194740

###Profanity Found
**Text**
by default, the title of a course site is not editable.

in sak-29823 we enforced the titlenoteditable property in all scenarios,
including initial site creation, so that instructors could not change
the title of a course site. this assumed that a roster would always be
chosen for the course site and the title would be taken from the
roster. this lead to problems when the "continue with no roster" feature
was enabled (it is off by default), so in sak-31261 changes were made to
address that problem which essentially reverted sak-29823, allowing
instructors to change course site titles during site creation.

this patch attempts to address both uses cases above. if a course site
is using a roster, the title will not be editable. if an instructor
chooses to "continue with no roster", a site title must be provided, so
we allow it to be edited. this is accomplished by checking to see if a
roster is attached or not.

due to the setup process being a wizard that maintains state between
pages, it is possible to first select a roster, then go back and decide
to continue with no roster. previously the old roster would remain in
the state and would be considered attached for the checks above, so this
patch clears any roster selections from the state when "continue with no
roster" is chosen. it also attempts to detect if the site title and/or
description were assigned by the roster selection and removes them
unless the user has edited them already.

##Repo ID: 25229

##Contributer ID: 81025

##Pull Request ID: 208661

###Profanity Found
**Text**
…hen initial button is pressed

##Repo ID: 25229

##Contributer ID: 167349

##Pull Request ID: 208671

###Profanity Found
**Text**
this loads the intermediate page and extracts the pdf url from the meta refresh. the most annoying part of this is that the intermediate page url from the js drop-down doesn't seem to be in the dom after the page has loaded, but it's in the initial html, so this refetches the html. there's probably a way to get the intermediate url without doing that. (if we were really desperate we could simulate a click, but that's probably not necessary.)

this also uses a new method for determining whether the user has access to the pdf or would get a "your organization may be charged for transactional access to this non-subscribed article." page (which has a continue button, but presumably we don't want to touch that).

this could use some testing, particularly for the access-checking part — there may be a better way to test for that, or there may be other versions of that access box. (i didn't want to test for the text strings (e.g., "get full text elsewhere") because i'm not sure if they're localized.)

##Repo ID: 22053

##Contributer ID: 80779

##Pull Request ID: 250670

###Profanity Found
**Text**
# added title to the vignette

## description
changed moved the initial title so that will show up on https://docs.ropensci.org/rsnps/articles/

## related issue
fix #90 



##Repo ID: 26036

##Contributer ID: 82336

##Pull Request ID: 256473

###Profanity Found
**Text**
changed initial subdomain from www. to mathscinet.. also updated test cases.
fixes #1451.

##Repo ID: 22053

##Contributer ID: 121473

##Pull Request ID: 250706

###Profanity Found
**Text**
this pr is an initial attempt at generating orcid v2.1 java source code, based on the orcid-source xsds at: https://github.com/orcid/orcid-source/tree/master/orcid-model/src/main/resources

this java source code was generated via the instructions in our [readme](https://github.com/dspace/orcid-jaxb-api/blob/master/readme.md).  

it currently only includes the following xsds:
* all xsds in [common_2.1](https://github.com/orcid/orcid-source/tree/master/orcid-model/src/main/resources/common_2.1)
* all xsds in [record_2.1](https://github.com/orcid/orcid-source/tree/master/orcid-model/src/main/resources/record_2.1)

the custom jaxb binding (loosely based off dspace-cris's) used to generate this source code is stored in this repo at: https://github.com/dspace/orcid-jaxb-api/blob/master/src/main/resources/binding/orcid-2.1.xjb  comments or updates on that binding also welcome -- submit a pr or add a comment here.

while the generated java source code need not be versioned / stored in github, i'd recommend doing so, simply as a reference for developers. otherwise, debugging issues in generated code may be more complex. additionally, storing generated source code in github allows us to more easily version it / tag it, etc.

feedback welcome. 

*please do not merge* until we verify this helps simplify https://github.com/dspace/dspace/pull/2028

**how to test**
* for easier testing, i've deployed this as a snapshot to sonatype: https://oss.sonatype.org/content/repositories/snapshots/org/dspace/orcid-jaxb-api/2.1.0-snapshot/
* if you do not want to use the snapshot version in sonatype, you can build locally by doing this:
    * checkout this pr's branch, and build the `orcid-jaxb-api-2.1.0-snapshot.jar` (via `mvn -u clean package`)
    * install thar jar manually in your local maven:
       ```
       mvn install:install-file
        -dfile=orcid-jaxb-api-2.1.0-snapshot.jar
        -dgroupid=org.dspace
        -dartifactid=orcid-jaxb-api
        -dversion=2.1.0-snapshot
        -dpackaging=jar
        -dgeneratepom=true
       ```
* checkout https://github.com/dspace/dspace/pull/2028
* add this dependency to the root pom, e.g.
  ```
  <dependency>
      <groupid>org.dspace</groupid>
      <artifactid>orcid-jaxb-api</artifactid>
      <version>2.1.0-snapshot</version>
  </dependency>
  ```
* remove all `org.orcid.*` source files added by https://github.com/dspace/dspace/pull/2028
* as needed, update https://github.com/dspace/dspace/pull/2028 code to use any new package/class names in this `orcid-jaxb-api` project.


##Repo ID: 22119

##Contributer ID: 85035

##Pull Request ID: 194808

###Profanity Found
**Text**
# summary

one major difference between `drake` and most other pipeline tools is that users declare dependencies *implicitly* in their plans and workspaces. other pipeline tools like make declare dependencies *explicitly* with rigorous build rules. the jump from *implicit* components to *explicit* dependency information is time-consuming and nontrivial, so in addition to the workflow plan data frame, i think we need a special data structure whose sole purpose is to store the full dependency detection results of the code analysis. i believe this will pave the way to make `drake` cleaner and faster in the long run.

# implementation

```r
load_mtcars_example()
config <- drake_config(my_plan)
str(config$ordinances)
```

this data structure is a list, and each element corresponds to a target or import. each target's corresponding element of `ordinances` has the complete specification of immediate dependencies (other targets, output files, input files, etc.) the trigger, and all the fields of the workflow plan data frame for fast lookup. 

`config$ordinances` is a list. i thought about making it an environment so lookup would be even faster, but then we would not be able to use `lightly_paralleize()` to run through it. i am open to other suggestions. either way, lookup should be constant-time, and we might see a little improved performance.

# plans for merging

i will be on vacation from november 15 through 27, and i will wait to merge this pr until i come back. i want to be present to address any bug reports, and i want more time to think about the name. "ordinances" is a good initial name because it is distinctive and thus easy to `sed` out later, but i am not totally sold on it.

# related discussion and issues

this pr implements #440, and i believe this is essentially what @gmbecker originally suggested in #504. #498 and #575 is also related.

cc @krlmlr 

# checklist

- [x] i have read `drake`'s [code of conduct](https://github.com/ropensci/drake/blob/master/conduct.md), and i agree to follow its rules.
- [x] i have listed any substantial changes in the [development news](https://github.com/ropensci/drake/blob/master/news.md).
- [x] i have added [`testthat`](https://github.com/r-lib/testthat) unit tests to [`tests/testthat`](https://github.com/ropensci/drake/tree/master/tests/testthat) to confirm that any new features or functionality work correctly.
- [x] i have tested this pull request locally with `devtools::check()`
- [x] this pull request is ready for review.
- [ ] i think this pull request is ready to merge.


##Repo ID: 25864

##Contributer ID: 166911

##Pull Request ID: 214901

###Profanity Found
**Text**
an initial pass at sphinx docs for jupyterhub.

to do:
- [ ] integrate readme content
- [ ] add content from folders other then docs


##Repo ID: 25439

##Contributer ID: 122355

##Pull Request ID: 253918

###Profanity Found
**Text**
a while back, you may remember the great `scale_c fiasco` of 2012..
after much discussion, it was decided that we drop the use of the `scale_c` parameter.
the following example is based on the initial plots that @amueller did.
you may recognize the plots from the mailing list discussions regarding the issue.

the example will hopefully serve as a reference tool, that can be used to explain to the next
person that sends a `serious bug` titled message to the mailing list how it works.

i wouldn't say the example is entirely ready for merging..
i would really first like some feedback on it from you all regarding readability, making sense,
getting the point across and mistakes.

the plots are shown below

thanks in advance
j

---

![svc l1 case ](http://oi45.tinypic.com/2nar59h.jpg)

![svc l2 case](http://oi47.tinypic.com/mi1d29.jpg)

---


##Repo ID: 25240

##Contributer ID: 129069

##Pull Request ID: 223571

###Profanity Found
**Text**
# summary

`drake` gets initial dependencies from the user's environment rather than script files. however, environments are brittle, so targets can falsely invalidate if you run `make()` in a stale r session. this pr implements safeguards and reminders for `make()` in interactive mode. if the r session is interactive and some targets are out of date, `make()` prompts you with a menu to keep you from accidentally mangling your project. it also reminds you to read #761 regardless of how your targets are doing.

```r
> interactive()
[1] true
> library(drake)
> plan <- drake_plan(x = 1, y = 2)
> make(plan)
2 outdated targets:
  x
  y

really run make() in interactive mode?
considerations: https://github.com/ropensci/drake/issues/761 

1: yes
2: no

selection: 1
target x
target y
make() in interactive mode requires extra care:
https://github.com/ropensci/drake/issues/761
> make(plan)
all targets are already up to date.
make() in interactive mode requires extra care:
https://github.com/ropensci/drake/issues/761
```

you can disable the menu with `make(force = true)` or `options(drake_force_interactive = true)`.

cc @milesmcbain, @ha0ye

# related github issues and pull requests

- ref: #761 (not necessarily fixed)

# checklist

- [x] i have read `drake`'s [code of conduct](https://github.com/ropensci/drake/blob/master/conduct.md), and i agree to follow its rules.
- [x] i have listed any substantial changes in the [development news](https://github.com/ropensci/drake/blob/master/news.md).
- [x] i have added [`testthat`](https://github.com/r-lib/testthat) unit tests to [`tests/testthat`](https://github.com/ropensci/drake/tree/master/tests/testthat) to confirm that any new features or functionality work correctly.
- [x] i have tested this pull request locally with `devtools::check()`
- [x] this pull request is ready for review.
- [x] i think this pull request is ready to merge.


##Repo ID: 25864

##Contributer ID: 166911

##Pull Request ID: 214959

###Profanity Found
**Text**
this addresses https://jira.duraspace.org/browse/fcrepo-1271

the jms headers are currently sent such that the baseurl value has a trailing slash and the identifier header has an initial slash. this makes it cumbersome for clients to compose the two values.

this pr strips off any trailing slash from the baseurl value before sending a message to a broker.


##Repo ID: 25216

##Contributer ID: 79819

##Pull Request ID: 183297

###Profanity Found
**Text**
## description of the issue/feature this pr addresses

there are some punctual cases in which the following error is logged: 

```<samplepartition at h20-0001-p1>.analyses: resolving uidreference failed for ac5c81bed80149108az23bd1ac0d502c.  no object will be returned.```

it is believed that initial transitions of sample (e.g. ```registered```, ```received```) happen during the object creation process by plone. at that moment, objects (```samplepartition```) don't have any analyses assigned yet and this error is logged. however, the error is only logged and the user doesn't expect/see any bad behavior. for this reason, it has been decided that the best choice is to **temporarily use a warning instead of an error**.

## current behavior before pr

an error is logged when resolving an uidreference fails on retrieving analyses from a sample partition.

## desired behavior after pr is merged 

a warning is logged when resolving an uidreference fails on retrieving analyses from a sample partition.

--
i confirm i have tested this pr thoroughly and coded it according to [pep8][1]
and [plone's python styleguide][2] standards.

[1]: https://www.python.org/dev/peps/pep-0008
[2]: https://docs.plone.org/develop/styleguide/python.html


##Repo ID: 22000

##Contributer ID: 84919

##Pull Request ID: 186020

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-2952

previously, only the very last one in the bitstream order would be included.
there is increased potential for character loss with the needed additional string conversions but initial testing has been positive.


##Repo ID: 22104

##Contributer ID: 121873

##Pull Request ID: 245595

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-2187

this pr completely removes all apis, configurations and views (jsps / xmlui aspects) which were associated with lucene. it has been lightly tested both on xmlui and jspui, and everything seems to work, but it could use additional eyes/testers.

this work is based off of initial work from @kshepherd. i borrowed his [ds-2187 branch](https://github.com/kshepherd/dspace/tree/ds-2187) and completed the work by refactoring it against the latest master (i.e. service api) and removing additional classes/configurations.

i've tried to do as thorough a code / configuration removal as i could. however, it's always possible i've overlooked something that is no longer needed (especially i18n messages).

this is ready for others to test/analyze for possible inclusion in 6.0.


##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 245593

###Profanity Found
**Text**
this pr connects to #31 and connects to #29

it adds services to interact with the rest api:  collectiondataservice and itemdataservice

these offer a `findbyid` method, and a `findall` method with an optional `scope` param, for items and collections.

tests and documentation are still lacking. i'd also like to refactor the data services, and their corresponding ngrx objects, because right now there is too much duplication of code. 

i opened this pr already, as these services are needed to start making ui components such as collection homepages and item view pages.
i suggest that people review this pr in its current state, and that we merge it asap so other work can start.
issue #31 will stay open until docs, tests and refactoring are complete.

i also added an initial version of a cacheservice, for the purpose of storing every model in the ngrx store only once. other places in the ngrx store should only store the ids of the models they need.
that way there is a single source of truth for any one model. it also makes the store less deeply nested, and therefore easier to write a reducer without accidentally mutating part of the state.

the services can then use rxjs to combine the ids from their section of the store, with the actual objects from the cache to return an observable for the correct set of objects to the user of the service.

you can find an example [here](https://github.com/artlowel/dspace-angular/blob/rest-services/src/app/core/data-services/collection/collection-data.service.ts#l21).

first, get an observable of the ids for the list of collections from the store:

```typescript
this.store.select<array<string>>('core', 'collectiondata', 'findmultiple', 'collectionuuids')
```

then use those ids to fetch an observable from the cacheservice with the list of collection objects:

``` typescript
this.cache.getlist<collection>(collectionuuids);
```

`flatmap` ensures we return an `observable<collection[]>` instead of an `observable<observable<collection[]>>` - it _flattens_ the observables.


there is a separate issue to expand the cacheservice to do everything we need: #32

##Repo ID: 22117

##Contributer ID: 85848

##Pull Request ID: 218633

###Profanity Found
**Text**
this pull request addresses #1639, and one of two issues involved in a report to the [zotero forum](https://forums.zotero.org/discussion/71243/available-for-beta-testing-zotero-connector-target-selector#latest).

the issue addressed here is a straight-up bug in the translator, in code that i wrote. single-item saves worked fine on the initial visit to a page, but retrieved incorrect metadata after selecting another item from the left-hand toc listing in the page. i apparently didn't manually test that action when i wrote the translator, and it has lurked in there for yonks until a librarian called us on it.

the second issue concerns the site itself, and is identified by @dstillman in the tracker issue and forum thread linked above.

##Repo ID: 22053

##Contributer ID: 85190

##Pull Request ID: 250818

###Profanity Found
**Text**
icons won't appear on the initial screen.

##Repo ID: 25229

##Contributer ID: 81010

##Pull Request ID: 211244

###Profanity Found
**Text**
this is an initial pr for
https://jira.duraspace.org/browse/ds-3095

_note: this pr will not work for java 8 because of [ds-3154](https://jira.duraspace.org/browse/ds-3154)._

this is a major refactor / rework of our parent pom (including fixing all alignment). a few key notes:
- follows sonatype recommendations at http://central.sonatype.org/pages/apache-maven.html
- when using a local maven `settings.xml`, you now need to specify a username/password for a `ossrh` server (which is the recommended name from sonatype). this is different from our current release procedure which shows a sample `settings.xml` using username/password combos for `sonatype-nexus-*` servers. see https://wiki.duraspace.org/display/dspace/release+procedure#releaseprocedure-updatemavensettings.xml
- enhanced comments in this parent pom and fixed alignment of tags (which is why the diff is so large)
- fixed all mailing list links (still pointed at sourceforge lists)
- removed outdated list of contributors / developers. that is managed on our wiki anyways.

overall, this _should_ work for java 7 (untested). however, i'm working on also fixing ds-3154 so that this will work for java 8 as well.


##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 245725

###Profanity Found
**Text**
this pr adds some initial content to the home page: a news section and the list of top level communities

the news is hardcoded for now,  and the top level community list isn't paginated, both of those can be improved later. the goal of this pr is just to make a start.

i moved the message that shows whether the development or production environment is active to the console.

this pr depends on #92 

![screen shot 2017-05-18 at 14 51 07](https://cloud.githubusercontent.com/assets/1567693/26203538/f3eee172-3bdb-11e7-9c79-9be280551c3b.png)



##Repo ID: 22117

##Contributer ID: 85848

##Pull Request ID: 218644

###Profanity Found
**Text**

changes in 2.6.1

 * issue 835 fix increased cpu consumption under heavy load caused by excessive
   spinning in the concurrentbag.requite() method.

 * issue 821 if a disconnection class exception is thrown during initial connection
   setup, do not set the flag that indicates that checkdriversupport() is complete.

 * issue 817 updated behavior of new initializationfailtimeout, please see the
   official documentation for details.

 * issue 742 add direct mxbean accessor methods to hikaridatasource for users who do 
   not want run run jmx.

##Repo ID: 25229

##Contributer ID: 86894

##Pull Request ID: 208929

###Profanity Found
**Text**
condition had been reversed during the initial refactoring due to the service api
https://github.com/dspace/dspace/blob/0292cee4c8a9eee519192b15aff770e291546523/dspace-xmlui/src/main/java/org/dspace/app/xmlui/aspect/discovery/recentsubmissions/recentsubmissiontransformer.java#l182
was the original check (excluding the addition of "handle/_/_*" for a site object)


##Repo ID: 22104

##Contributer ID: 85813

##Pull Request ID: 245767

###Profanity Found
**Text**
this pr will contain all the commits required for the initial integration of senaite/senaite.lims and senaite/bika.lims.  

> this includes:
> 
> important prs against bikalims/bika.lims between the time that it diverged from naralabs/bika.lims.
> commits required to pass relevant tests written in that same time period.
> additional work required to support client implementations using senaite.lims.

- [x] 1917 rockfruit https://github.com/senaite/bika.lims/pull/284
- [x] 1931 espruna https://github.com/senaite/bika.lims/pull/299
- [x] 1932 espurna https://github.com/senaite/bika.lims/pull/298
- [x] 1942 espurna https://github.com/senaite/bika.lims/pull/315
- [x] 1946 nihadness https://github.com/senaite/bika.lims/pull/304
- [x] 1972 nihadness https://github.com/senaite/bika.lims/pull/291
- [x] 1993 espurna https://github.com/senaite/bika.lims/pull/289 the same as 2246
- [x] 2000 rockfruit ``` no pr ```
- [x] 2016 nihadness https://github.com/senaite/bika.lims/pull/294
- [x] 2017 nihadness https://github.com/senaite/bika.lims/pull/304
- [x] 2043 rockfruit ``` no pr ```
- [x] 2053 nihadness https://github.com/senaite/bika.lims/pull/304
- [x] 2073 rockfruit ```no pr```
- [x] 2077 nihadness https://github.com/senaite/bika.lims/pull/306
- [x] 2080 nihadness https://github.com/senaite/bika.lims/pull/304
- [x] 2081 nihadness https://github.com/senaite/bika.lims/pull/304
- [x] 2092 rockfruit https://github.com/senaite/bika.lims/pull/284 [with #1917]
- [x] 2093 espurna https://github.com/senaite/bika.lims/pull/296 + rockfruit https://github.com/senaite/bika.lims/compare/1c547d9...senaite:senaite-integration
- [x] 2102 nihadness https://github.com/senaite/bika.lims/pull/297
- [x] 2112  nihadness https://github.com/senaite/bika.lims/pull/319
- [x] 2125 espurna https://github.com/senaite/bika.lims/pull/292
- [x] 2130 nihadness https://github.com/senaite/bika.lims/pull/309
- [x] 2205 espurna https://github.com/senaite/bika.lims/pull/318
- [x] 2208 juangallostra ```no pr```
- [x] 2210 juangallostra https://github.com/senaite/bika.lims/pull/310 + rockfruit https://github.com/senaite/bika.lims/pull/344
- [x] 2233 nihadness https://github.com/senaite/bika.lims/pull/309
- [x] 2246 espurna https://github.com/senaite/bika.lims/pull/289
- [x] 2252 nihadness https://github.com/senaite/bika.lims/pull/283
- [x] 2266 rockfruit https://github.com/senaite/bika.lims/pull/282
- [x] 2269 juangallostra https://github.com/senaite/bika.lims/pull/281
- [x] 2271 nihadness https://github.com/senaite/bika.lims/pull/280
- [x] 2107 rockfruit https://github.com/senaite/bika.lims/commit/ac6a0213cecd0af1cc39c0454e76cbf15a8d0099
- [x] 2158 xispa https://github.com/senaite/bika.lims/pull/321

new prs from bikalims/bika.lims to be merged:
- [x] 2294 (also pr-2210 from above) rockfruit + xispa + mike https://github.com/senaite/bika.lims/pull/344 https://github.com/senaite/bika.lims/pull/344/commits/101993943c523c086a7da5c3240ad86fd8005ba9
- [ ] 2273 mike https://github.com/senaite/bika.lims/pulls/344 https://github.com/bikalims/bika.lims/commit/2e630cc4f04146def28f52803f71e21c7d201cb7
- [ ] 2295
- [ ] 2297

##Repo ID: 22000

##Contributer ID: 84906

##Pull Request ID: 185901

###Profanity Found
**Text**
the new replacement is more strict but will still work for the
example given in #683.

added more test cases also the initial one together with an
example using the sharp s and one islandic example.

##Repo ID: 22053

##Contributer ID: 80847

##Pull Request ID: 251074

###Profanity Found
**Text**
this is the initial pr for the entities ui functionality.

##Repo ID: 22117

##Contributer ID: 85848

##Pull Request ID: 218753

###Profanity Found
**Text**
this pr depends on #355.
this pr closes #363.

when logged on as an administrator, a user can now edit an item's metadata.

the edit metadata page can be found at `[dspace-url]/items/[item-uuid]/edit/metadata`.

on this page you will be able to add, delete and edit metadata fields. the changes you make will be stored in the ngrx store - even if you don't immediately save them - and will be available as long as you don't refresh the page.

### add
to add a new metadata field, click the large green `+ add` button at the top of the page. a new (green) row will be added to the metadata table which you can edit.

### remove
to remove an existing metadata field, click the red `trash` icon in the last column of the field you would like to remove. the row of the field you removed will turn red.
*you can't edit or remove an already removed field.*

### edit
to edit an existing metadata field, click the blue `edit` icon in the last column of the field you would like to edit. all fields will turn into an input field which you can edit. whenever you make an actual change, the row will turn orange.
*this `edit` button will only be when the field is not in edit mode.*

### close edit mode
to close edit mode and display a field without the input fields, click the green `check` icon.
*this `check` button will only be available when the field is in edit mode.*

### discard changes of a single field
to undo all changes made to a single field, click the orange `undo` icon in the last column of the field to which changes were made. 
an added field will disappear, a removed or editted field will lose its red/orange background color and reset to its initial value.
*note that the `undo` icon will only be enabled when there are changes to undo.*

### discard all changes to all fields
to discard all changes you made, click the orange 'discard' button at the top of the page.
this will immediately remove all current changes.
when clicking the discard button, you will be shown a notification stating that you discarded all changes, but that you can still undo this by clicking the `undo` button at the top of the page.*
when clicking the undo button at the top of the page, all your changes will be reinstated.
when you don't click the `undo`button, your changes will be permanently removed when the notification disappears.

*note that you can only use the `discard` button when you made actual changes to the metadata. 
the `undo` button will only be available when there are changes to undo and the notification is still present.*

### save
to save all the changes you made to the item, click the save button. this will send an actual request to the backend and update the item.
*the `save` button will only be enabled when there are changes to save.*

### `metadatafield` input - help & validation
to make sure you cannot enter invalid data, validation was added to the `metadatafield` input field.
when entering something into this field, a dropdown with metadata fields - that match your input - will be shown from which you can choose.
if the user still enters a non-existing or invalid metadata field, an error message will be shown and you will not be able to save your changes.

### general clean up / refactoring
i got rid of al the occurrences of tnormalized in the dataservices (and the remotedatabuildservice). each tdomain has a single tnormalized, so carrying around both seemed unnecessary. in my opinion this makes the dataservices and remotedatabuildservice easier to understand and maintain.


**) note that ideally we would have liked this `undo` button to be part of the notification, but because of https://github.com/dspace/dspace-angular/issues/357 this is not possible yet.*

##Repo ID: 22117

##Contributer ID: 85926

##Pull Request ID: 218778

###Profanity Found
**Text**
@atmire-kristof discovered a small issue with my previous edit metadata pr #362
when a user discards all changes a notification appears and the discard button turns into an undo button.

however, when clicking - and therefore closing - the notification, the undo button would stay in place and only turn back into a discard button after initial the time-out has finished. this pr solves this issue.

after fixing this specific issue, @artlowel also discovered a caching issue with the metadata fields. when the user would go directly to the edit metadata page, already logged in, the code would not be able to correctly retrieve the list of available metadata fields. when the user subsequently tried to edit the field, every metadata field would be rendered as invalid and the auto complete feature would break. i fixed this by making sure the metadata fields are always interpreted as metadatafield objects. 





##Repo ID: 22117

##Contributer ID: 85926

##Pull Request ID: 218792

###Profanity Found
**Text**
hi @terrywbrady 
here my initial implementation of an endpoint that exposes the known endpoints via the hal browser.
start from
https://github.com/4science/dspace/blob/ds-3513/dspace-spring-rest/src/main/java/org/dspace/app/rest/rootrestresourcecontroller.java

there are several area that needs improvements
https://github.com/4science/dspace/blob/ds-3513/dspace-spring-rest/src/main/java/org/dspace/app/rest/discoverableendpointsservice.java#l81
https://github.com/4science/dspace/blob/ds-3513/dspace-spring-rest/src/main/java/org/dspace/app/rest/discoverableendpointsservice.java#l68
https://github.com/4science/dspace/blob/ds-3513/dspace-spring-rest/src/main/java/org/dspace/app/rest/restresourcecontroller.java#l67

##Repo ID: 22104

##Contributer ID: 79682

##Pull Request ID: 246036

###Profanity Found
**Text**
in the initial entities implementation, a rest feature for filtered-discovery-page has been created.
this was later-on noticed as a feature which is not necessary.
although the functionality is no longer used in angular, we found some remnants 

this pr removes the remainder of this functionality. it is related to https://github.com/dspace/dspace/pull/2499 but not dependent on that branch

##Repo ID: 22117

##Contributer ID: 85808

##Pull Request ID: 260437

###Profanity Found
**Text**
https://github.com/dspace/dspace-angular/issues/256

this initial work on routing by id works with uuid requests.  in separate work i was able to test handle routing using cached objects. however, i think we need a real rest endpoint for handle lookups in the actual implementation.  

i'm currently using the dso endpoint to look up communities, collections and items. wondering if that endpoint is the correct place to add support for handle (and other id type) lookups?

**update: discovered that the pid endpoint is designed for this task.  updated**. 

##Repo ID: 22117

##Contributer ID: 85758

##Pull Request ID: 260446

###Profanity Found
**Text**
in elfinder even if the resources tool was missing from the site the resources tool would be opened when using elfinder as a file picker. this stops that and prevents the resources folder form being displayed even when it’s set as the initial folder.

it was always the case that when browsing an alternative site that if the resources tool wasn’t present you wouldn’t see that folder present in elfinder.

if the resources tool is added, some files added and then removed you will still see the resources folder when browsing the current site.

##Repo ID: 25229

##Contributer ID: 80989

##Pull Request ID: 209260

###Profanity Found
**Text**
just removing the initial check for null, the other changes are just indentation.

##Repo ID: 25229

##Contributer ID: 81010

##Pull Request ID: 211677

###Profanity Found
**Text**
this pr updates the submission ui to use `projection=full` for `post` requests to `/workspaceitems` as an updated workaround to the issue described in detail here: https://github.com/dspace/dspace-angular/issues/581  

the initial workaround was to hardcode this setting into the rest api itself, see https://github.com/dspace/dspace/pull/2682

this pr instead moves that setting to the angular ui client.  

**however, this pr cannot be merged or tested** until the rest api is updated to accept the `projection=full` setting for `post` requests.  currently, the rest api only accepts that param on `get` requests.


##Repo ID: 22117

##Contributer ID: 85035

##Pull Request ID: 260517

###Profanity Found
**Text**
this pr adds pages to:
- create a new process
- get an overview of the processes you have access to
- see the output for a process.

you can start a new process by signing in and selecting new → process from the sidebar.

you can get an overview of available processes by selecting processes from the sidebar, from there you can click on an individual process to see its output.

note that this is an initial version of these uis. there are a lot of improvements we could make and extra features we could add, but we kept the scope as small as possible in order to keep the effort down.

![screenshot 2020-03-30 at 15 06 16](https://user-images.githubusercontent.com/1567693/77919477-8715b480-729d-11ea-8c8b-14114f009ffb.png)
![screenshot 2020-03-30 at 15 05 56](https://user-images.githubusercontent.com/1567693/77919503-8e3cc280-729d-11ea-8b51-4d16ec1c5b7e.png)
![screenshot 2020-03-30 at 15 07 14](https://user-images.githubusercontent.com/1567693/77919526-9432a380-729d-11ea-966e-a24eb9b02281.png)


##Repo ID: 22117

##Contributer ID: 85848

##Pull Request ID: 279023

###Profanity Found
**Text**
`pls` was kind of ignored by the common tests because of this.

i wonder whether `gmm` should have `clustermixin`.

there seem to be a couple of random failing general tests: with `randomizedlogisticregression` (that i shouldn't have touched) and with `pls` (in case of bad luck numerically, i think) but i could only reproduce them with nosetests on the small file, not with `make test`, so i don't have the seeds. 

based on initial work by @amueller.


##Repo ID: 25240

##Contributer ID: 129105

##Pull Request ID: 223635

###Profanity Found
**Text**
when i did our initial archivematica setup, i had a config error that meant mcpserver couldn't see gearman, and it was silently hanging. this patch adds a bit of logging when the gearman server is unavailable, so you have some hope of spotting this error.

it’s based on very similar code that’s already in mcpclient:

https://github.com/artefactual/archivematica/blob/e724372b799909f2604046cdbce4cd6a1283b801/src/mcpclient/lib/archivematicaclient.py#l244-l255

connects to https://github.com/archivematica/issues/issues/553.

##Repo ID: 25208

##Contributer ID: 79391

##Pull Request ID: 179847

###Profanity Found
**Text**
this is an implementation of (non-parametric) t-sne for visualization.

see [laurens van der maaten's paper](http://jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf) or [his website about t-sne](http://homepage.tudelft.nl/19j49/t-sne.html) for details. in comparison to other implementations and the original paper this version has these features:
- it is designed and optimized for python
- the degrees of freedom of the student's t-distribution are determined with a heuristic
- it has only a few parameters to control the optimization: `learning_rate`, `n_iter` and `early_exaggeration`, the momentum etc. are fixed and work well for most datasets
## todo
- [x] implement real `transform` (and maybe even `inverse_transform`)
- [x] integrate in sklearn (relative imports, build with cython, etc.)
- [x] remove python function calls from binary search
- [x] reference for the trustworthiness score
- [x] more parameters for gradient descent (`n_iter`, `learning_rate`, `early_exaggeration`)
- [x] find a robust learning schedule
- [x] refactor t-sne so that it is possible for the user to implement parametric t-sne
- [x] distances should be called affinities
- [x] tests
- [x] example (documentation, comparisons)
- [x] t-sne should expose the attributes `embedding_`, `nbrs_`, `training_data_`, `embedding_nbrs_` (similar to `isomap`)
- [x] remove generalization
- [x] narrative documentation in `doc/modules/manifold.rst`
- [x] integrate pca initialization (merge + docstring)
- [x] mention papers about barnes-hut-sne etc. in comment in `t_sne.py`
## learning schedules

in the literature:
- original paper: initialization with standard deviation 1e-4, 1000 episodes, learning rate 100, momentum 0.5 for 250 episodes, 0.8 for the rest, early exaggeration with 4 for 50 episodes
- matlab implementation: learning rate 500, early exaggeration for 100 episodes
- python implementation: initialization with standard deviation 1, learning rate 500, early exaggeration for 100 episodes, momentum 0.5 for 20 episodes
- [divvy](https://github.com/jmlewis/divvy/blob/master/plugins/reducers/tsne/tsne.c): initialization with standard deviation 1e-4, 1000 episodes, learning rate 1000, momentum 0.5 for 100 episodes, 0.8 for the rest, early exaggeration with 4 for 100 episodes
- parametric t-sne (not comparable): conjugate gradient
- barnes-hut t-sne: initialization with standard deviation 1e-4, 1000 episodes, learning rate 200, momentum 0.5 for 250 episodes, 0.8 for the rest, early exaggeration with 12 for 250 episodes

my experiences:
- the learning rate has to be set manually for optimal performance, something between 100 and 1000
- a high momentum (0.8) during early exaggeration improves the result

this implementation uses the following schedule:
- initialization with standard deviation 1e-4, 1000 episodes, learning rate 1000, momentum 0.5 for 50 episodes, 0.8 for the rest, early exaggeration with 4 for 100 episodes
## observations
- early compression (l2 penalty at the beginning of the optimization) did not give significant advantage in my experiments
- l-bfgs is faster for smaller datasets and creates larger gaps between natural clusters than gradient descent in larger datasets
- usually visualizations look better with gradient descent even though l-bfgs finds better local minima
- binary search requires 2.3 seconds in cython and 3.9 seconds in python on the digits dataset
## tips
- reducing the dimensionality of data to its first 50 principal components often results in better t-sne visualizations
- if the cost function increases during initial optimization, the early exaggeration factor or the learning rate might be too high
- if the cost function gets stuck in a bad local minimum increasing the learning rate helps sometimes
## examples

visualizations of some datasets can be found [here](http://www.informatik.uni-bremen.de/~afabisch/files/tsne/), e.g.

![digits dataset](http://www.informatik.uni-bremen.de/~afabisch/files/tsne/tsne_digits.png)
## work for other pull requests
- [barnes-hut-sne](http://arxiv.org/abs/1301.3342)
- [fast optimization for t-sne](http://cseweb.ucsd.edu/~lvdmaaten/workshops/nips2010/papers/vandermaaten.pdf)


##Repo ID: 25240

##Contributer ID: 170603

##Pull Request ID: 224589

###Profanity Found
**Text**
like #1367, this pr is designed to resolve a prerequisite for [vufind-1309](https://vufind.org/jira/browse/vufind-1309), though this is also a useful feature in its own right. see also #1354 for some earlier discussion about this feature.

todo
- [x] get initial implementation working
- [x] add support for appropriate interaction with email verification functionality
- [x] confirm csrf protection is appropriately applied
- [x] confirm captcha support is fully functional
- [x] add flag to differentiate between user-specified change and upstream change; do not overwrite user-specified changes.
- [x] review how to handle email propagation to auth handler (and whether to block email change when auth handler does not support updates).
- [x] test notification to old email address of changes.
- [x] test with postgresql
- [x] write mink test to cover new form
- [x] update changelog (including database changelog)
- [x] run full test suite

##Repo ID: 25234

##Contributer ID: 181246

##Pull Request ID: 249485

###Profanity Found
**Text**
this initial pr is to allow discussion concerning the implementation of `options("repos")` into `biocmanager` code.


##Repo ID: 25266

##Contributer ID: 86564

##Pull Request ID: 279814

###Profanity Found
**Text**
this is an initial attempt at adding support for ils-based paging in the checkouts list. the motivation is to provide usable performance in cases where the user has hundreds or thousands of loans (institutional users etc.). unfortunately not supported by many backends yet, but included is support in the following drivers: demo, voyager, sierrarest (no sorting choices for sierrarest though). paging can be enabled in the ini file.

there's one downside: since we don't know get all the id's, "renew all" button cannot be displayed.

todo
- [x] document ils driver spec changes
- [x] investigate whether we can better validate the page parameter to avoid displaying blank results

##Repo ID: 25234

##Contributer ID: 178201

##Pull Request ID: 249352

###Profanity Found
**Text**
this is needed to correctly compare the alphabrowse initial letter and url param so as to set the active class on the pagination list. the identical comparison fails to deal with numerical values in the param. 

##Repo ID: 25234

##Contributer ID: 81324

##Pull Request ID: 249204

###Profanity Found
**Text**
okay, here goes.

based of aurimas's initial work from a year ago, rebased on current master, imposed upon new data-layer changes, with a bunch of tests added (and bugs hunted down in the process).

~~translation is not supported yet and will be submitted as a separate pr.~~
translation added on the same branch.

~~note:
expiration logic is now as follows: the feed items are removed from the feed after x days (specified in feed options) from marking them as _read_. i am not sure if this is the most intuitive behaviour.~~
expired items are only removed if they are no longer provided on the rss feed too. this prevents having empty feeds for those that update infrequently


##Repo ID: 22063

##Contributer ID: 95348

##Pull Request ID: 251233

###Profanity Found
**Text**
closes #160 

still todo:
- add how to do the bootstrap job
- fix the link in initial deploy page

##Repo ID: 25491

##Contributer ID: 79647

##Pull Request ID: 279961

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-4316

this adds two new ways (in addition to the existing item uuid) to refer to other items when adding relationships via csv import:

a) by row name. if a previous row in the same csv declares a name (via an optional `rowname` column), you may refer to it by whatever name it has been given in the csv, by specifying `rowname:name` in the relationship.label column (where name is the actual unique row name of the row you're referring to). the row name may be any unique string. it is not persisted as metadata; the name is just a convenience used during import.

b) by unique metadata value. if a previous row in the same csv, or an item already in the repository, has a unique value for a given metadata field, you may refer to that item by specifying `field:value` in the relationship.label column. this allows, for example, referring to another item by doi (dc.identifier.doi:some_doi) or another application-specific identifier you know to be unique.

the csv import will fail with an appropriate error message if:

* any reference doesn't refer to an existing row or item
* any reference resolves to multiple items

note:

the metadataimport script has historically behaved slightly differently depending on whether you pass in -s ("silent") or not. in the former case, it does not run the initial pass through the csv (the validation/verification part). since it is important to test the first pass-through, we have added a -v ("validate") option to the cli, that only runs the initial validation. this is used by a limited set of the tests to ensure failure cases behave properly.

tbd: documentation needs to be added for this capability (cli usage and metadataimport docs in general require updates)

##Repo ID: 22104

##Contributer ID: 85757

##Pull Request ID: 246829

###Profanity Found
**Text**
this change will clear the dc.date.issued item metadata field when published is selected during the initial questions submission step. 

jira ticket: https://jira.duraspace.org/browse/ds-4328

##Repo ID: 22104

##Contributer ID: 85812

##Pull Request ID: 246851

###Profanity Found
**Text**
this change will clear the dc.date.issued item metadata field when published is selected during the initial questions submission step.

jira ticket: https://jira.duraspace.org/browse/ds-4328

##Repo ID: 22104

##Contributer ID: 85812

##Pull Request ID: 246852

###Profanity Found
**Text**
## overview

demonstrates how a nestjs singleton service can serve as a cache for data from s3.

the controller endpoint is ultimately likely to be unnecessary, but i added it to demonstrate how to use the topologyservice


### demo

![image](https://user-images.githubusercontent.com/4432106/74751148-d8f90280-523a-11ea-8993-7f56d54793bf.png)


### notes

this conflicts with changes in @rbreslow's pr. i'm planning to wait until his is merged to address those conflicts.

## testing instructions

- `scripts/setup`
- you should be able to download topojson from http://localhost:3005/districts/topology/pa
- after the initial access, the above endpoint should continue to function even after disconnecting your computer's internet connection, because the value is cached.


closes #25



##Repo ID: 25236

##Contributer ID: 178207

##Pull Request ID: 279994

###Profanity Found
**Text**
this pr contains the following updates:

| package | type | update | change |
|---|---|---|---|
| [node](https://togithub.com/nodejs/node) | final | patch | `12.18.2-alpine` -> `12.18.3-alpine` |

---

### release notes

<details>
<summary>nodejs/node</summary>

### [`v12.18.3`](https://togithub.com/nodejs/node/releases/v12.18.3)

[compare source](https://togithub.com/nodejs/node/compare/v12.18.2...v12.18.3)

##### notable changes

-   **deps:**
    -   upgrade npm to 6.14.6 (claudiahdz) [#&#8203;34246](https://togithub.com/nodejs/node/pull/34246)
    -   update node-inspect to v2.0.0 (jan krems) [#&#8203;33447](https://togithub.com/nodejs/node/pull/33447)
    -   uvwasi: cherry-pick [`9e75217`](https://togithub.com/nodejs/node/commit/9e75217) (colin ihrig) [#&#8203;33521](https://togithub.com/nodejs/node/pull/33521)

##### commits

-   \[[`0d79c533ef`](https://togithub.com/nodejs/node/commit/0d79c533ef)] - **async_hooks**: callback trampoline for makecallback (stephen belanger) [#&#8203;33801](https://togithub.com/nodejs/node/pull/33801)
-   \[[`bfffb977ad`](https://togithub.com/nodejs/node/commit/bfffb977ad)] - **benchmark**: fix async-resource benchmark (anna henningsen) [#&#8203;33642](https://togithub.com/nodejs/node/pull/33642)
-   \[[`09277fa5e4`](https://togithub.com/nodejs/node/commit/09277fa5e4)] - **benchmark**: fixing http_server_for_chunky_client.js (adrian estrada) [#&#8203;33271](https://togithub.com/nodejs/node/pull/33271)
-   \[[`5a6d80f25f`](https://togithub.com/nodejs/node/commit/5a6d80f25f)] - **buffer**: remove hoisted variable (nikolai vavilov) [#&#8203;33470](https://togithub.com/nodejs/node/pull/33470)
-   \[[`e057189ee8`](https://togithub.com/nodejs/node/commit/e057189ee8)] - **build**: configure byte order for mips targets (ben noordhuis) [#&#8203;33898](https://togithub.com/nodejs/node/pull/33898)
-   \[[`d77eaeefb8`](https://togithub.com/nodejs/node/commit/d77eaeefb8)] - **build**: add target specific build_type variable (daniel bevenius) [#&#8203;33925](https://togithub.com/nodejs/node/pull/33925)
-   \[[`d56585ec8d`](https://togithub.com/nodejs/node/commit/d56585ec8d)] - **build**: add lint_cpp_files to checkimports check (daniel bevenius) [#&#8203;33697](https://togithub.com/nodejs/node/pull/33697)
-   \[[`a5ce90c46b`](https://togithub.com/nodejs/node/commit/a5ce90c46b)] - **build**: add --v8-lite-mode flag (maciej kacper jagiełło) [#&#8203;33541](https://togithub.com/nodejs/node/pull/33541)
-   \[[`11dad02e50`](https://togithub.com/nodejs/node/commit/11dad02e50)] - **build**: fix python-version selection with actions (richard lau) [#&#8203;33589](https://togithub.com/nodejs/node/pull/33589)
-   \[[`bba41bf6e1`](https://togithub.com/nodejs/node/commit/bba41bf6e1)] - **build**: fix makefile script on windows (thomas) [#&#8203;33136](https://togithub.com/nodejs/node/pull/33136)
-   \[[`817f6593ee`](https://togithub.com/nodejs/node/commit/817f6593ee)] - **configure**: account for clang_vendor when checking for llvm version (nathan blair) [#&#8203;33860](https://togithub.com/nodejs/node/pull/33860)
-   \[[`a9c5b3348c`](https://togithub.com/nodejs/node/commit/a9c5b3348c)] - **console**: name console functions appropriately (ruben bridgewater) [#&#8203;33524](https://togithub.com/nodejs/node/pull/33524)
-   \[[`d8365bc71e`](https://togithub.com/nodejs/node/commit/d8365bc71e)] - **console**: mark special console properties as non-enumerable (ruben bridgewater) [#&#8203;33524](https://togithub.com/nodejs/node/pull/33524)
-   \[[`80782cb261`](https://togithub.com/nodejs/node/commit/80782cb261)] - **console**: remove dead code (ruben bridgewater) [#&#8203;33524](https://togithub.com/nodejs/node/pull/33524)
-   \[[`18dc03d6a5`](https://togithub.com/nodejs/node/commit/18dc03d6a5)] - **crypto**: fix wrong error message (ben bucksch) [#&#8203;33482](https://togithub.com/nodejs/node/pull/33482)
-   \[[`b64963e5c3`](https://togithub.com/nodejs/node/commit/b64963e5c3)] - **deps**: upgrade npm to 6.14.6 (claudiahdz) [#&#8203;34246](https://togithub.com/nodejs/node/pull/34246)
-   \[[`9ee9688fe0`](https://togithub.com/nodejs/node/commit/9ee9688fe0)] - **deps**: uvwasi: cherry-pick [`9e75217`](https://togithub.com/nodejs/node/commit/9e75217) (colin ihrig) [#&#8203;33521](https://togithub.com/nodejs/node/pull/33521)
-   \[[`8803d7e8cf`](https://togithub.com/nodejs/node/commit/8803d7e8cf)] - **deps**: update node-inspect to v2.0.0 (jan krems) [#&#8203;33447](https://togithub.com/nodejs/node/pull/33447)
-   \[[`5d3f818e9e`](https://togithub.com/nodejs/node/commit/5d3f818e9e)] - **dns**: make dns.resolver timeout configurable (ben noordhuis) [#&#8203;33472](https://togithub.com/nodejs/node/pull/33472)
-   \[[`10b88cb117`](https://togithub.com/nodejs/node/commit/10b88cb117)] - **dns**: use ternary operator simplify statement (wenning zhang) [#&#8203;33234](https://togithub.com/nodejs/node/pull/33234)
-   \[[`fbd6fe5839`](https://togithub.com/nodejs/node/commit/fbd6fe5839)] - **doc**: update code language flag for internal doc (rich trott) [#&#8203;33852](https://togithub.com/nodejs/node/pull/33852)
-   \[[`24fd15778a`](https://togithub.com/nodejs/node/commit/24fd15778a)] - **doc**: specify maxheadercount alias for maxheaderlistpairs (pranshu srivastava) [#&#8203;33519](https://togithub.com/nodejs/node/pull/33519)
-   \[[`04ceeaf5eb`](https://togithub.com/nodejs/node/commit/04ceeaf5eb)] - **doc**: add allowed info strings to style guide (derek lewis) [#&#8203;34024](https://togithub.com/nodejs/node/pull/34024)
-   \[[`ee36c87fd7`](https://togithub.com/nodejs/node/commit/ee36c87fd7)] - **doc**: clarify thread-safe function references (legendecas) [#&#8203;33871](https://togithub.com/nodejs/node/pull/33871)
-   \[[`30b5e76ffd`](https://togithub.com/nodejs/node/commit/30b5e76ffd)] - **doc**: use npm team for npm upgrades in collaborator guide (rich trott) [#&#8203;33999](https://togithub.com/nodejs/node/pull/33999)
-   \[[`06937249d0`](https://togithub.com/nodejs/node/commit/06937249d0)] - **doc**: correct default values in http2 docs (rich trott) [#&#8203;33997](https://togithub.com/nodejs/node/pull/33997)
-   \[[`498dfba33a`](https://togithub.com/nodejs/node/commit/498dfba33a)] - **doc**: use a single space between sentences (rich trott) [#&#8203;33995](https://togithub.com/nodejs/node/pull/33995)
-   \[[`47ea3067d0`](https://togithub.com/nodejs/node/commit/47ea3067d0)] - **doc**: revise text in dns module documentation introduction (rich trott) [#&#8203;33986](https://togithub.com/nodejs/node/pull/33986)
-   \[[`f29f77f111`](https://togithub.com/nodejs/node/commit/f29f77f111)] - **doc**: update fs.md (shakil-shahadat) [#&#8203;33820](https://togithub.com/nodejs/node/pull/33820)
-   \[[`ddc5afdddc`](https://togithub.com/nodejs/node/commit/ddc5afdddc)] - **doc**: warn that tls.connect() doesn't set sni (alba mendez) [#&#8203;33855](https://togithub.com/nodejs/node/pull/33855)
-   \[[`732b80b474`](https://togithub.com/nodejs/node/commit/732b80b474)] - **doc**: fix lexical sorting of bottom-references in dns doc (rich trott) [#&#8203;33987](https://togithub.com/nodejs/node/pull/33987)
-   \[[`6af2ed3fdc`](https://togithub.com/nodejs/node/commit/6af2ed3fdc)] - **doc**: change "github repo" to "code repository" (rich trott) [#&#8203;33985](https://togithub.com/nodejs/node/pull/33985)
-   \[[`322a51e582`](https://togithub.com/nodejs/node/commit/322a51e582)] - **doc**: use class: consistently (rich trott) [#&#8203;33978](https://togithub.com/nodejs/node/pull/33978)
-   \[[`410b23398d`](https://togithub.com/nodejs/node/commit/410b23398d)] - **doc**: update wasm code sample (pragyan das) [#&#8203;33626](https://togithub.com/nodejs/node/pull/33626)
-   \[[`335f405f1b`](https://togithub.com/nodejs/node/commit/335f405f1b)] - **doc**: link readable.\_read in stream.md (pranshu srivastava) [#&#8203;33767](https://togithub.com/nodejs/node/pull/33767)
-   \[[`3789c28c89`](https://togithub.com/nodejs/node/commit/3789c28c89)] - **doc**: specify default encoding in writable.write (pranshu srivastava) [#&#8203;33765](https://togithub.com/nodejs/node/pull/33765)
-   \[[`5609b17e2d`](https://togithub.com/nodejs/node/commit/5609b17e2d)] - **doc**: move --force-context-aware option in cli.md (daniel bevenius) [#&#8203;33823](https://togithub.com/nodejs/node/pull/33823)
-   \[[`f39ee7d245`](https://togithub.com/nodejs/node/commit/f39ee7d245)] - **doc**: add snippet for asyncresource and ee integration (andrey pechkurov) [#&#8203;33751](https://togithub.com/nodejs/node/pull/33751)
-   \[[`f8baeccaaa`](https://togithub.com/nodejs/node/commit/f8baeccaaa)] - **doc**: use single quotes in --tls-cipher-list (daniel bevenius) [#&#8203;33709](https://togithub.com/nodejs/node/pull/33709)
-   \[[`4654e2321b`](https://togithub.com/nodejs/node/commit/4654e2321b)] - **doc**: fix misc. mislabeled code block info strings (derek lewis) [#&#8203;33548](https://togithub.com/nodejs/node/pull/33548)
-   \[[`046dee6eb3`](https://togithub.com/nodejs/node/commit/046dee6eb3)] - **doc**: update v8 inspector example (colin ihrig) [#&#8203;33758](https://togithub.com/nodejs/node/pull/33758)
-   \[[`d547d1c1bc`](https://togithub.com/nodejs/node/commit/d547d1c1bc)] - **doc**: fix linting in doc-style-guide.md (pranshu srivastava) [#&#8203;33787](https://togithub.com/nodejs/node/pull/33787)
-   \[[`3b437416d5`](https://togithub.com/nodejs/node/commit/3b437416d5)] - **doc**: add formatting for version numbers to doc-style-guide.md (rich trott) [#&#8203;33755](https://togithub.com/nodejs/node/pull/33755)
-   \[[`b00996ce35`](https://togithub.com/nodejs/node/commit/b00996ce35)] - **doc**: remove "currently" from repl.md (rich trott) [#&#8203;33756](https://togithub.com/nodejs/node/pull/33756)
-   \[[`7595d15286`](https://togithub.com/nodejs/node/commit/7595d15286)] - **doc**: remove "currently" from vm.md (rich trott) [#&#8203;33756](https://togithub.com/nodejs/node/pull/33756)
-   \[[`36a8af7a5e`](https://togithub.com/nodejs/node/commit/36a8af7a5e)] - **doc**: remove "currently" from addons.md (rich trott) [#&#8203;33756](https://togithub.com/nodejs/node/pull/33756)
-   \[[`27e797687f`](https://togithub.com/nodejs/node/commit/27e797687f)] - **doc**: remove "currently" from util.md (rich trott) [#&#8203;33756](https://togithub.com/nodejs/node/pull/33756)
-   \[[`94ac13678d`](https://togithub.com/nodejs/node/commit/94ac13678d)] - **doc**: change "pre node.js v0.10" to "prior to node.js 0.10" (rich trott) [#&#8203;33754](https://togithub.com/nodejs/node/pull/33754)
-   \[[`f1a810880e`](https://togithub.com/nodejs/node/commit/f1a810880e)] - **doc**: normalize c++ code block info strings (derek lewis) [#&#8203;33483](https://togithub.com/nodejs/node/pull/33483)
-   \[[`289d0bf105`](https://togithub.com/nodejs/node/commit/289d0bf105)] - **doc**: remove default parameter value from header (rich trott) [#&#8203;33752](https://togithub.com/nodejs/node/pull/33752)
-   \[[`35cee03849`](https://togithub.com/nodejs/node/commit/35cee03849)] - **doc**: remove shell dollar signs without output (nick schonning) [#&#8203;33692](https://togithub.com/nodejs/node/pull/33692)
-   \[[`d10fac73a3`](https://togithub.com/nodejs/node/commit/d10fac73a3)] - **doc**: add lint disabling comment for collaborator list (rich trott) [#&#8203;33719](https://togithub.com/nodejs/node/pull/33719)
-   \[[`8dbf3349d0`](https://togithub.com/nodejs/node/commit/8dbf3349d0)] - **doc**: fix urls to avoid redirection (sapics) [#&#8203;33614](https://togithub.com/nodejs/node/pull/33614)
-   \[[`5416635677`](https://togithub.com/nodejs/node/commit/5416635677)] - **doc**: improve buffer.md a tiny bit (tom nagle) [#&#8203;33547](https://togithub.com/nodejs/node/pull/33547)
-   \[[`a3b6095db1`](https://togithub.com/nodejs/node/commit/a3b6095db1)] - **doc**: normalize markdown code block info strings (derek lewis) [#&#8203;33542](https://togithub.com/nodejs/node/pull/33542)
-   \[[`4fcbfdc45c`](https://togithub.com/nodejs/node/commit/4fcbfdc45c)] - **doc**: normalize javascript code block info strings (derek lewis) [#&#8203;33531](https://togithub.com/nodejs/node/pull/33531)
-   \[[`543605782d`](https://togithub.com/nodejs/node/commit/543605782d)] - **doc**: outline when origin is set to unhandledrejection (ruben bridgewater) [#&#8203;33530](https://togithub.com/nodejs/node/pull/33530)
-   \[[`7dc28ab4d3`](https://togithub.com/nodejs/node/commit/7dc28ab4d3)] - **doc**: update txt fandamental and raw code blocks (zeke sikelianos) [#&#8203;33028](https://togithub.com/nodejs/node/pull/33028)
-   \[[`cf82adf87f`](https://togithub.com/nodejs/node/commit/cf82adf87f)] - **doc**: normalize bash code block info strings (derek lewis) [#&#8203;33510](https://togithub.com/nodejs/node/pull/33510)
-   \[[`7ea6b07b90`](https://togithub.com/nodejs/node/commit/7ea6b07b90)] - **doc**: normalize shell code block info strings (derek lewis) [#&#8203;33486](https://togithub.com/nodejs/node/pull/33486)
-   \[[`74a1493441`](https://togithub.com/nodejs/node/commit/74a1493441)] - **doc**: normalize c code block info strings (derek lewis) [#&#8203;33507](https://togithub.com/nodejs/node/pull/33507)
-   \[[`281d7f74d8`](https://togithub.com/nodejs/node/commit/281d7f74d8)] - **doc**: correct tls.rootcertificates to match implementation (eric bickle) [#&#8203;33313](https://togithub.com/nodejs/node/pull/33313)
-   \[[`6133639d53`](https://togithub.com/nodejs/node/commit/6133639d53)] - **doc**: fix buffer.from(object) documentation (nikolai vavilov) [#&#8203;33327](https://togithub.com/nodejs/node/pull/33327)
-   \[[`b599037f78`](https://togithub.com/nodejs/node/commit/b599037f78)] - **doc**: fix typo in pathtofileurl example (antoine du hamel) [#&#8203;33418](https://togithub.com/nodejs/node/pull/33418)
-   \[[`78734c2698`](https://togithub.com/nodejs/node/commit/78734c2698)] - **doc**: eliminate dead space in api section's sidebar (john gardner) [#&#8203;33469](https://togithub.com/nodejs/node/pull/33469)
-   \[[`c76ec4d007`](https://togithub.com/nodejs/node/commit/c76ec4d007)] - **doc**: fixed a grammatical error in path.md (deep310) [#&#8203;33489](https://togithub.com/nodejs/node/pull/33489)
-   \[[`1b76377bce`](https://togithub.com/nodejs/node/commit/1b76377bce)] - **doc**: correct commonjs self-resolve spec (guy bedford) [#&#8203;33391](https://togithub.com/nodejs/node/pull/33391)
-   \[[`70d025f510`](https://togithub.com/nodejs/node/commit/70d025f510)] - **doc**: standardize on sentence case for headers (rich trott) [#&#8203;33889](https://togithub.com/nodejs/node/pull/33889)
-   \[[`3e68d21c6f`](https://togithub.com/nodejs/node/commit/3e68d21c6f)] - **doc**: use sentence-case for headings in docs (rich trott) [#&#8203;33889](https://togithub.com/nodejs/node/pull/33889)
-   \[[`dfa8028254`](https://togithub.com/nodejs/node/commit/dfa8028254)] - **doc**: fix readline key binding documentation (ruben bridgewater) [#&#8203;33361](https://togithub.com/nodejs/node/pull/33361)
-   \[[`6f8b7a85d2`](https://togithub.com/nodejs/node/commit/6f8b7a85d2)] - **doc,tools**: properly syntax highlight api ref docs (derek lewis) [#&#8203;33442](https://togithub.com/nodejs/node/pull/33442)
-   \[[`43d1d89d27`](https://togithub.com/nodejs/node/commit/43d1d89d27)] - **domain**: fix unintentional deprecation warning (anna henningsen) [#&#8203;34245](https://togithub.com/nodejs/node/pull/34245)
-   \[[`ba476326dd`](https://togithub.com/nodejs/node/commit/ba476326dd)] - **domain**: remove native domain code (stephen belanger) [#&#8203;33801](https://togithub.com/nodejs/node/pull/33801)
-   \[[`76b06e53c6`](https://togithub.com/nodejs/node/commit/76b06e53c6)] - **errors**: fully inspect errors on exit (ruben bridgewater) [#&#8203;33523](https://togithub.com/nodejs/node/pull/33523)
-   \[[`9111fab663`](https://togithub.com/nodejs/node/commit/9111fab663)] - **esm**: fix loader hooks doc annotations (derek lewis) [#&#8203;33563](https://togithub.com/nodejs/node/pull/33563)
-   \[[`3559471153`](https://togithub.com/nodejs/node/commit/3559471153)] - **esm**: share package.json cache between esm and cjs loaders (kirill shatskiy) [#&#8203;33229](https://togithub.com/nodejs/node/pull/33229)
-   \[[`d09f6d55c7`](https://togithub.com/nodejs/node/commit/d09f6d55c7)] - **esm**: doc & validate source values for formats (bradley farias) [#&#8203;32202](https://togithub.com/nodejs/node/pull/32202)
-   \[[`a76fa60c63`](https://togithub.com/nodejs/node/commit/a76fa60c63)] - **fs**: fix readdir failure when libuv returns uv_dirent_unknown (kirill shatskiy) [#&#8203;33395](https://togithub.com/nodejs/node/pull/33395)
-   \[[`b92c0cb15c`](https://togithub.com/nodejs/node/commit/b92c0cb15c)] - **fs**: fix realpath inode link caching (denys otrishko) [#&#8203;33945](https://togithub.com/nodejs/node/pull/33945)
-   \[[`04fa6d675f`](https://togithub.com/nodejs/node/commit/04fa6d675f)] - **fs**: close file descriptor of promisified truncate (joão reis) [#&#8203;34239](https://togithub.com/nodejs/node/pull/34239)
-   \[[`c9cf41d841`](https://togithub.com/nodejs/node/commit/c9cf41d841)] - **fs**: support util.promisify for fs.readv (lucas holmquist) [#&#8203;33590](https://togithub.com/nodejs/node/pull/33590)
-   \[[`adb93f153b`](https://togithub.com/nodejs/node/commit/adb93f153b)] - **fs**: unify style in preprocesssymlinkdestination (bartosz sosnowski) [#&#8203;33496](https://togithub.com/nodejs/node/pull/33496)
-   \[[`5fb1cc8cc1`](https://togithub.com/nodejs/node/commit/5fb1cc8cc1)] - **fs**: replace checkposition with validateinteger (rickyes) [#&#8203;33277](https://togithub.com/nodejs/node/pull/33277)
-   \[[`75107e23a8`](https://togithub.com/nodejs/node/commit/75107e23a8)] - **http2**: always call callback on http2serverresponse#end (pranshu srivastava) [#&#8203;33911](https://togithub.com/nodejs/node/pull/33911)
-   \[[`0f0720a665`](https://togithub.com/nodejs/node/commit/0f0720a665)] - **http2**: add writable\* properties to compat api (pranshu srivastava) [#&#8203;33506](https://togithub.com/nodejs/node/pull/33506)
-   \[[`8def93429e`](https://togithub.com/nodejs/node/commit/8def93429e)] - **http2**: add type checks for http2serverresponse.end (pranshu srivastava) [#&#8203;33146](https://togithub.com/nodejs/node/pull/33146)
-   \[[`a3b7e5992d`](https://togithub.com/nodejs/node/commit/a3b7e5992d)] - **http2**: use `object.create(null)` for `getheaders` (pranshu srivastava) [#&#8203;33188](https://togithub.com/nodejs/node/pull/33188)
-   \[[`bcdf4c808d`](https://togithub.com/nodejs/node/commit/bcdf4c808d)] - **http2**: reuse .\_ontimeout() in http2session and http2stream classes (rickyes) [#&#8203;33354](https://togithub.com/nodejs/node/pull/33354)
-   \[[`103a9af673`](https://togithub.com/nodejs/node/commit/103a9af673)] - **inspector**: drop 'chrome-' from inspector url (colin ihrig) [#&#8203;33758](https://togithub.com/nodejs/node/pull/33758)
-   \[[`0941635bb5`](https://togithub.com/nodejs/node/commit/0941635bb5)] - **inspector**: throw error when activating an already active inspector (joyee cheung) [#&#8203;33015](https://togithub.com/nodejs/node/pull/33015)
-   \[[`0197ea4e56`](https://togithub.com/nodejs/node/commit/0197ea4e56)] - **lib**: replace charcodeat with fixed unicode (rickyes) [#&#8203;32758](https://togithub.com/nodejs/node/pull/32758)
-   \[[`69291e4b7d`](https://togithub.com/nodejs/node/commit/69291e4b7d)] - **lib**: add int16array primordials (sebastien ahkrin) [#&#8203;31205](https://togithub.com/nodejs/node/pull/31205)
-   \[[`83c9364bf1`](https://togithub.com/nodejs/node/commit/83c9364bf1)] - **lib**: update todo comments (ruben bridgewater) [#&#8203;33361](https://togithub.com/nodejs/node/pull/33361)
-   \[[`a94e7dabcc`](https://togithub.com/nodejs/node/commit/a94e7dabcc)] - **lib**: update executionasyncid/triggerasyncid comment (daniel bevenius) [#&#8203;33396](https://togithub.com/nodejs/node/pull/33396)
-   \[[`857ff68485`](https://togithub.com/nodejs/node/commit/857ff68485)] - **meta**: introduce codeowners again (james m snell) [#&#8203;33895](https://togithub.com/nodejs/node/pull/33895)
-   \[[`f534ac06bd`](https://togithub.com/nodejs/node/commit/f534ac06bd)] - **meta**: fix a typo in the flaky test template (colin ihrig) [#&#8203;33677](https://togithub.com/nodejs/node/pull/33677)
-   \[[`1376c3bab2`](https://togithub.com/nodejs/node/commit/1376c3bab2)] - **meta**: wrap flaky test template at 80 characters (colin ihrig) [#&#8203;33677](https://togithub.com/nodejs/node/pull/33677)
-   \[[`b7ea7be2a8`](https://togithub.com/nodejs/node/commit/b7ea7be2a8)] - **meta**: add flaky test issue template (ash cripps) [#&#8203;33500](https://togithub.com/nodejs/node/pull/33500)
-   \[[`0867ab7da5`](https://togithub.com/nodejs/node/commit/0867ab7da5)] - **module**: fix error message about importing names from cjs (fábio santos) [#&#8203;33882](https://togithub.com/nodejs/node/pull/33882)
-   \[[`47f5eeb0d5`](https://togithub.com/nodejs/node/commit/47f5eeb0d5)] - **n-api**: add version to wasm registration (gus caplan) [#&#8203;34045](https://togithub.com/nodejs/node/pull/34045)
-   \[[`2e97d82509`](https://togithub.com/nodejs/node/commit/2e97d82509)] - **n-api**: document nexttick timing in callbacks (mathias buus) [#&#8203;33804](https://togithub.com/nodejs/node/pull/33804)
-   \[[`90ddf0aa2e`](https://togithub.com/nodejs/node/commit/90ddf0aa2e)] - **n-api**: ensure scope present for finalization (michael dawson) [#&#8203;33508](https://togithub.com/nodejs/node/pull/33508)
-   \[[`ed741ecb1e`](https://togithub.com/nodejs/node/commit/ed741ecb1e)] - **n-api**: remove `napi_env::callintomodulethrow` (gabriel schulhof) [#&#8203;33570](https://togithub.com/nodejs/node/pull/33570)
-   \[[`0a949c3f93`](https://togithub.com/nodejs/node/commit/0a949c3f93)] - **napi**: add \_\_wasm32\_\_ guards (gus caplan) [#&#8203;33597](https://togithub.com/nodejs/node/pull/33597)
-   \[[`7c7f5c8869`](https://togithub.com/nodejs/node/commit/7c7f5c8869)] - **net**: refactor check for windows (rickyes) [#&#8203;33497](https://togithub.com/nodejs/node/pull/33497)
-   \[[`578e731321`](https://togithub.com/nodejs/node/commit/578e731321)] - **querystring**: fix stringify for empty array (sapics) [#&#8203;33918](https://togithub.com/nodejs/node/pull/33918)
-   \[[`13b693fd54`](https://togithub.com/nodejs/node/commit/13b693fd54)] - **querystring**: improve stringify() performance (brian white) [#&#8203;33669](https://togithub.com/nodejs/node/pull/33669)
-   \[[`d3737a1c32`](https://togithub.com/nodejs/node/commit/d3737a1c32)] - **src**: add errorproperties on process.report (himself65) [#&#8203;28426](https://togithub.com/nodejs/node/pull/28426)
-   \[[`b57778ff26`](https://togithub.com/nodejs/node/commit/b57778ff26)] - **src**: tolerate eperm returned from tcsetattr (patr0nus) [#&#8203;33944](https://togithub.com/nodejs/node/pull/33944)
-   \[[`9e1185afee`](https://togithub.com/nodejs/node/commit/9e1185afee)] - **src**: clang_format base_object (yash ladha) [#&#8203;33680](https://togithub.com/nodejs/node/pull/33680)
-   \[[`69f962953c`](https://togithub.com/nodejs/node/commit/69f962953c)] - **src**: remove unnecessary calculation in base64.h (sapics) [#&#8203;33839](https://togithub.com/nodejs/node/pull/33839)
-   \[[`b1c9f75a20`](https://togithub.com/nodejs/node/commit/b1c9f75a20)] - **src**: use tolocal in node_os.cc (wenningplus) [#&#8203;33939](https://togithub.com/nodejs/node/pull/33939)
-   \[[`153f292a97`](https://togithub.com/nodejs/node/commit/153f292a97)] - **src**: handle empty maybe(local) in node_util.cc (anna henningsen) [#&#8203;33867](https://togithub.com/nodejs/node/pull/33867)
-   \[[`6d5383de35`](https://togithub.com/nodejs/node/commit/6d5383de35)] - **src**: improve indention for upd_wrap.cc (gengjiawen) [#&#8203;33976](https://togithub.com/nodejs/node/pull/33976)
-   \[[`437f387de9`](https://togithub.com/nodejs/node/commit/437f387de9)] - **src**: reduce scope of code cache mutex (anna henningsen) [#&#8203;33980](https://togithub.com/nodejs/node/pull/33980)
-   \[[`9199808355`](https://togithub.com/nodejs/node/commit/9199808355)] - **src**: do not track baseobjects via cleanup hooks (anna henningsen) [#&#8203;33809](https://togithub.com/nodejs/node/pull/33809)
-   \[[`5b987c46b7`](https://togithub.com/nodejs/node/commit/5b987c46b7)] - **src**: remove ref to tools/generate_code_cache.js (daniel bevenius) [#&#8203;33825](https://togithub.com/nodejs/node/pull/33825)
-   \[[`185657dfd7`](https://togithub.com/nodejs/node/commit/185657dfd7)] - **src**: remove unused vector include in string_bytes (daniel bevenius) [#&#8203;33824](https://togithub.com/nodejs/node/pull/33824)
-   \[[`ec2452c4af`](https://togithub.com/nodejs/node/commit/ec2452c4af)] - **src**: avoid unnecessary tolocalchecked calls (daniel bevenius) [#&#8203;33824](https://togithub.com/nodejs/node/pull/33824)
-   \[[`74843db28c`](https://togithub.com/nodejs/node/commit/74843db28c)] - **src**: simplify format in node_file.cc (himself65) [#&#8203;33660](https://togithub.com/nodejs/node/pull/33660)
-   \[[`86283aaa6a`](https://togithub.com/nodejs/node/commit/86283aaa6a)] - **src**: handle missing tracingcontroller everywhere (anna henningsen) [#&#8203;33815](https://togithub.com/nodejs/node/pull/33815)
-   \[[`e07c1c2508`](https://togithub.com/nodejs/node/commit/e07c1c2508)] - **src**: simplify reindent function in json_utils.cc (sapics) [#&#8203;33722](https://togithub.com/nodejs/node/pull/33722)
-   \[[`449d9ec1c5`](https://togithub.com/nodejs/node/commit/449d9ec1c5)] - **src**: add "missing" bash completion options (daniel bevenius) [#&#8203;33744](https://togithub.com/nodejs/node/pull/33744)
-   \[[`4b4fb1381b`](https://togithub.com/nodejs/node/commit/4b4fb1381b)] - **src**: use check() instead of fromjust in environment (daniel bevenius) [#&#8203;33706](https://togithub.com/nodejs/node/pull/33706)
-   \[[`6f1d38cd8f`](https://togithub.com/nodejs/node/commit/6f1d38cd8f)] - **src**: use tolocal in safegetenv (daniel bevenius) [#&#8203;33695](https://togithub.com/nodejs/node/pull/33695)
-   \[[`5b8cac8cf5`](https://togithub.com/nodejs/node/commit/5b8cac8cf5)] - **src**: remove unnecessary tolocalchecked call (daniel bevenius) [#&#8203;33683](https://togithub.com/nodejs/node/pull/33683)
-   \[[`eb8d6f5fd8`](https://togithub.com/nodejs/node/commit/eb8d6f5fd8)] - **src**: simplify maybestackbuffer::capacity() (ben noordhuis) [#&#8203;33602](https://togithub.com/nodejs/node/pull/33602)
-   \[[`e3beb781e0`](https://togithub.com/nodejs/node/commit/e3beb781e0)] - **src**: avoid oob read in url parser (anna henningsen) [#&#8203;33640](https://togithub.com/nodejs/node/pull/33640)
-   \[[`99371ade2a`](https://togithub.com/nodejs/node/commit/99371ade2a)] - **src**: use maybelocal.tolocal instead of isempty worker (daniel bevenius) [#&#8203;33599](https://togithub.com/nodejs/node/pull/33599)
-   \[[`9c69296990`](https://togithub.com/nodejs/node/commit/9c69296990)] - **src**: don't use semicolon outside function (shelley vohr) [#&#8203;33592](https://togithub.com/nodejs/node/pull/33592)
-   \[[`41d879616f`](https://togithub.com/nodejs/node/commit/41d879616f)] - **src**: remove unused using declarations (daniel bevenius) [#&#8203;33268](https://togithub.com/nodejs/node/pull/33268)
-   \[[`103479a0c5`](https://togithub.com/nodejs/node/commit/103479a0c5)] - **src**: use maybelocal.tolocal instead of isempty (daniel bevenius) [#&#8203;33554](https://togithub.com/nodejs/node/pull/33554)
-   \[[`05cbd8f6f2`](https://togithub.com/nodejs/node/commit/05cbd8f6f2)] - **src**: use const in constant args.length() (himself65) [#&#8203;33555](https://togithub.com/nodejs/node/pull/33555)
-   \[[`48035a2a35`](https://togithub.com/nodejs/node/commit/48035a2a35)] - **src**: use maybelocal::frommaybe to return exception (daniel bevenius) [#&#8203;33514](https://togithub.com/nodejs/node/pull/33514)
-   \[[`e1050344f8`](https://togithub.com/nodejs/node/commit/e1050344f8)] - **_revert_** "**src**: fix missing extra ca in tls.rootcertificates" (eric bickle) [#&#8203;33313](https://togithub.com/nodejs/node/pull/33313)
-   \[[`77b6298b67`](https://togithub.com/nodejs/node/commit/77b6298b67)] - **src**: remove beforeexit callback list (ben noordhuis) [#&#8203;33386](https://togithub.com/nodejs/node/pull/33386)
-   \[[`a522c0e2c7`](https://togithub.com/nodejs/node/commit/a522c0e2c7)] - **src**: use maybelocal.tolocal instead of isempty (daniel bevenius) [#&#8203;33457](https://togithub.com/nodejs/node/pull/33457)
-   \[[`0837c2cc99`](https://togithub.com/nodejs/node/commit/0837c2cc99)] - **src**: remove unused headers in src/util.h (juan josé arboleda) [#&#8203;33070](https://togithub.com/nodejs/node/pull/33070)
-   \[[`6f6fb1fcf5`](https://togithub.com/nodejs/node/commit/6f6fb1fcf5)] - **src**: prefer make_unique (michael dawson) [#&#8203;33378](https://togithub.com/nodejs/node/pull/33378)
-   \[[`c697b96dea`](https://togithub.com/nodejs/node/commit/c697b96dea)] - **src**: remove unnecessary else in base_object-inl.h (daniel bevenius) [#&#8203;33413](https://togithub.com/nodejs/node/pull/33413)
-   \[[`abf04b245a`](https://togithub.com/nodejs/node/commit/abf04b245a)] - **src,build**: add --openssl-default-cipher-list (daniel bevenius) [#&#8203;33708](https://togithub.com/nodejs/node/pull/33708)
-   \[[`62edaaefc2`](https://togithub.com/nodejs/node/commit/62edaaefc2)] - **stream**: fix the spellings (antsmartian) [#&#8203;33635](https://togithub.com/nodejs/node/pull/33635)
-   \[[`998b22cbbc`](https://togithub.com/nodejs/node/commit/998b22cbbc)] - **test**: add test for http2serverresponse#\[writablecorked,cork,uncork] (pranshu srivastava) [#&#8203;33956](https://togithub.com/nodejs/node/pull/33956)
-   \[[`9b8695fb35`](https://togithub.com/nodejs/node/commit/9b8695fb35)] - **test**: account for non-node basename (shelley vohr) [#&#8203;33952](https://togithub.com/nodejs/node/pull/33952)
-   \[[`b9f8034f95`](https://togithub.com/nodejs/node/commit/b9f8034f95)] - **test**: fix typo in common/index.js (gengjiawen) [#&#8203;33976](https://togithub.com/nodejs/node/pull/33976)
-   \[[`7744f66e0d`](https://togithub.com/nodejs/node/commit/7744f66e0d)] - **test**: print arguments passed to mustnotcall function (denys otrishko) [#&#8203;33951](https://togithub.com/nodejs/node/pull/33951)
-   \[[`b5113d0b53`](https://togithub.com/nodejs/node/commit/b5113d0b53)] - **test**: temporarily exclude test on arm (michael dawson) [#&#8203;33814](https://togithub.com/nodejs/node/pull/33814)
-   \[[`c50bd2f954`](https://togithub.com/nodejs/node/commit/c50bd2f954)] - **test**: fix invalid regular expressions in case test-trace-exit (legendecas) [#&#8203;33769](https://togithub.com/nodejs/node/pull/33769)
-   \[[`d374e76428`](https://togithub.com/nodejs/node/commit/d374e76428)] - **test**: changed function to arrow function (sagar jadhav) [#&#8203;33711](https://togithub.com/nodejs/node/pull/33711)
-   \[[`0982bf4234`](https://togithub.com/nodejs/node/commit/0982bf4234)] - **test**: uv_tty_init now returns einval on ibm i (xu meng) [#&#8203;33629](https://togithub.com/nodejs/node/pull/33629)
-   \[[`3032f0f38d`](https://togithub.com/nodejs/node/commit/3032f0f38d)] - **test**: make flaky test stricter (robert nagy) [#&#8203;33539](https://togithub.com/nodejs/node/pull/33539)
-   \[[`ef27e6ce57`](https://togithub.com/nodejs/node/commit/ef27e6ce57)] - **test**: mark test-dgram-multicast-ssmv6-multi-process flaky (ashcripps) [#&#8203;33498](https://togithub.com/nodejs/node/pull/33498)
-   \[[`a131c72586`](https://togithub.com/nodejs/node/commit/a131c72586)] - **tools**: enable no-else-return lint rule (luigi pinca) [#&#8203;32667](https://togithub.com/nodejs/node/pull/32667)
-   \[[`6651bde34e`](https://togithub.com/nodejs/node/commit/6651bde34e)] - **tools**: update remark-preset-lint-node@1.15.1 to 1.16.0 (rich trott) [#&#8203;33852](https://togithub.com/nodejs/node/pull/33852)
-   \[[`2e38f0dafd`](https://togithub.com/nodejs/node/commit/2e38f0dafd)] - **tools**: remove superfluous regex in tools/doc/json.js (rich trott) [#&#8203;33998](https://togithub.com/nodejs/node/pull/33998)
-   \[[`ba813dd0dd`](https://togithub.com/nodejs/node/commit/ba813dd0dd)] - **tools**: prevent js2c from running if nothing changed (daniel bevenius) [#&#8203;33844](https://togithub.com/nodejs/node/pull/33844)
-   \[[`fd5ab63d96`](https://togithub.com/nodejs/node/commit/fd5ab63d96)] - **tools**: remove unused vector include in mkdcodecache (daniel bevenius) [#&#8203;33828](https://togithub.com/nodejs/node/pull/33828)
-   \[[`54a4a816a4`](https://togithub.com/nodejs/node/commit/54a4a816a4)] - **tools**: update eslint to 7.2.0 (colin ihrig) [#&#8203;33776](https://togithub.com/nodejs/node/pull/33776)
-   \[[`5328089c91`](https://togithub.com/nodejs/node/commit/5328089c91)] - **tools**: remove unused using declarations code_cache (daniel bevenius) [#&#8203;33697](https://togithub.com/nodejs/node/pull/33697)
-   \[[`2f02fbac3a`](https://togithub.com/nodejs/node/commit/2f02fbac3a)] - **tools**: update remark-preset-lint-node from 1.15.0 to 1.15.1 (rich trott) [#&#8203;33727](https://togithub.com/nodejs/node/pull/33727)
-   \[[`3d05e3d861`](https://togithub.com/nodejs/node/commit/3d05e3d861)] - **tools**: fix check-imports.py to match on word boundaries (richard lau) [#&#8203;33268](https://togithub.com/nodejs/node/pull/33268)
-   \[[`ff4f9a9247`](https://togithub.com/nodejs/node/commit/ff4f9a9247)] - **tools**: update eslint to 7.1.0 (colin ihrig) [#&#8203;33526](https://togithub.com/nodejs/node/pull/33526)
-   \[[`f495ab3dcb`](https://togithub.com/nodejs/node/commit/f495ab3dcb)] - **tools**: add docserve target (antoine du hamel) [#&#8203;33221](https://togithub.com/nodejs/node/pull/33221)
-   \[[`a9dbb224af`](https://togithub.com/nodejs/node/commit/a9dbb224af)] - **util**: fix width detection for del without icu (ruben bridgewater) [#&#8203;33650](https://togithub.com/nodejs/node/pull/33650)
-   \[[`02ae3f5625`](https://togithub.com/nodejs/node/commit/02ae3f5625)] - **util**: support combining diacritical marks for symbols (ruben bridgewater) [#&#8203;33650](https://togithub.com/nodejs/node/pull/33650)
-   \[[`524b230143`](https://togithub.com/nodejs/node/commit/524b230143)] - **util**: gracefully handle unknown colors (ruben bridgewater) [#&#8203;33797](https://togithub.com/nodejs/node/pull/33797)
-   \[[`e3533ab337`](https://togithub.com/nodejs/node/commit/e3533ab337)] - **util**: mark classes while inspecting them (ruben bridgewater) [#&#8203;32332](https://togithub.com/nodejs/node/pull/32332)
-   \[[`c4129f91e8`](https://togithub.com/nodejs/node/commit/c4129f91e8)] - **vm**: allow proxy callbacks to throw (gus caplan) [#&#8203;33808](https://togithub.com/nodejs/node/pull/33808)
-   \[[`8adfb542eb`](https://togithub.com/nodejs/node/commit/8adfb542eb)] - **wasi**: allow wasi stdio to be configured (colin ihrig) [#&#8203;33544](https://togithub.com/nodejs/node/pull/33544)
-   \[[`33984d6e4d`](https://togithub.com/nodejs/node/commit/33984d6e4d)] - **wasi**: simplify wasi memory management (colin ihrig) [#&#8203;33525](https://togithub.com/nodejs/node/pull/33525)
-   \[[`5e5be9929b`](https://togithub.com/nodejs/node/commit/5e5be9929b)] - **wasi**: refactor and enable poll_oneoff() test (colin ihrig) [#&#8203;33521](https://togithub.com/nodejs/node/pull/33521)
-   \[[`383c5b3962`](https://togithub.com/nodejs/node/commit/383c5b3962)] - **wasi**: relax webassembly.instance type check (ben noordhuis) [#&#8203;33431](https://togithub.com/nodejs/node/pull/33431)
-   \[[`7df79f498c`](https://togithub.com/nodejs/node/commit/7df79f498c)] - **wasi,worker**: handle termination exception (ben noordhuis) [#&#8203;33386](https://togithub.com/nodejs/node/pull/33386)
-   \[[`3b46e7f148`](https://togithub.com/nodejs/node/commit/3b46e7f148)] - **win,fs**: use namespaced path in absolute symlinks (bartosz sosnowski) [#&#8203;33351](https://togithub.com/nodejs/node/pull/33351)
-   \[[`4388dad537`](https://togithub.com/nodejs/node/commit/4388dad537)] - **win,msi**: add arm64 config for windows msi (dennis ameling) [#&#8203;33689](https://togithub.com/nodejs/node/pull/33689)
-   \[[`032c64f1e4`](https://togithub.com/nodejs/node/commit/032c64f1e4)] - **worker**: fix variable referencing in template string (harshitha kp) [#&#8203;33467](https://togithub.com/nodejs/node/pull/33467)
-   \[[`1c64bc5e34`](https://togithub.com/nodejs/node/commit/1c64bc5e34)] - **worker**: perform initial port.unref() before preload modules (anna henningsen) [#&#8203;33455](https://togithub.com/nodejs/node/pull/33455)
-   \[[`c502384ab7`](https://togithub.com/nodejs/node/commit/c502384ab7)] - **worker**: use \_writev in internal communication (anna henningsen) [#&#8203;33454](https://togithub.com/nodejs/node/pull/33454)

</details>

---

### renovate configuration

:date: **schedule**: at any time (no schedule defined).

:vertical_traffic_light: **automerge**: disabled by config. please merge this manually once you are satisfied.

:recycle: **rebasing**: whenever pr becomes conflicted, or you tick the rebase/retry checkbox.

:no_bell: **ignore**: close this pr and you won't be reminded about this update again.

---

 - [ ] <!-- rebase-check -->if you want to rebase/retry this pr, check this box

---

this pr has been generated by [whitesource renovate](https://renovate.whitesourcesoftware.com). view repository job log [here](https://app.renovatebot.com/dashboard#github/jupyterhub/configurable-http-proxy).

##Repo ID: 25440

##Contributer ID: 143074

##Pull Request ID: 281019

###Profanity Found
**Text**
in the initial entities implementation, a rest feature for filtered-discovery-page has been created.
this was later-on noticed as a feature which is not necessary.

this pr removes this functionality

##Repo ID: 22104

##Contributer ID: 85808

##Pull Request ID: 246857

###Profanity Found
**Text**
## overview

this pull request adds a 2 step user registration system with email verification

### demo

```
$ http http://localhost:3005/auth/email/register email=mmaurizi@azavea.com password=mike12345 name="mike m"
http/1.1 201 created                                                                                                                                                                    
connection: keep-alive                                                                                                                                                                  
content-length: 7
content-type: text/html; charset=utf-8                                                                                                                                                  
date: thu, 02 apr 2020 15:39:44 gmt                                                                                                                                                     
etag: w/"7-gfw9aupkrb4jbgwx0k+slemacno"                                                                                                                                                 
x-powered-by: express                                                                                                                                                                   
                                                                                                                                                                                        
success

$ http post http://localhost:3005/auth/email/resend-verification/mmaurizi@azavea.com
http/1.1 201 created
connection: keep-alive
content-length: 7
content-type: text/html; charset=utf-8
date: thu, 02 apr 2020 16:13:31 gmt
etag: w/"7-gfw9aupkrb4jbgwx0k+slemacno"
x-powered-by: express

success

$ http post http://localhost:3005/auth/email/verify/iku9orzhsplzzkrsywoo7vdjn9u
http/1.1 201 created
connection: keep-alive
content-length: 114
content-type: application/json; charset=utf-8
date: thu, 02 apr 2020 16:13:50 gmt
etag: w/"72-kdki5zx15wvb9oy36dywp6gsu3m"
x-powered-by: express

{
    "email": "mmaurizi@azavea.com",
    "id": "0614a225-8d2b-4c71-acdc-d66b4869b470",
    "isemailverified": true,
    "name": "mike m"
}

$ http post http://localhost:3005/auth/email/login email=mmaurizi@azavea.com password=mike12345
http/1.1 201 created
connection: keep-alive
content-length: 114
content-type: application/json; charset=utf-8
date: thu, 02 apr 2020 16:41:44 gmt
etag: w/"72-kdki5zx15wvb9oy36dywp6gsu3m"
x-powered-by: express

{
    "email": "mmaurizi@azavea.com",
    "id": "0614a225-8d2b-4c71-acdc-d66b4869b470",
    "isemailverified": true,
    "name": "mike m"
}

$ http post http://localhost:3005/auth/email/login email=mmaurizi@azavea.com password=mike54321
http/1.1 400 bad request
connection: keep-alive
content-length: 74
content-type: application/json; charset=utf-8
date: thu, 02 apr 2020 16:41:52 gmt
etag: w/"4a-j+tcadnmdmqd2xhuxvqyixrnqbg"
x-powered-by: express

{
    "error": "invalid password",
    "message": "invalid_password",
    "statuscode": 400
}


```

### notes

 - i haven't disabled `login` for users whose emails are not verified because i didn't know if we wanted to restrict login entirely or merely restrict access in the application to features that need email.
 - i'm deferring password validation to a future issue, hopefully i can find something that has an equivalent react ui component to validate during registration in #52 
 - we need to add issues forgot password & change password apis & frontend pages, we missed those in our initial planning
 - we should add an issue to update the email registration copy / style it.
 - i didn't 1-for-1 copy much, but i used this as a reference work quite a bit: https://github.com/marcomelilli/nestjs-email-authentication/

## testing instructions

- `scripts/update`
- create a user using the `/auth/email/register`endpoint
- login using `auth/email/login`
- verify that you see email contents printed to the console running `scripts/server`
- test resending an email with `/auth/email/resend-verification/:email`
- using the token in the email printed to the console, verify your user using `auth/email/verify/:token` 

closes #49 

##Repo ID: 25236

##Contributer ID: 178207

##Pull Request ID: 280005

###Profanity Found
**Text**
## overview

adds an email-based system for resetting a forgottten password.

### demo

![localhost_3003_ (14)](https://user-images.githubusercontent.com/4432106/82921752-b9aef700-9f46-11ea-90d8-09e6ed25ae48.png)
![localhost_3003_password-reset_crc8s3cgoeazltlok5oxvq_3epw](https://user-images.githubusercontent.com/4432106/82921749-b9aef700-9f46-11ea-9fef-425561b2791e.png)
![localhost_3003_ (15)](https://user-images.githubusercontent.com/4432106/82921750-b9aef700-9f46-11ea-9fbb-dfb45f2d451e.png)
![localhost_3003_password-reset_crc8s3cgoeazltlok5oxvq_3epw (2)](https://user-images.githubusercontent.com/4432106/82921748-b9166080-9f46-11ea-82c1-dbcc7b952755.png)


### notes

 - i combined the models for email verification & password registration into 1 model with a type column that differentiates them, which seemed more dry but is different from how the sample repo i looked at for #74 did things.
 - we weren't checking email verification links for expiration (:astonished:) so i added a 1 day expiration for both the password reset email & the initial verification email

## testing instructions

- http://localhost:3003/forgot-password

closes #76 

##Repo ID: 25236

##Contributer ID: 178207

##Pull Request ID: 280027

###Profanity Found
**Text**
this small pr gives administrators the ability to discover (both) withdrawn and private items. it includes:

- a new discovery configuration (in discovery.xml) called "showundiscoverableitems". the configuration includes solr filters that find items that have been withdrawn or made private.
- a new `solrservicesearchplugin` that prevents discovery of withdrawn or private items by non-administrative users.
- changes to `discoveryrestrepository` that cause the `solrserviceimpl.search()` method to be called with `includeundiscoverable = true` for requests that include the "showundiscoverableitems" configuration.
- modification of `discoveryconfigurationservice` to allow for discovery configurations that include the a community handle (e.g.: "showundiscoverableitems.12345/12")

integration tests will be added.

### needed feedback
it would be great to have feedback on how well the requirements described in the jira issue https://jira.duraspace.org/browse/ds-3906 have been met by this initial pr. if the general approach looks good i can refine things a bit and add its.  some documentation should also be added to the rest contract, i think.

also, browse for withdrawn items and private items are separate features on the development spreadsheet, but there's a note asking whether these features can be combined.  this configuration as of now combines the two.

##Repo ID: 22104

##Contributer ID: 85758

##Pull Request ID: 246938

###Profanity Found
**Text**
this is a work-in-progress pr to add docker support to vufind. i based the initial draft of these changes on the latest 3.1 tag, so i could start from a known-working vufind state (that's also why the 3.1.3 version bump commit is caught up in this pr; let me know if that's an issue). for a completely working example context to play with, see [unicalabs/vufind:release-3.1](https://github.com/unicalabs/vufind/tree/release-3.1).

### additions

* `dockerfile` enables the building of a docker image with support for php 7.1 and apache.
* `docker-vufind-entrypoint` enables custom behavior within the vufind container at runtime, often based on environment variables (such as `vufind_mysql_url` or `vufind_solr_url`).
* `docker-compose.yml` enables the creation of a full working stack for development purposes, including vufind (from the above image), solr (from their official image), and mysql (from their official image). the same principles can be applied for a production stack.
* `solr/docker/dev_link_vendor.sh` is a symlink hack to map the file structure the biblio core config expects to the one provided by the official solr container image.

### modifications
* `build.xml` now checks if the `vufind_install_solr` environment variable is set before installing solr. if the value is `no`, solr will not be downloaded and installed. the docker image doesn't need a solr server installed within (it has a separate container from the official solr project for that), so this saves space/time.  

### development use
with [docker](https://www.docker.com/community-edition#/download) and [docker compose](https://docs.docker.com/compose/install/) installed, one can run `docker-compose up` and have a fully-working development environment, including a provisioned mysql database (available from your local machine at `mysql://root@localhost/vufind` and within the vufind container at `mysql://root@mysql/vufind`) and a solr instance (available from your local machine at http://localhost:8983/solr and within the vufind container at http://solr:8983/solr).

**warning:** by design, data in the mysql database and solr instance currently will disappear when their respective containers are halted.

### production use
production use looks a bit different. as i work through the implementation, i'd like to create some documentation and public examples.

### to-do
a few things i need to work on:

- [x]  resolve zend error, likely from post-`3.1.2` work-in-process in `master` (i could use help with this one):
```
fatal error: uncaught typeerror: argument 1 passed to zend\servicemanager\abstractpluginmanager::__construct() must implement interface zend\servicemanager\configinterface or be null, instance of zend\servicemanager\servicemanager given, called in /usr/local/vufind/module/vufind/src/vufind/service/factory.php on line 143 and defined in /usr/local/vufind/vendor/zendframework/zendframework/library/zend/servicemanager/abstractpluginmanager.php:62

stack trace: 
#0 /usr/local/vufind/module/vufind/src/vufind/service/factory.php(143): zend\servicemanager\abstractpluginmanager->__construct(object(zend\servicemanager\servicemanager), array) 
#1 [internal function]: vufind\service\factory::getconfig(object(zend\servicemanager\servicemanager), 'vufindconfig', 'vufind\\config') 
#2 /usr/local/vufind/vendor/zendframework/zendframework/library/zend/servicemanager/servicemanager.php(939): call_user_func('vufind\\service\\...', object(zend\servicemanager\servicemanager), 'vufindconfig', 'vufind\\config') 
#3 /usr/local/vufind/vendor/zendfram in /usr/local/vufind/vendor/zendframework/zendframework/library/zend/servicemanager/abstractpluginmanager.php on line 62
```
- [x]  resolve solr error, likely just a moved library from post-`3.1.2` work-in-process in `master`:
```
org.apache.solr.common.solrexception: could not load conf for core biblio: can't load schema /opt/solr/server/solr/mycores/biblio/conf/schema.xml: plugin init failure for [schema.xml] fieldtype "text": plugin init failure for [schema.xml] analyzer/tokenizer: error loading class 'solr.icutokenizerfactory'
```
- [x]  improve `docker-vufind-entrypoint` to hot-overwrite the local `config.ini` with mysql/solr connection information from environment variables. the default state needs to work for dev, and prod use should necessitate setting these values.
- [ ]  create example project: https://github.com/unicalabs/vufind-docker-example
- [x]  revise according to [failed codacy checks](https://www.codacy.com/app/crhallberg/vufind/pullrequest?prid=639234).
- [x]  make vufind available at the site root instead of at `/vufind`.
- [x]  adjust the `phing installsolr` job to do nothing if it's running in a dockerized environment. this should improve image build and dev first-run performance significantly.

##Repo ID: 25234

##Contributer ID: 81348

##Pull Request ID: 249046

###Profanity Found
**Text**
an initial attempt at publications/symplectic integration. i'm mainly looking for feedback on the apis/data model..
## publications

publications are not linked to any specific tenant and have a very basic datamodel (for now).
each publication is identified by 1 or more source ids. for example:

the publication p:abc123def which was ingested from symplectic. they originally harvested it from
pubmed and web of science. the source ids for this publication would look something like:
- pubmed#cc-112-aeda
- wos#32146541234525

this allows for having multiple ingesters which can ingest publications but keep duplication to a minimum.
for example, if there would ever be a pubmed ingester, it should ingest the same publication with
source id `pubmed#cc-112-eada`. the ingestion api will detect that there already is a publication for this source id
in the system and will not create a second record.

oae users from different tenants can be linked to a single publications. this is to enhance
the cross-tenant. linking a user to a publication happens by passing in:
- the publication id
- the oae user id
- the name of the user as found in the publication

the passed in name doesn't have to be a full match as some (very basic) disambiguation will be used (jarowinkler).
### rest api

this logic is also exposed on the rest api even though there is no current ui need for it (yet).
this has been done so data loads with the model loader can happen. there is a configuration option in the admin ui
which allows an admin to enable this for regular users. tenant and global admins can always use the rest api
## symplectic

an example ingester for symplectic has been added. it's able to do either full or incremental synchronizations.
it will run a synchronization on a configurable (config.js) interval.
on a full update it will:
- iterate over all the users in symplectic, fetch their publications and ingest them

on an incremental update it will:
- iterate over all the _updated_ users in symplectic since the last run, fetch their publications and ingest them
- retrieve publications for any new oae users
- retry any user that failed previously

symplectic can be enabled on a tenant-by-tenant basis in the admin ui.
publications that are marked as invisible will not be ingested.


##Repo ID: 25206

##Contributer ID: 79267

##Pull Request ID: 247326

###Profanity Found
**Text**
jira: https://jira.lyrasis.org/browse/ds-4425

this pr will fix the performance issues raised with the rework of the indexableobject. the problem was located in the indexeventconsumer. 

the previous behavior for when a workflow item passed the consumer:
* it would add the item from that workflow item to the "to-index-list" of objects to be indexed.
* it then passed this single object to discovery service
* this discovery method would resolve the object into the related objects (item, workflow item, pooled task, ...)
* the discovery method would trigger a single commit at the end commit

what my code changed:
* instead of adding the single object the code would add all the related objects to the "to-index-list", so for a workflow item this would be: item, workflow item, pooled task, ...
* it would then pass these objects one by one to the discovery service doing a single commit for each of them. this would lead to x number of additional commits to the solr which was slowing the whole thing down.

what we did to fix it:
* all the objects are still added to the "to-index-list"
* we still pass each object to the discovery service but do not trigger a commit at the end
* we trigger a single commit at the end of the consumer when we are done looping over all the objects

the fix here has the initial benefit if multiple items are deposited at a single context.commit that there will now only be one commit instead of a single commit for every item. so the general performance of dspace should also be better.

ps: the timing for the travis could still be a bit longer then it was before the indexableobject merge, but this is because the api tests have increased from 815 to 833

##Repo ID: 22104

##Contributer ID: 85802

##Pull Request ID: 263865

###Profanity Found
**Text**
…nless necessary.

this is an initial attempt at trying to reduce the situations where an ils connection is made so that the database connection is not established unless it's actually needed. this means that e.g. getconfig() could be called without the database connection. currently the lazy connection initialization is only in voyager driver because i can't test the others, but it could be extended if this mechanism is found viable. this pr avoids making the ils connection at least when displaying favorites and saved searches (plus some other situations in our customized version). previously the check for support of password change initialized the connection when logged in with a library card. feedback appreciated!


##Repo ID: 25234

##Contributer ID: 181580

##Pull Request ID: 248820

###Profanity Found
**Text**
…earch/home. fixed lateral links (author, subject etc.) to also include the current hidden filters.

to reproduce the first issue:

1.) configure search tabs so that also the initial tab has filters
2.) start a new session
3.) go directly to e.g. myresearch/home
4.) do a search from there.


##Repo ID: 25234

##Contributer ID: 181580

##Pull Request ID: 248731

###Profanity Found
**Text**
switched to trigger() for the selection event so that it can be bound to with the bind() function and the initialization function doesn't need to be modified.
moved the autocomplete window to the form so that the bounding rect is not needed thus avoiding positioning problems e.g. when window is scrolled while suggestions are loading.
align suggestions when window is resized.
set the initial content with .html().
use the greater of input width and form width for the maximum autocomplete list width instead of the arbitrary \* 2 width.


##Repo ID: 25234

##Contributer ID: 181580

##Pull Request ID: 248617

###Profanity Found
**Text**
draft pr to build macos releases with the extension json files.
this should add the postinst/prerm scripts for deb files to add the extension automatically
add initial json files on macos

##Repo ID: 25219

##Contributer ID: 80154

##Pull Request ID: 279692

###Profanity Found
**Text**
bumps [snyk](https://github.com/snyk/snyk) from 1.298.0 to 1.342.2.
<details>
<summary>release notes</summary>
<p><em>sourced from <a href="https://github.com/snyk/snyk/releases">snyk's releases</a>.</em></p>
<blockquote>
<h2>v1.342.2</h2>
<h2><a href="https://github.com/snyk/snyk/compare/v1.342.1...v1.342.2">1.342.2</a> (2020-06-16)</h2>
<h3>bug fixes</h3>
<ul>
<li>handle undefined return from cli command (<a href="https://github.com/snyk/snyk/commit/1d7176347c2d00a2dae44b62bd80c52fcd8cfa40">1d71763</a>)</li>
</ul>
<h2>v1.342.1</h2>
<h2><a href="https://github.com/snyk/snyk/compare/v1.342.0...v1.342.1">1.342.1</a> (2020-06-16)</h2>
<h3>bug fixes</h3>
<ul>
<li>upgrade snky-docker-plugin (<a href="https://github.com/snyk/snyk/commit/d20b90b1b68442887dcea9b8331ff1b0a06bf8df">d20b90b</a>)</li>
</ul>
<h2>v1.342.0</h2>
<h1><a href="https://github.com/snyk/snyk/compare/v1.341.2...v1.342.0">1.342.0</a> (2020-06-16)</h1>
<h3>bug fixes</h3>
<ul>
<li>print-deps to only print under certain deps in graph threshold (<a href="https://github.com/snyk/snyk/commit/45440efadf147e12e5cf406b8e6f810932cc477d">45440ef</a>)</li>
</ul>
<h3>features</h3>
<ul>
<li>initial gradle graph support (<a href="https://github.com/snyk/snyk/commit/4fc47a36c943e9d1dfab2ca16530f4cf20f5b7bb">4fc47a3</a>)</li>
<li>support snyk test &amp; monitor with depgraph from plugins (<a href="https://github.com/snyk/snyk/commit/23dc1b303ce65e2f43a6848ff9d374f93b8c50f0">23dc1b3</a>)</li>
</ul>
<h2>v1.341.2</h2>
<h2><a href="https://github.com/snyk/snyk/compare/v1.341.1...v1.341.2">1.341.2</a> (2020-06-16)</h2>
<h3>bug fixes</h3>
<ul>
<li>make container commands use always static scan (<a href="https://github.com/snyk/snyk/commit/11baf79e0cc6965d843541cda5663c46b763ad5e">11baf79</a>)</li>
</ul>
<h2>v1.341.1</h2>
<h2><a href="https://github.com/snyk/snyk/compare/v1.341.0...v1.341.1">1.341.1</a> (2020-06-15)</h2>
<h3>bug fixes</h3>
<ul>
<li>remove duplicated call to maybeprintdeps (<a href="https://github.com/snyk/snyk/commit/9c238094703760d0d3c6fab3b88f981184c485c6">9c23809</a>)</li>
</ul>
<h2>v1.341.0</h2>
<h1><a href="https://github.com/snyk/snyk/compare/v1.340.0...v1.341.0">1.341.0</a> (2020-06-15)</h1>
</tr></table> ... (truncated)
</blockquote>
</details>
<details>
<summary>commits</summary>
<ul>
<li><a href="https://github.com/snyk/snyk/commit/ea3338361f9a55ac2244b3e90355310671dea8c8"><code>ea33383</code></a> merge pull request <a href="https://github-redirect.dependabot.com/snyk/snyk/issues/1177">#1177</a> from snyk/fix/unexpected-exit-on-ignore</li>
<li><a href="https://github.com/snyk/snyk/commit/df62c5d12d202b310b3a696af985cefc8ab307f5"><code>df62c5d</code></a> merge pull request <a href="https://github-redirect.dependabot.com/snyk/snyk/issues/1188">#1188</a> from snyk/fix/bump_snyk_docker_plugin_version</li>
<li><a href="https://github.com/snyk/snyk/commit/43f5b5d36f84f8d1c22c104216f29bf127fa6412"><code>43f5b5d</code></a> merge pull request <a href="https://github-redirect.dependabot.com/snyk/snyk/issues/1165">#1165</a> from snyk/feat/support-depgraph-deptree-coexistence</li>
<li><a href="https://github.com/snyk/snyk/commit/45440efadf147e12e5cf406b8e6f810932cc477d"><code>45440ef</code></a> fix: print-deps to only print under certain deps in graph threshold</li>
<li><a href="https://github.com/snyk/snyk/commit/d20b90b1b68442887dcea9b8331ff1b0a06bf8df"><code>d20b90b</code></a> fix: upgrade snky-docker-plugin</li>
<li><a href="https://github.com/snyk/snyk/commit/3ad359666de0ccbe0b578ad4a9c854cddb15bef9"><code>3ad3596</code></a> merge pull request <a href="https://github-redirect.dependabot.com/snyk/snyk/issues/1179">#1179</a> from snyk/fix/make_experimental_option_default_for_c...</li>
<li><a href="https://github.com/snyk/snyk/commit/d9313d879f0cf787c9fbda31888ef6f6008d9cf9"><code>d9313d8</code></a> chore: tests for new depgraph path</li>
<li><a href="https://github.com/snyk/snyk/commit/23dc1b303ce65e2f43a6848ff9d374f93b8c50f0"><code>23dc1b3</code></a> feat: support snyk test &amp; monitor with depgraph from plugins</li>
<li><a href="https://github.com/snyk/snyk/commit/4fc47a36c943e9d1dfab2ca16530f4cf20f5b7bb"><code>4fc47a3</code></a> feat: initial gradle graph support</li>
<li><a href="https://github.com/snyk/snyk/commit/1f96517856e417f46c4852f4de37afbc2c0dc786"><code>1f96517</code></a> refactor: target-builders minor changes</li>
<li>additional commits viewable in <a href="https://github.com/snyk/snyk/compare/v1.298.0...v1.342.2">compare view</a></li>
</ul>
</details>
<br />


[![dependabot compatibility score](https://api.dependabot.com/badges/compatibility_score?dependency-name=snyk&package-manager=npm_and_yarn&previous-version=1.298.0&new-version=1.342.2)](https://dependabot.com/compatibility-score/?dependency-name=snyk&package-manager=npm_and_yarn&previous-version=1.298.0&new-version=1.342.2)

dependabot will resolve any conflicts with this pr as long as you don't alter it yourself. you can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>dependabot commands and options</summary>
<br />

you can trigger dependabot actions by commenting on this pr:
- `@dependabot rebase` will rebase this pr
- `@dependabot recreate` will recreate this pr, overwriting any edits that have been made to it
- `@dependabot merge` will merge this pr after your ci passes on it
- `@dependabot squash and merge` will squash and merge this pr after your ci passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this pr if it is closed
- `@dependabot close` will close this pr and stop dependabot recreating it. you can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this pr and stop dependabot creating any more for this major version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this pr and stop dependabot creating any more for this minor version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this pr and stop dependabot creating any more for this dependency (unless you reopen the pr or upgrade to it yourself)
- `@dependabot use these labels` will set the current labels as the default for future prs for this repo and language
- `@dependabot use these reviewers` will set the current reviewers as the default for future prs for this repo and language
- `@dependabot use these assignees` will set the current assignees as the default for future prs for this repo and language
- `@dependabot use this milestone` will set the current milestone as the default for future prs for this repo and language
- `@dependabot badge me` will comment on this pr with code to add a "dependabot enabled" badge to your readme

additionally, you can set the following in your dependabot [dashboard](https://app.dependabot.com):
- update frequency (including time of day and day of week)
- pull request limits (per update run and/or open at any time)
- out-of-range updates (receive only lockfile updates, if desired)
- security updates (receive only security updates, if desired)



</details>

<!-- reviewable:start -->
---
this change is [<img src="https://reviewable.io/review_button.svg" height="34" align="absmiddle" alt="reviewable"/>](https://reviewable.io/reviews/oaeproject/hilary/2176)
<!-- reviewable:end -->


##Repo ID: 25206

##Contributer ID: 79282

##Pull Request ID: 280236

###Profanity Found
**Text**
this is a staging ground for full `async`/`await` support in translators. both `detect*()` and `do*()` can now be marked as `async` and can use `await` to wait for promise-returning functions. (import translators could already return a promise from `doimport()` and do incremental saving via promise-returning `item.complete()` functions, but it was hacky and unpleasant.)

this change is made possible by @adomasven's removal of the mozilla sandbox in favor of a less-secure `eval()`-based sandbox like what we use in the connectors. we're comfortable doing that because 1) we now load remote pages with xhr/domparser rather using hidden browsers and running translators in those browsers, so we're not worried about untrusted js on remote pages potentially getting access to privileged code and 2) we review translator code and can make sure translators are using only the translator api and aren't using `eval()`, so we don't need as strict isolation from globals or other zotero code that might be accessible somehow. we might still want to do some initial page loads in hidden browsers, but if necessary we can always let the js run and then reparse the dom with domparser to get a safe static document, at the cost of some efficiency.

currently, this exposes the promise-based `zotero.http.request()` as `zu.request()`, which returns a promise for an xmlhttprequest object. that may be a bit too verbose to expose directly to translators, so we need to figure out what request functionality translators really need and what it should look like. (ccing @adam3smith and @zuphilip for any thoughts they have on this.) among other things:

  * `doget()`/`dopost()` automatically fail translation on non-2xx status codes. we probably want to keep that in general, but some translators could possibly benefit from specifying that 403 or 404 isn't a fatal error. the main question is whether translators actually need a response object that allows them to check the response status code and content type. it may be enough 1) for 403/404 (when explicitly allowed?) to result in a promise resolution of `null` or to throw the promise with an `http.unexpectedstatusexception` that lets you check `.status` without throwing translation and 2) for content type to be ignored or handled with string checks (e.g., does this look like ris?).
  * we should simplify the `zotero.http.request()` signature in general (both for translators and for the rest of zotero) to allow a url in the first parameter, similar to `fetch()`, and do a get if not specified in `options`. (technically a `body` in `options` could even make it default to post, though `method` would still be possible in `options` for other methods.)
  * `doget()`/`dopost()` return raw text, which is useful for anything retrieving bibtex/ris/etc. it would be nice to be able to just do `var ris = await request(url);`.
  * we can probably stop using `processdocuments()` altogether, since `zotero.http.request()` supports `response: 'document'`. instead you'd just do a loop and run the handler function on the `await`ed response. as above, if we didn't return a response object we'd need to decide how to convey that a response either couldn't be parsed as a document or was a 403/404. `null` is probably sufficient for the former, and the latter could be either `null` or a thrown promise. maybe a translator doesn't care about the distinction and only cares whether it got 1) a 200 and an html document or 2) something else?

we won't be able to start using this in translators for probably a month after the first release that includes it, at which time we can cut off translator updates for older versions.

down the line, it would be nice to get rid of the callback-based functions so that we can remove the horrible `incrementasyncprocesses()`/etc. stuff in the translator framework.

##Repo ID: 22063

##Contributer ID: 80779

##Pull Request ID: 251362

###Profanity Found
**Text**
fixes #3000 

<img width="131" alt="screen shot 2020-05-08 at 07 40 23" src="https://user-images.githubusercontent.com/111218/81416856-30529480-90ff-11ea-8519-432ba3f942bf.png">

the default configuration is  still to initialize with  a default sidebar, but  this can be disabled  with the initial configuration:

```
       window: {
         defaultsidebarpanel: null,
       }, 
```

##Repo ID: 25222

##Contributer ID: 175396

##Pull Request ID: 279589

###Profanity Found
**Text**
resolves: https://jira.lyrasis.org/browse/ds-4480

* use discrete pojos (element) for representing metadata structure as xml rather than xmlelement
* add policy pojo for capturing resourcepolicies which are on dspaceobjects
* write policy.xml when packaging bagit aips
* when reading xml, use the elementdeserializer to allow easier reading of different elements

--------------------------------

## notes

the main goal of this was to package the `resourcepolicy` objects on each `dspaceobject` which is being packaged. most of this will look similar to the `metsrightscrosswalk`, with things being simplified a bit for the bagit packers. an example of what the `policy.xml` looks like is provided in the tests:
```
<policies>
        <value rp-in-effect="true" rp-end-date="2100-01-01" rp-context="administrator" rp-action="admin">administrator</value>
        <value rp-in-effect="true" rp-start-date="2000-01-01" rp-context="anonymous" rp-action="read">anonymous</value>
        <value rp-in-effect="true" rp-start-date="2000-01-01" rp-context="anonymous" rp-action="read_item">anonymous</value>
        <value rp-in-effect="true" rp-start-date="2000-01-01" rp-context="anonymous" rp-action="read_bitstream">anonymous</value>
        <value rp-name="user add" rp-description="dspace user add policy" rp-in-effect="true" rp-context="academic user" rp-action="add">dspace-user@localhost.localdomain</value>
        <value rp-in-effect="true" rp-context="academic user" rp-action="write">dspace-user@localhost.localdomain</value>
        <value rp-in-effect="true" rp-context="academic user" rp-action="remove">dspace-user@localhost.localdomain</value>
        <value rp-in-effect="true" rp-context="academic user" rp-action="delete">dspace-user@localhost.localdomain</value>
</policies>
```
the `value` attributes are composed of the `resourcepolicy` fields. the `rp-action` is mapped directly by using the values defined in `constants` to string equivalents (see `bagitpolicyutil#actionmapper()`). the body of the `value` tag will be the `group` name or `eperson` email, which is used to fetch them from the dspace database when importing.


there are also changes to how xml is handled by the bagit packers. most of this was done in anticipation of ds-4481 because the dspace-roles schema would not be supported as easily with how the bagit packers were previously handling xml. overall, the changes are:
* `xmlelement` -> `element` (roughly)
* pojos for each tag which implement `element`, e.g. `metadata`, `policy`, and `value`
* `elementdeserializer` in order to have per-tag deserialization
  * `metadatadeserializer` searches for the `metadata` tag, then uses the `valuedeserializer` in order to read all the value tags

-----------------------------------

## testing

1. create a new dspace repository with the rts and bagit enabled 
2. create a community, collection, and item
3. edit the authorizations for each of the above
    a. can be for a group, eperson. etc
4. run the `transfer aip(s)` curation option for the community
5. review the `policy.xml` written for...
    a. the community
    b. the collection
    c. the item and bitstreams
6. remove some of the authorizations changed?
7. run the `replace all aips` curation option for the community
8. review the authorizations and verify they match what exist when the initial transfer was done


##Repo ID: 22100

##Contributer ID: 157084

##Pull Request ID: 279616

###Profanity Found
**Text**
resolves #637 by addressing the following:
- adjusting the initial bounding box for leaflet on the home landing page
- restoring the link color for the leaflet search control

<img width="759" alt="geoblacklight_issues_637_screenshot_0" src="https://user-images.githubusercontent.com/1443986/43329000-61217f54-918d-11e8-97e0-dae1091457e7.png">


##Repo ID: 25217

##Contributer ID: 164731

##Pull Request ID: 183728

###Profanity Found
**Text**
## description of the issue/feature this pr addresses

linked issue: https://github.com/senaite/senaite.core/issues/483

## current behavior before pr

interim fields were sorted alphabetically after save

## desired behavior after pr is merged

interim fields keep initial sort order

--
i confirm i have tested this pr thoroughly and coded it according to [pep8][1]
and [plone's python styleguide][2] standards.

[1]: https://www.python.org/dev/peps/pep-0008
[2]: https://docs.plone.org/develop/styleguide/python.html


##Repo ID: 22000

##Contributer ID: 168130

##Pull Request ID: 186229

###Profanity Found
**Text**
changes proposed:
  * `resource_daily_stats` - daily stats query for a user/resource
combination
  * `site_daily_stats` - daily stats query for the entire site
  * `resource_range_stats` - date range query for a user/resource
combination
  * `site_range_stats` - date range query for the entire site

@nestorw @lfarrell -- please let me know if these initial queries are a good starting point, if i'm missing any that should be added, etc. i tried to base these on what i'm seeing in the mockups, assuming there might be some front-end manipulation/sorting of the data. so, feedback welcome :smile: 

fixes #2736 

@samvera/hyrax-code-reviewers 


##Repo ID: 22050

##Contributer ID: 81176

##Pull Request ID: 192702

###Profanity Found
**Text**
fixes #2844 

when a new hyrax application is first built, without an initial model built, the rsolr query for the admin dashboard fails by generating an invalid query with the first clause being an empty parens. this fix ensures that the first clause is returned if there are no models in the system, which would be a `nil` in this case. activefedora, that eventually calls the affected method, properly handles when `nil` is returned and structures the resulting query without an empty parens. 

tests included to cover the three scenarios (no models, 1 model, and multiple models).


<img width="1351" alt="screen shot 2018-03-28 at 9 42 25 am" src="https://user-images.githubusercontent.com/32885/38043642-8c0dedf4-326c-11e8-82e0-0fb526a885db.png">


##Repo ID: 22050

##Contributer ID: 171194

##Pull Request ID: 192750

###Profanity Found
**Text**
fixes #2949 

this pr creates a collections javascript utilities class.  the initial motivation is to dry up some code duplication between collections and collections types' edit views, specifically the "add sharing" or "add participants" tab for adding groups and users.

the code here does a few things, and might look bigger than it actually is.  there's a good amount of reorganizing along with new code.

1. creates a `collectionutilities` javascript class, which can be the source for shared modules/classes which encapsulate functionality which collections and collection types need.  the `collectionutilities` class can be imported where it's needed, assuming the importer is an `.es6` file.

2. moves the previous code for handling adding users and groups via ajax when editing a collection or collection type, sharing or participants tab, to the new utility class.

3. moves the previous code for handling the enabled/disabled state of 2.'s "add" buttons to the new utility class. 

4. creates a new es6 file `app/assets/javascripts/hyrax/collections_v2.es6`, which begins a work in progress of eventually replacing the es5 file `app/assets/javascripts/hyrax/collections.js`, so we can take advantage of modularity, code-reuse, this utility class, etc.

5. begins thinning out the `app/assets/javascripts/hyrax/collections.js` file by moving one handler function (for starters) to the new utility class.

6. the collection types js file, `app/assets/javascripts/hyrax/collection_types.es6` might look like a decent amount was modified outside of the additional code, but this is just running it through prettier (https://prettier.io/), to get some consistency. 

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 79509

##Pull Request ID: 192810

###Profanity Found
**Text**
adds `hyrax::permission` and `hyrax::accesscontrollist` as an initial implementation of acls and read/edit/discover grants for objects in valkyrie.

a simple grant/revoke dsl is added to encapsulate the most common practice of granting or revoking a particular access mode for a given user or group.

for now, this is only working against the abstract valkyrie interface; further work is needed to allow the wings adapter to translate the valkyrie native approach to `activefedora`-compatible data/operations.

this moves work forward toward #3584.

changes proposed in this pull request:
* build out low-level infrastructure for valkyrie handling of permissions

guidance for testing, such as acceptance criteria or new user interface behaviors:
* none; impact of this work is limited to internals.

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 193379

###Profanity Found
**Text**
refs https://github.com/samvera-labs/hyku/issues/457

this is the initial update to the styling of the featured works list and recently uploaded list based on the homepage mockups in the above hyku issue.

the outcomes of this pr are:
- [x] consistent styling between the featured and recent list
- [x] updated layout to better present the information
- [x] changes the tab panels to pill panels (in preparation for additional updates) for a more consistent look with the formatted tables of information

*display before*
<img width="1242" alt="screen shot 2017-12-13 at 10 01 48 am" src="https://user-images.githubusercontent.com/2294288/33957511-ac99cc6e-dff6-11e7-9b24-a6d67f9f5ce9.png">

<img width="1238" alt="screen shot 2017-12-13 at 10 01 55 am" src="https://user-images.githubusercontent.com/2294288/33957528-b62ae2e0-dff6-11e7-8ac5-871b07504559.png">

*display after*

<img width="1250" alt="screen shot 2017-12-13 at 9 48 25 am" src="https://user-images.githubusercontent.com/2294288/33957564-d09a8572-dff6-11e7-857c-4631bc607d34.png">

<img width="1242" alt="screen shot 2017-12-13 at 9 48 39 am" src="https://user-images.githubusercontent.com/2294288/33957573-d7adc57c-dff6-11e7-8fd5-ac227e98603a.png">



@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 79487

##Pull Request ID: 192460

###Profanity Found
**Text**
here is an initial attempt following the initial simper suggestion as a solution.

##Repo ID: 22104

##Contributer ID: 85823

##Pull Request ID: 246596

###Profanity Found
**Text**
this is the initial pr for the rest entities functionality.
it contains integration tests and javadocs, but there are still a few things included which will be cleaned up in the future.
a few examples are:
* customizations specific to setting up the demo
* bugfixes in the master which are either already in another pr or not yet in another pr

we will further cleanup these things, but some will be dependent on other merges in the master
don't let this stop you from reviewing the functionality

##Repo ID: 22104

##Contributer ID: 85808

##Pull Request ID: 246604

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-3433
it's quite reasonable that the mail session is not defined in the jndi initial context, or that there is no initial context at all.  don't issue warn messages to the log in these cases as they are not failures -- it is expected that a new session will be created from the dspace configuration.

other name service exceptions are still logged, as they may indicate real problems.

also, the name being looked up is now logged at debug level.

briefly tested on the command line without a context; with a context but no name defined; with a context and a name defined.  currently the logger is not set up by webapp.s until after the session has been retrieved or created, so it's not possible to test in a webapp.

see https://github.com/mwoodiupui/ephemeral-jndi-context for how i rigged up the context while testing.

##Repo ID: 22104

##Contributer ID: 146589

##Pull Request ID: 246605

###Profanity Found
**Text**
removed the http 404 in case users is empty
refactored the async statement so that callbacks aren't called twice in case of error, which was the initial problem

this helped solving the problem: http://stackoverflow.com/questions/27521471/callback-was-already-called-async-parallel

##Repo ID: 25206

##Contributer ID: 177918

##Pull Request ID: 247760

###Profanity Found
**Text**
part of #344 

this is an initial take on tackling #344 and only implements an "open in arcgis online" button for content that is already coming from an esri web service.

this work comes out of discussions at geo4libcamp 2019. thanks so much for help on this from @eliotjordan, @karenmajewicz, @ajturner, @jgravois, and @dmfenton . a more complete implementation will come with details provided in #344, but we wanted to get the initial pieces in front of users for feedback.

![openinarcgis](https://user-images.githubusercontent.com/1656824/52498888-e5aa3b80-2b8e-11e9-8bcc-585a91e7da88.gif)


##Repo ID: 25217

##Contributer ID: 79473

##Pull Request ID: 183800

###Profanity Found
**Text**
(no one doing an initial install should use resque)

@projecthydra-labs/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 79495

##Pull Request ID: 191508

###Profanity Found
**Text**
some initial tests for this custom query; the wings version of this went
untested initiially. i wrote these (uncomprehensive) tests while debugging an
issue that turned out to be unrelated; so here they are.

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 263728

###Profanity Found
**Text**
`_read_messages` calls `connect` over and over again when the connection fails to the gateway websocket. in the case that the kernel no longer exists, this causes an infinite loop without any backoff.

there's several solutions, this is one of them. please let me know if you see any potential problems. eg: is it possible that there's an initial period where this will 404 while the eg is spinning up the kernel and preparing the ws endpoint? hasn't happened to me locally.

##Repo ID: 25237

##Contributer ID: 131855

##Pull Request ID: 280814

###Profanity Found
**Text**
evidence accumulation clustering: eac, an ensemble based clustering framework:
fred, ana ln, and anil k. jain. "data clustering using evidence
    accumulation." pattern recognition, 2002. proceedings. 16th international
    conference on. vol. 4. ieee, 2002.

basic overview of algorithm:
1. cluster the data many times using a clustering algorithm with randomly (within reason) selected parameters.
2. create a co-association matrix, which records the number of times each pair of instances were clustered together.
3. cluster this matrix.

this seems to work really well, like a kernel method, making the clustering "easier" that it was for the original dataset.

the default of the algorithm are setup to follow the defaults used by fred and jain (2002), whereby the clustering in step 1 is k-means with k selected randomly from 10 and 30. the clustering in step 3 is the mst algorithm, which i have yet to implement (will do in this pr).

**after initial feedback,** i think people are happy with the api.

todo:
- [x] mst algorithm from the paper, which was used as the final clusterer. completed in pr #1991 
- [ ] ~~there is an improvement to the speed of the algorithm (don't have the paper on hand) that has been published, that should be incorporated~~ (will be done in a later pr)
- [x] examples/usage
- [x] narrative documentation
- [x] revert test_clustering, line 508, to only check for spectralclustering
- [x] use a sparse matrix for the co-association matrix


##Repo ID: 25240

##Contributer ID: 167622

##Pull Request ID: 223997

###Profanity Found
**Text**
morpheus documentation initial commit


##Repo ID: 25229

##Contributer ID: 81064

##Pull Request ID: 206271

###Profanity Found
**Text**
the initial fork was against ojs:master instead of ojs:ojs-stable-3_1_1, my bad.

##Repo ID: 25226

##Contributer ID: 86405

##Pull Request ID: 199914

###Profanity Found
**Text**
this pull requests includes the results of my initial investigation into ui testing the dataverse project using cypress (see https://github.com/iqss/dataverse/issues/5846 for the overall discussion and https://www.cypress.io/ for a general overview of the tool).

![ezgif com-optimize](https://user-images.githubusercontent.com/395846/58661220-9ba8b980-8327-11e9-8a39-b1f8554f2dea.gif)

some important points to consider regarding the code added in this pr:

- cypress is based on javascript/nodejs and thus requires an installation of `node`. it runs its tests in a browser-instance based on chromium/chrome/electron, depending on the browsers that are installed. cypress can be installed by running `npm install` within `tests/`, and run locally using `npm run cypress:dev` or in ci using `npm run cypress:ci`.
  - cypress is not (yet) usable for cross-browser testing but i think they are working on it.
- cypress is configured with the `cypress.json` file located in `tests/cypress.json`. this "default" configuration can be overridden with environment variables (e.g., in ci):
  - define `cypress_baseurl=https://staging.app.com` to override the default setting. could be useful to point cypress to another instance of dataverse when running in ci.
  - see also https://docs.cypress.io/guides/guides/environment-variables.html#setting
- to setup the integration with the cypress dashboard (see https://www.cypress.io/dashboard/), update `projectid` in `cypress.json` or set it dynamically using environment variable as described above.
  - the dashboard (free for oss) displays screen recordings and other meta information that have been created by cypress when run in ci. the dashboard does not actually execute the tests! 
  - to receive recordings, the ci runner also depends on the `cypress_record_key` environment variable, the value of which is shown when creating the cypress project.
  - for an example of what the dashboard could do, see https://dashboard.cypress.io/#/projects/ufkudc/runs, which displays some of the runs executed when i was developing.
- the dataverse application stack needs to be in pristine state prior to testing, as the ui frameworks expects that the environment is always initialized the same way. naive example: there always needs to be "one notification to be read", which is then marked as read by the ui tests.
  - when running a dataverse instance in ci (`docker-aio` or `dataverse-kubernetes`), this will implicitly be the case, as the instance is spun up separately in each job.
  - when executing against a `phoenix` instance, this needs to be ensured manually, or cleanup api calls need to be added to `beforeeach` in the respective ui tests.
  - see https://docs.cypress.io/guides/references/best-practices.html for best practices in general and regarding this point (the cypress docs are quite good).
- when running ui tests as developed for this pr, one can run into some incompatibilities with the frame busting techniques applied in dataverse. the following line in `dataverse_template.xhtml` would need to be disabled/removed when testing, or refactored in general: 
  - `if (window !== top) top.location = window.location;`

## related issues

- #5846 uzh - ui testing / additional test improvements

## pull request checklist

- [x] unit [tests][] completed
- [x] integration [tests][]: none
- [x] deployment requirements, [sql updates][], [solr updates][], etc.: none
- [x] [documentation][docs] completed
- [x] merged latest from "develop" [branch][] and resolved conflicts

[tests]: http://guides.dataverse.org/en/latest/developers/testing.html
[sql updates]: http://guides.dataverse.org/en/latest/developers/sql-upgrade-scripts.html
[solr updates]: https://github.com/iqss/dataverse/blob/develop/conf/solr/7.3.0/schema.xml
[docs]: http://guides.dataverse.org/en/latest/developers/documentation.html
[branch]: http://guides.dataverse.org/en/latest/developers/branching-strategy.html


##Repo ID: 25213

##Contributer ID: 79644

##Pull Request ID: 182570

###Profanity Found
**Text**
following bootstrap's lead, migrate scss files from px to rem. assuming standard browser 1rem = 16px base.

vertical spacers (margins/paddings) shifted to 1 or half rem increments (ex. 6px to 0.5rem) to standardize vertical rhythm. horizontal spacers converted directly from px to rem (ex. 12px to 0.75rem), except where within 1px to base (ex. 15px to 1rem). hard-coded heights shifted to 16px/per rem closest fit (ex. 450px/16px = 28.125, so 28rem). odd px counts converted to nearest divisible by 4, cuz' 16 base (ex. 5px to 0.25rem).

this is the initial conversion commit. some polishing commits to follow.

##Repo ID: 25217

##Contributer ID: 79968

##Pull Request ID: 183752

###Profanity Found
**Text**
this incorporates an initial valkyrie::rescourcefactory to unblock further work. 

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 193136

###Profanity Found
**Text**
this pull request imports the `fpr` app and remove the bits from `idcommand` that manipulated the workflow data in preparation for the merge of https://github.com/artefactual/archivematica/pull/1251 where the workflow data is removed from the database.

and you may be wondering... why 120k lines of code? well that's just mostly the initial data that we populate to users via fixtures, mostly related to pronom updates!

we'd still need to figure out what's the impact of removing this feature:
- were users relying on it? it's definitely not documented!
- how could we work around it? once #1251 is merged, we could explain how to alter the workflow in according to new identification commands. this could easily be done in the scope of am19.
- what would be a good solution in the long term? e.g. implement a workflow link that can list the identification commands made available via fpr, similar to the link that lists ss locations during aip/dip storage.

my suggestion: merge this, file a new issue to tackle the above.

- connects to https://github.com/archivematica/issues/issues/213
   `problem: fpr app import and writes to main.models`
- connects to https://github.com/archivematica/issues/issues/181
    `problem: it's hard to maintain fpr-admin as a separate repo`

##Repo ID: 25208

##Contributer ID: 79365

##Pull Request ID: 179806

###Profanity Found
**Text**
in active fedora, it assumes quite often that a given object will have
only a single valid content model. with models in the community
starting to extend from other models (ie. sufia or internal models at
bpl), this update makes such cases more sane. note that this
functionality is only for reading of objects.

for the below bulleted examples, i will assume the following two
models:

```
class genericfile << activefedora::base

class extendedgenericfile << genericfile
```
- belongs_to and has_many should automatically cast objects based on
  the base class_name. for example, if one has:
  
  ``````
  ```
  has_many files, class_name: "genericfile"
  ```
  ``````
  
  in this case, "genericfile" objects will still be returned as such.
  but "extendedgenericfile" objects will be instantiated as that
  class. note that only the first cmodel order on the
  "extendedgenericfile" object is not important as it will attempt
  to use the most specific class available.
- adapt_to_cmodel no longer blindly uses the first cmodel. if an object
  of a class other than activefedora::base is called with it, it will
  attempt to find a more specific model based on that base model. if
  no more specific model is found, it will return itself.
  
  otherwise, if the object is loaded of type activefedora::base,
  it will use the first model, and cast as that unless it finds
  a more specific model registered in the system (based on that
  first model it finds).
- as these are read-only support, relationships are not written
  upon creation. so, to best use these, if one instantiates an
  extended cmodel, one should create the cmodel inheritance in
  their own code at some point. to do this, some psuedo-code
  one needs to do during object creation is:
  
  ``````
  ```
  object_superclass = self.class.superclass
  until object_superclass == activefedora::base
  || object_superclass == object do
    add_relationship(:has_model, object_superclass.to_class_uri)
    object_superclass = object_superclass.superclass
  end
  ```
  ``````
  
  it is ideal to place this in overriding "assert_content_model"
  that is only called on initial object creation.
  
  note: this is not needed to use these changes in most cases.
  it only affects locating extended objects in relationships
  defined as their superclass. for example, using the objects
  above, :has_many of type "genericfile" won't find
  "extendedgenericfile" objects without actually persisting this
  inheritence. this is not an issue if one isn't attempting to
  use extended cmodels (ie. rather than extending genericfile
  one simply keeps the same name and overwrites it in their system,
  as is done in wgbh's dam system).


##Repo ID: 22034

##Contributer ID: 81753

##Pull Request ID: 187653

###Profanity Found
**Text**
this pr adds initial mocking with mockito in several places that i found it could be useful.

**important**: the larger test suite depends on a change to **production** code in that the entity manager in `passwordreset/passwordresetservicebean.java` needs to be *protected* instead of *private*. i found that throughout the codebase, it is already often the case that the em is only *protected*, so found it reasonable to change this for improved testability. if you prefer or use any other kind of dependency injection in such cases, i can still amend this. without this production change, we could not unit test or *cleanly* mock anything related to database interactions.

as for the specific changes:
- add a test suite for `passwordreset/passwordresetservicebeantest.java`
  - executes/covers 86% of instructions compared to 0% before the change
  - however, this is only a simple metric and the assertions and evaluations are on a relatively rudimentary level (as far as i got with limited understanding of the entire codebase)
    - for example, the test ensures that an email would have been sent or not sent in the respective cases, or that the returned object correctly includes `ischanged` or `isemailfound`
  - all externalities that are used within the class are mocked
- add initial test suite for `makedatacount/datasetmetricsservicebeantest.java`
  - test different behaviors of `testgetdatasetmetricsbydatasetmonthcountry`
  - the entity manager is already accessible here, so no need for a change

## related issues

- connects to #5796

## pull request checklist

- [x] unit [tests][] completed
- [x] integration [tests][]: none
- [x] deployment requirements, [sql updates][], [solr updates][], etc.: none
- [x] [documentation][docs] completed
- [x] merged latest from "develop" [branch][] and resolved conflicts

##Repo ID: 25213

##Contributer ID: 79644

##Pull Request ID: 182521

###Profanity Found
**Text**
in active fedora, it assumes quite often that a given object will have
only a single valid content model. with models in the community
starting to extend from other models (ie. sufia or internal models at
bpl), this update makes such cases more sane. note that this
functionality is only for reading of objects.

for the below bulleted examples, i will assume the following two
models:

```
class genericfile << activefedora::base

class extendedgenericfile << genericfile
```
- belongs_to and has_many should automatically cast objects based on
  the base class_name. for example, if one has:
  
  ``````
  ```
  has_many files, class_name: "genericfile"
  ```
  ``````
  
  in this case, "genericfile" objects will still be returned as such.
  but "extendedgenericfile" objects will be instantiated as that
  class. note that only the first cmodel order on the
  "extendedgenericfile" object is not important as it will attempt
  to use the most specific class available.
- adapt_to_cmodel no longer blindly uses the first cmodel. if an object
  of a class other than activefedora::base is called with it, it will
  attempt to find a more specific model based on that base model. if
  no more specific model is found, it will return itself.
  
  otherwise, if the object is loaded of type activefedora::base,
  it will use the first model, and cast as that unless it finds
  a more specific model registered in the system (based on that
  first model it finds).
- as these are read-only support, relationships are not written
  upon creation. so, to best use these, if one instantiates an
  extended cmodel, one should create the cmodel inheritance in
  their own code at some point. to do this, some psuedo-code
  one needs to do during object creation is:
  
  ``````
  ```
  object_superclass = self.class.superclass
  until object_superclass == activefedora::base
  || object_superclass == object do
    add_relationship(:has_model, object_superclass.to_class_uri)
    object_superclass = object_superclass.superclass
  end
  ```
  ``````
  
  it is ideal to place this in overriding "assert_content_model"
  that is only called on initial object creation.
  
  note: this is not needed to use these changes in most cases.
  it only affects locating extended objects in relationships
  defined as their superclass. for example, using the objects
  above, :has_many of type "genericfile" won't find
  "extendedgenericfile" objects without actually persisting this
  inheritence. this is not an issue if one isn't attempting to
  use extended cmodels (ie. rather than extending genericfile
  one simply keeps the same name and overwrites it in their system,
  as is done in wgbh's dam system).


##Repo ID: 22034

##Contributer ID: 81753

##Pull Request ID: 187661

###Profanity Found
**Text**
extension modules defined on associations are added to the association proxy itself, but are not propagated to scopes created from that association proxy.  this commit fixes that.

(the two assertions in the test case cover both built-in scope methods such as `where`, `limit`, etc., as well as scopes defined on the target class of the association.  during initial development, i tried a solution that addressed built-in scopes but failed for named scopes on the target class.)


##Repo ID: 1

##Contributer ID: 79981

##Pull Request ID: 178620

###Profanity Found
**Text**
extension modules defined on associations are added to the association proxy itself, but are not propagated to scopes created from that association proxy.  this commit fixes that.

(the two assertions in the test case cover both built-in scope methods such as `where`, `limit`, etc., as well as scopes defined on the target class of the association.  during initial development, i tried a solution that addressed built-in scopes but failed for named scopes on the target class.)


##Repo ID: 1

##Contributer ID: 79981

##Pull Request ID: 178623

###Profanity Found
**Text**
this pr adds some initial unit tests to the following classes/methods:

- `filemetadata.getfiledatetodisplay`
- `dataaccess.createnewstorageio (partial)`
- `filesizechecker.testisallowedfilesize`

i also added and used the testing dependency on `junit.jupiter.params` as described in #5657.

## related issues

- connects to issue #5634 (as well as prs #5642 and #5643)

## pull request checklist

- [x] unit [tests][] completed
- [x] integration [tests][]: none
- [x] deployment requirements, [sql updates][], [solr updates][], etc.: none
- [x] [documentation][docs] completed
- [x] merged latest from "develop" [branch][] and resolved conflicts

##Repo ID: 25213

##Contributer ID: 79644

##Pull Request ID: 182465

###Profanity Found
**Text**
circle ci supports "workflow" pipelines. this is an initial configuration that
breaks our prior circle setup down into a workflow to avoid duplication of
work.

the jobs included in the workflow are as follows:

  - `bundle`: this checks out code and installs the `hyrax` level dependencies.
  the output of this step is cached to avoid duplicating work across workflow
  runs, and persists to the workflow's workspace for use by other jobs within
  this workflow run.
  - `build`: generates the engine cart application for use by the test suite.
  this depends on the `bundle` job. the output also persisted into the
  workspace.
  - `lint`: runs `rubocop`. this is broken into a separate job so it can run in
  parallel with `build`.
  - `test`: runs `rspec` using the output of `bundle` and `build`. this job is
  configured to run in 4x parallelism, and only after `build` and `lint` have
  succeeded.

a next step might be to fan the workflow out further to include build/test
processes covering supported versions of ruby and rails.

this is a ci configuration change, and does not impact any production code.

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 193153

###Profanity Found
**Text**
allows authenticators to set .auth_state from info in the initial authentication.

cc @yuvipanda this is the pr i forgot to open

##Repo ID: 25439

##Contributer ID: 128296

##Pull Request ID: 254277

###Profanity Found
**Text**
since 2013, the initial commit d6868ad, added the endorsed java api.
these days, there is no reference to be found installing the resulting files.
the api was not included in the war file.

## related issues

- #6140

## pull request checklist

- [x] merged latest from "develop" [branch][] and resolved conflicts

[branch]: http://guides.dataverse.org/en/latest/developers/branching-strategy.html


##Repo ID: 25213

##Contributer ID: 79647

##Pull Request ID: 182659

###Profanity Found
**Text**
circle ci supports "workflow" pipelines. this is an initial configuration that
breaks our prior circle setup down into a workflow to avoid duplication of
work.

the jobs included in the workflow are as follows:

  - `bundle`: this checks out code and installs the `hyrax` level dependencies.
  the output of this step is cached to avoid duplicating work across workflow
  runs, and persists to the workflow's workspace for use by other jobs within
  this workflow run.
  - `build`: generates the engine cart application for use by the test suite.
  this depends on the `bundle` job. the output also persisted into the
  workspace.
  - `lint`: runs `rubocop`. this is broken into a separate job so it can run in
  parallel with `build`.
  - `test`: runs `rspec` using the output of `bundle` and `build`. this job is
  configured to run in 4x parallelism, and only after `build` and `lint` have
  succeeded.

a next step might be to fan the workflow out further to include build/test
processes covering supported versions of ruby and rails.

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 193157

###Profanity Found
**Text**
circle ci supports "workflow" pipelines. this is an initial configuration that
breaks our prior circle setup down into a workflow to avoid duplication of
work.

the jobs included in the workflow are as follows:

  - `bundle`: this checks out code and installs the `hyrax` level dependencies.
  the output of this step is cached to avoid duplicating work across workflow
  runs, and persists to the workflow's workspace for use by other jobs within
  this workflow run.
  - `build`: generates the engine cart application for use by the test suite.
  this depends on the `bundle` job. the output also persisted into the
  workspace.
  - `lint`: runs `rubocop`. this is broken into a separate job so it can run in
  parallel with `build`.
  - `test`: runs `rspec` using the output of `bundle` and `build`. this job is
  configured to run in 4x parallelism, and only after `build` and `lint` have
  succeeded.

a next step might be to fan the workflow out further to include build/test
processes covering supported versions of ruby and rails.

@samvera/hyrax-code-reviewers


##Repo ID: 22050

##Contributer ID: 146260

##Pull Request ID: 193158

###Profanity Found
**Text**
i took the time to fix #4796. 

**previous code logic:**
it seems like #765 actually only addressed part of the problem. @marceloramires checked to see if the first range in the list was a selection and assumed that if this was a selection, the others would be selections too. if this was the case, then delete all the text in the selections. this handled deleting multicursor selections.

there was then separate logic that handled the tabbing. this logic was only built to accommodate one cursor, so if it detects a tab, it deletes it, and if it doesn't, it uses the function `deleteh(-1, "char")`, which handles the situation like a normal deletion. normal deletion worked as expected for multicursor, but the tab deletion was only built considering one cursor and specifically deletes the tab for the "primary" cursor, which is the one returned by `cm.getcursor()`.

**updated code logic:**
to fix this, i consider each cursor separately. for each cursor, i first check if it is a selection. if it is, i delete the selection. then i know it's a cursor, so i check to see that all characters on the line that come before it are spaces. if they're all spaces, we use tab delete, otherwise, we only delete one character at a time.

**note on new logic:**
i also want to note that deleting one character at a time is somewhat different from the previous logic. before, even if there was text on the line, it would still use tab logic, so if i have 
```
stuff = 'tabs         |   '
012301230123012301230123
```
this is what backspacing would do
```
stuff = 'tabs       |   '
012301230123012301230123
```
now, it just deletes one character, which is what i found pycharm did, and what i think logically makes sense. if you have spaces after the initial text, they're no longer used for indentation, and you're more likely to care about the specific number of spaces (which deleting would make unclear). if anything, i can put tab deletion back in, but i think it should consistently be 4 spaces rather than to the nearest tabstop, which would seem random unless you're counting all the characters in the line each time you hit delete.

if all this looks good, i'm ready to merge!


##Repo ID: 25237

##Contributer ID: 181021

##Pull Request ID: 221840

###Profanity Found
**Text**
it seems that the current purge scripts are quite old. there are some incompatibilities. for example getlocalfileinfo($info) function wants 'zip' paprameter, but we don't have it, because all file names are just hashes. so it means we need a modified getlocalfileinfo function that doesn't use 'zip' parameter in query?

there was a 'todo' mentioning to use sscan when it will be available in phpredis. now phpredis supports getting multiple results with spop. what was the initial behind sscan? performance?

##Repo ID: 22064

##Contributer ID: 85223

##Pull Request ID: 218926

###Profanity Found
**Text**
this proposal is based on https://github.com/jupyter/jupyter_client/pull/348.

this proposal defines the logic for creating new zmq connection without closing existing websocket connection if a kernel was restarted with new ports (e.g. when the kernel is not responding during initial startup).
the following changes were added to the `on_kernel_restarted` function:
- `kwargs` support
- `newports` parameter from `kwargs` used if it is defined. if the parameter is not in `kwargs` set it to `false`
- if `newports == true` then existing zmq connection to the kernel is closed and new stream with updated ports is opened.
- if `newports == false` then client is notified that the kernel was restarted
this proposal solves the issue described in https://github.com/jupyter/jupyter_client/issues/347

##Repo ID: 25237

##Contributer ID: 128672

##Pull Request ID: 221472

###Profanity Found
**Text**
this is the same as https://github.com/jupyter/notebook/pull/4804, but i moved it over to it's own branch instead of master. use this one.

copied from https://github.com/jupyter/notebook/pull/4804:
i took the time to fix #4796.

previous code logic:
it seems like #765 actually only addressed part of the problem. @marceloramires checked to see if the first range in the list was a selection and assumed that if this was a selection, the others would be selections too. if this was the case, then delete all the text in the selections. this handled deleting multicursor selections.

there was then separate logic that handled the tabbing. this logic was only built to accommodate one cursor, so if it detects a tab, it deletes it, and if it doesn't, it uses the function deleteh(-1, "char"), which handles the situation like a normal deletion. normal deletion worked as expected for multicursor, but the tab deletion was only built considering one cursor and specifically deletes the tab for the "primary" cursor, which is the one returned by cm.getcursor().

updated code logic:
to fix this, i consider each cursor separately. for each cursor, i first check if it is a selection. if it is, i delete the selection. then i know it's a cursor, so i check to see that all characters on the line that come before it are spaces. if they're all spaces, we use tab delete, otherwise, we only delete one character at a time.

note on new logic:
i also want to note that deleting one character at a time is somewhat different from the previous logic. before, even if there was text on the line, it would still use tab logic, so if i have

stuff = 'tabs         |   '
012301230123012301230123

this is what backspacing would do

stuff = 'tabs       |   '
012301230123012301230123

now, it just deletes one character, which is what i found pycharm did, and what i think logically makes sense. if you have spaces after the initial text, they're no longer used for indentation, and you're more likely to care about the specific number of spaces (which deleting would make unclear). if anything, i can put tab deletion back in, but i think it should consistently be 4 spaces rather than to the nearest tabstop, which would seem random unless you're counting all the characters in the line each time you hit delete.

if all this looks good, i'm ready to merge!

##Repo ID: 25237

##Contributer ID: 181021

##Pull Request ID: 221851

###Profanity Found
**Text**
a recent change broke the ability to add a new processing configuration because it was trying to load from disk when the name of the config was `none` which always returned a 404 as a reaction to `ioerror`. in this commit, the form is rendered without initial data when `name` equals `none`.

connects to https://github.com/archivematica/issues/issues/242.

##Repo ID: 25208

##Contributer ID: 79365

##Pull Request ID: 179770

###Profanity Found
**Text**
## description of the issue/feature this pr addresses

**depends on: [pr #1026 removed auto-digest of results reports on verify transitions](https://github.com/senaite/senaite.core/pull/1026)**

actually, there are two different transitions binded to analysis request workflow with similar ids that are confusing:
- `retract` (title "retract"): this transition is available before analysis request being verified. this transition retracts all the active, not yet verified, analyses from the ar. 
- `retract_ar` (title "invalidate"): this transition is only available when analysis request status is `verified` or `published`. this transition leaves the analysis request to an `invalid` state, generates a copy of the analysis request (retest) with same analyses, but in `to_be_verified` state. a relationship between both is established thanks to `parentanalysisrequest` and `childanalysisrequest` fields. also, if the initial status was `published`, an e-mail to labman and client is sent.

with this pull request, the following actions have been achieved:
- `retract_ar` transition id becomes `invalidate`
- field `parentanalysisrequest` is renamed to `invalidated` to avoid confusions
- field `childanalysisrequest` is renamed to `retest` to avoid confusions

**side note**
at the moment, these two fields are still rendered in the view thanks to `get_custom_fields`, but will be ported to the `header_table` in a new `header_table` refactoring that is under progress

## current behavior before pr

`retract_ar` transition and fields used to store the relationship amongst retests and invalidated are confusing.

## desired behavior after pr is merged

`retract_ar` is replaced by `invalidate` and fields `parentanalysisrequest` and `childanalysisrequest` are replaced by `invalidated` and `retest`.

--
i confirm i have tested this pr thoroughly and coded it according to [pep8][1]
and [plone's python styleguide][2] standards.

[1]: https://www.python.org/dev/peps/pep-0008
[2]: https://docs.plone.org/develop/styleguide/python.html


##Repo ID: 22000

##Contributer ID: 168182

##Pull Request ID: 186366

###Profanity Found
**Text**
closes #1686 

with the initial window state as updated in this pr:

<img width="500" alt="mirador-screenshot" src="https://user-images.githubusercontent.com/96776/51776011-6d327d80-20ac-11e9-9219-93221a5c7177.png">


##Repo ID: 25222

##Contributer ID: 79472

##Pull Request ID: 184980

###Profanity Found
**Text**
this pr removes the code related to the quarantine feature.

i've recorded how the workflow looks in `qa/1.x` with the quarantine feature and how it looks now in this https://github.com/artefactual/archivematica/issues/598#issuecomment-567388848 and added links to svg files which hopefully will make reviewing this easier.

the initial commit in this pr was rebased from @sevein's branch: https://github.com/artefactual/archivematica/tree/dev/issue-598-remove-quarantine

connected to https://github.com/artefactual/archivematica/issues/598

##Repo ID: 25208

##Contributer ID: 79378

##Pull Request ID: 263146

###Profanity Found
**Text**
![overlapping windows](https://user-images.githubusercontent.com/145874/52032559-4920d300-24d6-11e9-8b6d-04e8933be571.gif)

[netlify demo](https://deploy-preview-1759--mirador-dev.netlify.com/__tests__/integration/mirador/)

this pr implements an overlapping windowing system using react-rnd, which includes some of the same dependencies as react-grid-layout. it allows dragging and resizing of windows, and should allow us to implement grid-like behaviour on top of it in the future. it also registers the position and size of windows in the redux store as they update, allowing us to query the workspace for windows intersecting with the workspace viewport boundary, in response to which we would then pan (or "expand") the workspace.

because it uses a more complete library, this pr doesn't have the bugs of the previous overlapping spike pr i put in, so there shouldn't be any jitter while dragging; the window should stick to the initial mouse position.

still needs to implement zindex updating for the focused window.

##Repo ID: 25222

##Contributer ID: 80391

##Pull Request ID: 185005

###Profanity Found
**Text**
## description of the issue/feature this pr addresses

this pr enhances the id server machinery to support suffixes in samples (ars) to mimic the behavior of senaite versions < 1.3.0 with the `-r01` suffix of the initial ar, and the consecutive `-rnn` suffixes for the retested ars. 

the introduced behavior keeps now for retests the *base id* of the invalidated ar. the *base id* is the id without the suffix (aka the sample id). therefore it will work even for ars introduced in senaite < 1.3.0.

the following **new** variables are supported now for the type `analysisrequestretest`:

- `parent_ar_id`: the original id of the invalidated ar, e.g. `water-0001-r01`
- `parent_base_id`: the *base id* (aka the sample id) with the suffix removed, e.g. `water-0001`
- `retest_count`: the current retest count, e.g. 1 for the first invalidation
- `test_count`: the total number of tests (initial test + retests) or just the number of retests + 1

a full (advanced) configuration would look like this:

```json
[
  {
    "form": "{sampletype}-{year}-{seq:04d}-r01",
    "portal_type": "analysisrequest",
    "prefix": "analysisrequest",
    "sequence_type": "generated",
    "split_length": 2,
  }, {
    "form": "{parent_base_id}-r{test_count:02d}",
    "portal_type": "analysisrequestretest",
    "prefix": "analysisrequestretest",
    "sequence_type": "",
  },
]
``` 

the following **new** variables are supported now for the type `analysisrequestpartition`:

- `parent_ar_id`:  the original id of the parent ar, e.g. `water-0001-r01`
- `parent_base_id`: the "base" id with the suffix removed of the parent ar
- `partition_count`: the current number of created partitions

a full (advanced) configuration would look like this:

```json
[
  {
    "form": "{sampletype}-{year}-{seq:04d}-r01",
    "portal_type": "analysisrequest",
    "prefix": "analysisrequest",
    "sequence_type": "generated",
    "split_length": 2,
  }, {
    "form": "{parent_base_id}-r{test_count:02d}",
    "portal_type": "analysisrequestretest",
    "prefix": "analysisrequestretest",
    "sequence_type": "",
  }, {
    "form": "{parent_ar_id}-p{partition_count:02d}",
    "portal_type": "analysisrequestpartition",
    "prefix": "analysisrequestpartition",
    "sequence_type": "",
  },
]
``` 

also see here for further information:
https://github.com/senaite/senaite.core/pull/1228

## current behavior before pr

sample suffix not supported

## desired behavior after pr is merged

sample suffix supported

--
i confirm i have tested this pr thoroughly and coded it according to [pep8][1]
and [plone's python styleguide][2] standards.

[1]: https://www.python.org/dev/peps/pep-0008
[2]: https://docs.plone.org/develop/styleguide/python.html


##Repo ID: 22000

##Contributer ID: 168130

##Pull Request ID: 186542

###Profanity Found
**Text**
…display basic manifest level metadata.

closes #1583 

![info-panel-toggle](https://user-images.githubusercontent.com/96776/52093064-b97b3300-256e-11e9-8b9a-e75ee565f890.gif)


## open questions/todos
- [x] should we close the sidebar panel when the sidebar menu is closed?
- [x] apply active state on the icon in the side bar
- [x] should i consider splitting out any container vs. presentational components?
- [x] apply initial basic styling / markup
- [x] ~~address any initial a11y considerations~~ (deal w/ this later)
- [x] ~~is there a way to accomplish the design goals (not changing aspect ratio of image but also not overlay the image), or can we spin that off into a separate ticket?~~ (out of scope for this ticket)
- [x] spin out canvas level metadata work to a new ticket (#1780)

##Repo ID: 25222

##Contributer ID: 79472

##Pull Request ID: 185006

###Profanity Found
**Text**
this pr enables a fulltext search of all linked pdfs.

it is an initial implementation skeleton, where work can be started from.

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 196421

###Profanity Found
**Text**
enable creation of versions from existing 

**jira ticket**: https://jira.duraspace.org/browse/fcrepo-2617

# what does this pull request do?
allows for creation of mementos of containers and binaries from the existing version of a resource.

# what's new?
* updates fedoraversioning endpoints for use creating mementos from existing resource contents.
* adds memento datetime header to responses when retrieving memento
* adds methods to fedoraresource for getting a resources memento datetime and determining if a resource is a memento
* adds integration tests for creating mementos
* pr includes initial implementation of creating historical mementos from the request body, but this will potentially change in future work

# how should this be tested?

`fedoraversioningit` documents and tests this feature, but it can also be used via curl:

```
# create versioned container
curl -xpost -h "slug: versioned_container1" -h "link: <http://mementoweb.org/ns#originalresource>; rel=\"type\"" http://localhost:8080/rest/ -h "content-type: text/n3" --data-binary "<> <info:fedora/test/field> \"original\""

# create memento of current state of container
curl -xpost http://localhost:8080/rest/versioned_container1/fcr:versions

# retrieve memento
curl <url from response body of previous request>


# create versioned binary
curl -xpost -h "slug: versioned_bin1" -h "link: <http://mementoweb.org/ns#originalresource>; rel=\"type\"" http://localhost:8080/rest/ -h "content-type: application/octet-stream" --data-binary "binarycontent"

# create memento of current state of container
curl -xpost http://localhost:8080/rest/versioned_bin1/fcr:versions

# retrieve memento
curl <url from response body of previous request>
```

# additional notes:
* it is only suggested to interact with these changes via fedoraversioning endpoints, the interface of versionservice may change.
* binaries cannot be versioned separately from their descriptions in this pr
* usage of modeshape copy method is temporary.
* a number of private/protected methods were moved from fedoraldp to contentexposingresource in order to make it available to fedoraversioning.

##Repo ID: 25216

##Contributer ID: 79825

##Pull Request ID: 251869

###Profanity Found
**Text**
**what this pr does / why we need it**: this pr supports direct uploads to s3 using presigned urls

**which issue(s) this pr closes**:  

closes #6489 

**special notes for your reviewer**: this pr builds on #6488. it could be modified to work independent of multiple stores, but that's not how it was developed and i suspect multiple stores will be merged before this. as of now, this branch is up to date with dev plus #6488.

 the initial state of the pr bypasses all ingest processing for direct uploads. i'll be adding that back in. up to you guys if you want to test prior to that. also owe some documentation.

**suggestions on how to test this**:
once a store is configured to do direct uploads via a jvm option, the store should work as normal w.r.t. user interface uploads. testing should probably focus on making sure that's true. once the pr is updated to support ingest processes, testing could check that the processing is the same between a normal store and a direct upload one.
there will also be a version of the dvuploader that can use the direct upload capability when a store supports it (next pr). that could be used to test the api calls directly.
performance would be nice to test as well - overall speed and max file size.

**does this pr introduce a user interface change?**:
none beyond that in #6488. that said, some elements, like the upload progress bar are being controlled via javascript rather than by primefaces when direct upload is used, so there could be some unintentional/minor style differences (something else to test...).

**is there a release notes update needed for this change?**:
could be worth mentioning, but everything beyond #6488 is optional, so there are no required upgrade steps.

**additional documentation**:


##Repo ID: 25213

##Contributer ID: 79629

##Pull Request ID: 262903

###Profanity Found
**Text**
the current cd algorithm breaks when the dual gap if the biggest coordinate update is less than tolerance. glmnet however checks if the max change in the objective is less than tol and then breaks. this surprisingly leads to huge changes in speedup with almost no noticeable regression in prediction.

it states that, each inner coordinate-descent loop continues until the maximum change in the objective after any coefficient update is less than thresh times the null deviance.

it should be noted that the default tolerance in this case is 1e-7

some initial benchmarks using `lassocv` and `precompute=false`.

for the newsgroup dataset (using two categories), 5 random splits. (1174 x 130107), test_size = 2/3 of total size.

```
in this branch (using tol=1e-7)
mean_time = 16.6982872009
mean_accuracy_score = 0.89587628866
in master (using tol=1e-4)
mean_time = 236.406961584
mean_accuracy_score = 0.889175257732
```

for the haxby dataset with the mask, using 5 random splits, (216 x 577)

```
in this branch (using tol=1e-7)
mean_time = 0.495861053467
mean_accuracy_score = 0.958333333333
in master (using tol=1e-4)
mean_time = 3.05996584892
mean_accuracy_score = 0.930555555556
```

for the arcene dataset, (100 \* 10000)

```
in this branch (using tol=1e-7)
mean_time = 4.69407510757
accuracy_score on test data = 0.68
in master (using tol=1e-7)
mean_time = 57.34074401860.68
accuracy_score on test data = 0.68
```

for the duke dataset, 5 random splits

```
in master
mean_accuracy_score = 0.84000000000000008
mean_time = 3.316893196105957
in this branch
mean_accuracy_score = 0.82666666666666655
mean_time = 1.2530781269073485
```

since the default tolerances are different, how do we accomodate this change in terms of api. do we need a new stopping criteria called "glmnet?".


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225127

###Profanity Found
**Text**
fixes https://github.com/scikit-learn/scikit-learn/issues/2690

the design is similar to the java code written here https://code.google.com/p/jbirch/
i am pretty much sure it works (if the java implementation is correct, ofc), since i get the same clusters for both cases. i opened this as a proof of concept.

this example has been modified, http://scikit-learn.org/stable/auto_examples/cluster/plot_mini_batch_kmeans.html

when `threshold` is set to 3.0

![figure_1](https://cloud.githubusercontent.com/assets/1867024/4772737/1dd8604a-5b9b-11e4-800d-aea031410a30.png)

when `threshold` is set to 1.0

![figure_2](https://cloud.githubusercontent.com/assets/1867024/4772748/2e46daec-5b9b-11e4-8f49-672b0ada17b7.png)

todo: a lot
- [x] make it as fast as possible.
- [x] support for sparse matrices.
- [x] extensive testing.
- [x] make the common tests pass, for now i have added it to `dont_test` ;)
- [x] narrative documentation

awating some initial feedback!


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225183

###Profanity Found
**Text**
very initial implementation of linearsvr using liblinear's code (which was always available, we just did not use it). still lacking tests and documentation.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225226

###Profanity Found
**Text**
in `gaussiannb.partial_fit`, when there is a mismatch between the target labels (or classes) `y` and the `classes` argument, a `keyerror` was raised while attempting to access the `class2idx` ( refactored to `class_to_index` for readability ) with the mismatching key.

sample code that reproduces this `keyerror`
`gnb.partial_fit(x = [[1,2], [-2,2]], y = [1,2], classes = [0,1])`
- now a `valueerror` with a message explaining that is raised.
  `valueerror: the target label in y does not exist in the initial classes argument, classes=[0, 1]; the conflicting target label is 2`
- added nrt to test the same.

@gaelvaroquaux could you take a look at this?


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225273

###Profanity Found
**Text**
initial early crack at the rest of the ensembles carrying on from #3961 

my biggest question is how (or if) to handle `class_weight='subsample'` in `gradientboostingclassifier`. in `randomforestclassifier`, i weighted based on the bootstrap sample as i have done in `baggingclassifier` in this pr. but the applicability to gbm is not so clear to me. right now i simply use the 'auto' weighting as a initialization of the sample weights, as the fit `sample_weight` param does right now, and as is implemented in `adaboostclassifier` in this pr. my initial thought for 'subsample' was to fit the residuals to the re-weighted boosting `sample_weight` while not actually altering it and letting the iterations do their things, but i feel that we may be venturing far away from the literature there...

any thoughts?

additionally, i'm certain travis will be upset with me on the infamous `check_class_weight_classifiers` in `estimator_checks`. gbm may get by from the hack here: https://github.com/scikit-learn/scikit-learn/pull/3961#discussion-diff-22450369 but the two meta estimators do not call `min_weight_fraction_leaf` directly and are sure to fail. as one solution, i could add another bandaid to check if the estimator has `base_estimator` and set a decision tree with a similar bias against lightly weighted leaf nodes. 

will add individual estimator checks on top of this soon, of course.

calling the previous reviewers for input: @glouppe @amueller @gaelvaroquaux , plus any of you other fine people who are willing to comment :-)


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225385

###Profanity Found
**Text**
`v0 = random_state.rand(m.shape[0])` leads to an initial residual vector in arpack which is all positive. however, this is not the absolute or squared residual, but a true difference. thus, it is better to initialize with `randn` to have an equally distributed sign.

the effect of the previous initialization is that eigsh frequently does not converge to the correct eigenvalues, e.g. negative eigenvalues for s.p.d. matrix, which leads to an incorrect null-space.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 225869

###Profanity Found
**Text**
required for initial setup and analysis of the tool so that it can be used extensively later for some symptom report collection.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226459

###Profanity Found
**Text**
here's initial version of decision tree plot function (#6261). 
tell me what you think and i'll add all docs then. also i am thinking about adding `matplotlib` plotting to this function.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226622

###Profanity Found
**Text**
## adding mean absolute error criteria to `tree.decisiontreeregressor`

sorry for the long silence, the past few weeks have been busy with the start of a new quarter. things have settled down, though, and i'm ready to resume contributions.
i spent the past few days reading through and trying to get a handle on the `tree` module, and i've begun looking into implementing the mean absolute error (mae) split criterion into the decisiontreeregressor. i'm creating this wip pr to provide a public ground for discussion about the code; i believe that feedback early, fail fast would help maximize the amount of learning i can gain from this pr to apply toward future contributions.

here's a task list of sub-objectives (that i see) to complete:
- [x] override `node_value` method to calculate the median
- i have an initial version of `node_value` in my initial commit, please let me know if i'm on the right track / if there are things i should fix or can improve in functional correctness, efficiency, and style.
- [x] update `node_impurity` to return the mean absolute error
- [x] write the `children_impurity` method

i've never used c / c++ before, so i've been learning and experimenting with c and cython as well. if you see a segment of code that looks incorrect, please point it out! i'm looking forward to learning more about cython and c through this pr.

thanks!


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226766

###Profanity Found
**Text**
### referenced issues

this pr comes to fix #3550 and #5774. it's similar to pr #3758, which seems to be abandoned.

**important note**: my development files `hack-dev/*` would be removed before merging this pr.
### explanations

from the comments in the pr #3758, this pr improves the documentation of the parameter `alpha`, deprecates it for `labelpropagation` and fix the label clamping (the credit is all to @musically-ut).

from [1] and [3], we can see that `labelpropagation` doesn't have a clamping factor. in the case of `labelspreading`, from [2] and [3] we have 

![image](https://cloud.githubusercontent.com/assets/1699905/14866129/5dae176c-0cc2-11e6-985a-c9d4630e8f41.png)

which means that `alpha = 0` keeps the initial label information `ŷ(0)`. as suggested by @amueller in #3758, this should be the only possible value for `labelpropagation`.

in the current implementation, [line 239](https://github.com/scikit-learn/scikit-learn/blob/78a674875e30417afe9621346ba022834c138351/sklearn/semi_supervised/label_propagation.py#l239), `alpha = 0` would not propagate label information to the unlabeled instances, but would propagate label information to the labeled instances. i saw this exact behavior with my data, but i couldn't find yet a simple test case to catch it.
### some additional comments

in #5774, @musically-ut discussed a very important point about the current implementation, the graph construction. there is no mention about directed graphs in the referenced papers, but it's what the current implementation does ([line 137](https://github.com/scikit-learn/scikit-learn/blob/78a674875e30417afe9621346ba022834c138351/sklearn/semi_supervised/label_propagation.py#l137)). maybe a specific issue should be created for this.
### referenced papers

[1] zhu, xiaojin, and zoubin ghahramani. learning from labeled and unlabeled data with label propagation. technical report cmu-cald-02-107, carnegie mellon university, 2002.
[2] zhou, dengyong, et al. "learning with local and global consistency." advances in neural information processing systems 16.16 (2004): 321-328.
[3] bengio, yoshua, olivier delalleau, and nicolas le roux. "label propagation and quadratic criterion." semi-supervised learning (2006): 193-216.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226797

###Profanity Found
**Text**
#### reference issue

fixes #6740
#### what does this implement/fix? explain your changes.

subtract x_means from initial centroids iff it's also subtracted from x
#### any other comments?

the bug happens when x is sparse and initial cluster centroids are given. in this case the means of each of x's columns are computed and subtracted from init for no reason.

to reproduce:

``` py
import numpy as np
import scipy
from sklearn.cluster import kmeans
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data

# get a local optimum
centers = kmeans(n_clusters=3).fit(x).cluster_centers_

# fit starting from a local optimum shouldn't change the solution
np.testing.assert_allclose(
    centers,
    kmeans(n_clusters=3, init=centers, n_init=1).fit(x).cluster_centers_
)

# the same should be true when x is sparse, but wasn't before the bug fix
x_sparse = scipy.sparse.csr_matrix(x)
np.testing.assert_allclose(
    centers,
    kmeans(n_clusters=3, init=centers, n_init=1).fit(x_sparse).cluster_centers_
)
```


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226803

###Profanity Found
**Text**
#### reference issue

see #6675 
#### what does this implement/fix? explain your changes.

implement boxcox transform. the current approach is apply univariate on each feature with lambda being evaluated for maximising the log likelihood
#### any other comments?

this is just my initial attempt and am not sure if it is supposed to be computed in this manner. the documentation and tests need to be made better but first wanted to ask if this the expected functionality. please do give any suggestions on improving this. thanks.

<!-- reviewable:start -->

---

this change is [<img src="https://reviewable.io/review_button.svg" height="34" align="absmiddle" alt="reviewable"/>](https://reviewable.io/reviews/scikit-learn/scikit-learn/6781)

<!-- reviewable:end -->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226825

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#contributing-pull-requests
-->
#### reference issue

none, but andy referenced this in his initial email i believe. 
#### what does this implement/fix? explain your changes.

updates info about the mailing list from the old sourceforge one to the new python one.
#### any other comments?

there are still lots of people posting on the old one instead of the new one, should we tell them to move the conversation to the new one?

<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 226840

###Profanity Found
**Text**
this pr fixes the negative value of the lower bound (`-np.infty`) of the gaussianmixture to ensure the lower bound differences between each iterations is always positive. 

in practice, it doesn't change the results of the gaussian mixture.

the only way to add a test for that is to store the useless difference of lower bound between two iterations. as the sign of the initial lower bound value does not change the result, i think it's not add a test for that.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227041

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#contributing-pull-requests
-->
#### reference issue

<!-- example: fixes #1234 -->
#### what does this implement/fix? explain your changes.

current implementation of pa requires the step size (c) to be same across all fit()/partial_fit()
the changes allow to vary the value of c per call of fit()/partial_fit(). 

use case : google's priority inbox paper uses this to incorporate user feedback. 
[google_prioroty_inbox.pdf](https://github.com/scikit-learn/scikit-learn/files/456577/google_prioroty_inbox.pdf)

"in practice, we abuse c by adjusting it per mail to represent our confidence in the label, e.g. a manual correction by a user is given a higher value of c. user models also have higher c than the global model, and new user models have higher values still to promote initial learning."
#### any other comments?

<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227126

###Profanity Found
**Text**
fixes the regression described in #5988. #6089, and the initial patch here, were incorrect. ~~replaces #6089. this is #6089 rebased with an error context manager.~~


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227186

###Profanity Found
**Text**
#### reference issue

issue [3298](https://github.com/scikit-learn/scikit-learn/issues/3298)
#### what does this implement/fix? explain your changes.

incorporates roc auc computations for some multiclass roc auc algorithms:
- hand & till, 2001 one vs one
- provost & domingo, 2000 one vs rest
#### any other comments?

i wanted to just get in an initial pr for this issue because i am sure there will be many modifications/suggestions from everyone.

_todos_
- [x] i haven't implemented comprehensive testing for edge cases yet. i've added a few short tests to assess correctness of the different algorithms, but would also like more feedback on this specific area.
- [x] updating documentation
- [x] pep8!
- [x] check compatibility for different versions of python & packages supported by sklearn. (e.g. one failure was with numpy: `typeerror: unique() got an unexpected keyword argument 'return_counts'`)


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227308

###Profanity Found
**Text**
in #7654 i discovered that a yield test was not being run by nosetests because it was wrapped in skip_if_32bit. 

previously 
`nosetests sklearn.ensemble.tests.test_forest:test_importances --verbose` would output 

```
sklearn.ensemble.tests.test_forest.test_importances ... ok
----------------------------------------------------------------------
ran 1 test in 0.000s
ok
```

however, this success was simply because nothing was being run. 

with the change all 10 of the tests embeded in this one function are run. unfortunately they are all failing. 

```
(venv2) joncrall@hyrule:~/code/scikit-learn$ nosetests sklearn.ensemble.tests.test_forest:test_importances --verbose
sklearn.ensemble.tests.test_forest.test_importances('extratreesclassifier', 'gini', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('extratreesclassifier', 'entropy', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('randomforestclassifier', 'gini', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('randomforestclassifier', 'entropy', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'friedman_mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'mae', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'friedman_mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail
sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'mae', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 , ... fail

======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('extratreesclassifier', 'gini', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('extratreesclassifier', 'entropy', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('randomforestclassifier', 'gini', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('randomforestclassifier', 'entropy', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'friedman_mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('extratreesregressor', 'mae', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'friedman_mse', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


======================================================================
fail: sklearn.ensemble.tests.test_forest.test_importances('randomforestregressor', 'mae', array([[ 0.31727627,  1.05972592, -0.1446832 , ...,  0.5589773 ,
----------------------------------------------------------------------
traceback (most recent call last):
  file "/home/joncrall/venv2/local/lib/python2.7/site-packages/nose/case.py", line 197, in runtest
    self.test(*self.arg)
  file "/home/joncrall/code/scikit-learn/sklearn/ensemble/tests/test_forest.py", line 209, in check_importances
    assert_equal(n_important, 3)
assertionerror: 2 != 3
    '2 != 3' = '%s != %s' % (safe_repr(2), safe_repr(3))
    '2 != 3' = self._formatmessage('2 != 3', '2 != 3')
>>  raise self.failureexception('2 != 3')


----------------------------------------------------------------------
ran 10 tests in 1.109s

failed (failures=10)
```

what i did to fix the initial problem was in `skip_if_32bit` i checked if the input function was a generator. 
if it was not then the function runs like it used to. if it is a generator i create a different wrapper that re-yields the results if the function is enabled and yields functions that raise skiptest errors if the function is disabled. 

i also raised notimplemented errors in other wrappers if a generator function is passed in.  


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227302

###Profanity Found
**Text**
#### reference issue
fixes #7744

#### what does this implement/fix? explain your changes.
this pr modifies common tests to catch convergence warnings and assert them. this is done since `max_iter` of estimators is deliberately set low to ensure fast execution.

#### any other comments?
@amueller i wasn't sure what needed to be done exactly but this happens now:

```
$ nosetests --traverse-namespace utils/tests/test_estimator_checks.py
..
----------------------------------------------------------------------
ran 2 tests in 2.872s

ok
```

as opposed to initial situation (current master) where:

```
$ nosetests --traverse-namespace utils/tests/test_estimator_checks.py
/home/karan/documents/scikit-learn/sklearn/linear_model/coordinate_descent.py:1739: userwarning: objective did not converge, you might want to increase the number of iterations
  warnings.warn('objective did not converge, you might want'
/home/karan/documents/scikit-learn/sklearn/linear_model/coordinate_descent.py:1739: userwarning: objective did not converge, you might want to increase the number of iterations
  warnings.warn('objective did not converge, you might want'
/home/karan/documents/scikit-learn/sklearn/linear_model/coordinate_descent.py:1739: userwarning: objective did not converge, you might want to increase the number of iterations
  warnings.warn('objective did not converge, you might want'
..
----------------------------------------------------------------------
ran 2 tests in 2.237s

ok
```


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227381

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#contributing-pull-requests
-->
#### reference issue
fixes #7908 


#### what does this implement/fix? explain your changes.
on the first iteration of ransac regression, if no inliers are found, an error is produced and the code is stopped.  ideally the procedure would just skip that iteration and continue on to the next iteration where it would use a different random sample which could produce valid inliers.

generally this error is produced when `n_inliers_subset` and `n_inliers_best` are both zero. my fix was to set the initial value for `n_inliers_best` to 1.  thus if `n_inliers_subset >= 1`, the code follows the normal path, and if `n_inliers_subset == 0`, the code progresses to the next iteration. this fixes the bug as described in this issue.

however, setting `n_inliers_best = 1` creates an issue again in the first iteration of this loop in the case when `n_inliers_subset == 1`. the subsequent comparison is made: `score_subset < score_best`. since `score_best` is initialized to `np.inf`, the code will incorrectly skip to the next iteration, ignoring the fact that in the first iteration, we did find valid inliers.  the fix for this is to change the initial value of `score_best` to `-np.inf`.  in general, i think this is better practice when initializing these types of variables anyway.

#### any other comments?


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->



##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227446

###Profanity Found
**Text**
this provides an alternative method for calculating feature importances for random forests, by means of a permutation test. this test was described in the initial random forest paper [1], and codified in subsequent literature [2]. we based this work in part on the work done in a previous pull request #3436, but opted to start a new pull request as our implementation differs substantially, and uses somewhat different methodology in performing the actual permutation test (we could not verify the method used in #3436 anywhere in the literature).

relevant to issue #6024, which is requesting permutation importances specifically for the randomforestclassifier - but also makes the point that permutation importances could be applied more generally to classifiers/regressors.

**references**
.. [1] l. breiman, "random forests", machine learning, 45(1), 5-32, 2001.
.. [2] jerome paul and pierre dupont, "inferring statistically significant features from random forests", neurocomputing, 150, part b:471–480, 2015.

#### outstanding issues
- [ ] **no support for randomforestregressor**
-- regression would require a different accuracy metric. r^2 score is one option, but we should consider which metric to use as default, and if we want to support alternative accuracy metrics for permutation importance calculations.
- [ ] **no support multiple outputs**
-- this is easy enough to rectify, but we will need to decide how to handle aggregate accuracy over multiple outputs. one way to do this might be a simple average over all outputs. should consider how this aggregation might interact with other accuracy metrics, if we choose to support other options.
- [ ] **no support for class/sample weights**
-- this implementation does not currently account for class weights or sample weights in calculating feature importances. this may be desirable, but it seems more sensible to use the same weights that were used to train the forest. need to do a quick literature search on this, happy to accept comments if anyone else has an opinion.
- [ ] **use of static methods for helper functions**
-- we opted to implement a number of helper functions as static methods on the forestclassifier class in order to make the code more readable and avoid repeated code (i.e., `_get_oob_data`, `_predict_oob`, `_calc_mislabel_rate`). this doesn't seem like standard practice, so any advice on the preferred method for doing this would be appreciated.
- [ ] **use of _feature_importances at the tree level**
-- the changes made to the basedecisiontree are a bit of a hack, but were necessary to ensure that the feature importances reported by the tree are self-consistent with those calculated at the forest level (e.g., for the std bars reported in the example we added). we could also accomplish this by moving the permutation test logic into the tree itself, but the trees being aware of the out-of-bag sampling seems wrong as well. suggestions definitely welcome here.

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227512

###Profanity Found
**Text**
missingindicator transformer for the missing values indicator mask.
see #6556 

#### what does this implement/fix? explain your changes.
the current implementation returns a indicator mask for the missing values.

#### any other comments?
it is a very initial attempt and currently no tests are present. please do have a look and give suggestions on the design. thanks !

- [x] implementation
- [x] documentation
- [x] tests

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227536

###Profanity Found
**Text**
#### reference issue
this is start of work to address the issues in #78 #7574

#### what does this implement/fix? explain your changes.
this adds an initial draft of the progiter object. this object 
wraps around long-running loops and reports progress in a simple but customization way. 
the purpose is meant to simplify writing progress messages and create a construct that can simply be dropped into existing code.

i've added in usage of this object into kmeans++ and minibatchkmeans to address my original use case. the case with minibatchkmeans requires a bit more customization because other useful messages in the loop. however, the case with kmeans++ where the change is extremely minimal and really demonstrates how this can just be dropped into existing code. 


#### any other comments?

while this feature does work end-to-end it is not complete. 
because this is a work in progress i have left some debugging code, references to my utility library (utool), and documentation constructs that i use in my coding workflow to quickly test things. 

i don't see myself able to work much on this feature in the near future, but i did want to push what i had so far because (a) just to put it out there, (b) so i don't lose it, and (c) in case it is useful to someone else. 


* **basic usage**
basic usage of the object looks like this: 

```python
    >>> from sklearn.externals.progiter import progiter
    >>> def is_prime(n):
    ...     return n >= 2 and not any(n % i == 0 for i in range(2, n))
    >>> for n in progiter(range(10000)):
    >>>     # do some work
    >>>     is_prime(n)
    10000/10000... rate=13294.94 hz, eta=0:00:00, total=0:00:00, wall=13:34 est 
```
by default the output is continually updated by clearing the previous line, so at the end only the last progress message shows.

* **demo function**
the progiter module itself contains a small demo function to demonstrate how it works. running the demo results in this output: 

```
-----
demo #0: progress can be disabled and incur essentially 0 overhead
however, the overhead of enabled progress is minimal and typically insignificant
this is verbosity mode verbose=0

tic(u'demo0')
...toc(u'demo0')=0.6284s

-----
demo #1: progress is shown by default in the same line
this is verbosity mode verbose=1

tic(u'demo1')
demo1 1000/1000... rate=1584.12 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
...toc(u'demo1')=0.6314s

-----
demo #2: clearline=false prints multiple lines.
progress is only printed as needed
notice the adjustment behavior of the print frequency
this is verbosity mode verbose=2

tic(u'demo2')
demo2    0/1000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:20 est 
demo2    1/1000... rate=2702.52 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo2  257/1000... rate=1522.38 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo2  642/1000... rate=1560.16 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo2 1000/1000... rate=1573.36 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
...toc(u'demo2')=0.6357s

-----
demo #3: adjustments can be turned off to give constant feedback
this is verbosity mode verbose=3

tic(u'demo3')
demo3    0/1000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:20 est 
demo3  100/1000... rate=1476.12 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  200/1000... rate=1427.07 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  300/1000... rate=1479.27 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  400/1000... rate=1505.12 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  500/1000... rate=1491.30 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  600/1000... rate=1515.48 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  700/1000... rate=1512.45 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  800/1000... rate=1514.54 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3  900/1000... rate=1515.45 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
demo3 1000/1000... rate=1516.72 hz, eta=0:00:00, total=0:00:00, wall=13:20 est 
...toc(u'demo3')=0.6594s
```

* **usage in minibatchkmeans**
an example showing how this works in the context of minibatchkmeans is here: 

```python
        >>> from sklearn.cluster import minibatchkmeans
        >>> from sklearn.datasets.samples_generator import make_blobs
        >>> import numpy as np
        >>> n_clusters = 4000
        >>> x, true_labels = make_blobs(n_samples=int(1e5), centers=n_clusters,
        ...                             cluster_std=1., random_state=42)
        >>> mbkm = minibatchkmeans(n_clusters=n_clusters,
        ...                        init_size=3 * n_clusters, n_init=2,
        ...                        random_state=0, verbose=2).fit(x)
        >>> print('mbkm.labels_ = %r' % (mbkm.labels_,))
```

first with verbose=2, which means the progiter object will not clear progress lines and always just append the next line to stdout.

```
init cluster centers with k-means++
kmeans++    0/4000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:24 est 
kmeans++    1/4000... rate=192.34 hz, eta=0:00:20, total=0:00:00, wall=13:24 est 
kmeans++  192/4000... rate=931.83 hz, eta=0:00:04, total=0:00:00, wall=13:24 est 
kmeans++  480/4000... rate=1034.86 hz, eta=0:00:03, total=0:00:00, wall=13:24 est 
kmeans++ 1117/4000... rate=1084.50 hz, eta=0:00:02, total=0:00:01, wall=13:24 est 
kmeans++ 1125/4000... rate=1084.81 hz, eta=0:00:02, total=0:00:01, wall=13:24 est 
kmeans++ 2250/4000... rate=1107.09 hz, eta=0:00:01, total=0:00:02, wall=13:24 est 
kmeans++ 2260/4000... rate=1107.16 hz, eta=0:00:01, total=0:00:02, wall=13:24 est 
kmeans++ 3390/4000... rate=1112.93 hz, eta=0:00:00, total=0:00:03, wall=13:24 est 
kmeans++ 4000/4000... rate=1114.58 hz, eta=0:00:00, total=0:00:03, wall=13:24 est 
inertia for init 1/2: 169.317605
init cluster centers with k-means++
kmeans++    0/4000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:24 est 
kmeans++    1/4000... rate=3412.78 hz, eta=0:00:01, total=0:00:00, wall=13:24 est 
kmeans++  257/4000... rate=975.97 hz, eta=0:00:03, total=0:00:00, wall=13:24 est 
kmeans++  642/4000... rate=1059.49 hz, eta=0:00:03, total=0:00:00, wall=13:24 est 
kmeans++ 1123/4000... rate=1044.57 hz, eta=0:00:02, total=0:00:01, wall=13:24 est 
kmeans++ 2050/4000... rate=1060.59 hz, eta=0:00:01, total=0:00:01, wall=13:24 est 
kmeans++ 2160/4000... rate=1063.67 hz, eta=0:00:01, total=0:00:02, wall=13:24 est 
kmeans++ 3240/4000... rate=1074.09 hz, eta=0:00:00, total=0:00:03, wall=13:24 est 
kmeans++ 3285/4000... rate=1074.54 hz, eta=0:00:00, total=0:00:03, wall=13:24 est 
kmeans++ 4000/4000... rate=1082.62 hz, eta=0:00:00, total=0:00:03, wall=13:24 est 
inertia for init 2/2: 169.461913
begining mini-batch iterations
minibatch      0/100000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:24 est 
minibatch      1/100000... rate=24.79 hz, eta=1:07:13, total=0:00:00, wall=13:24 est inertias: batch=0.024289, ewa=0.024289 
[minibatchkmeans] reassigning 50 cluster centers.
minibatch     12/100000... rate=37.27 hz, eta=0:00:00, total=0:00:00, wall=13:24 est inertias: batch=0.022055, ewa=0.024292 
converged (lack of improvement in inertia) at iteration 12/100000
computing label assignment and total inertia
labels inertia    0/1000... rate=0.00 hz, eta=?, total=0:00:00, wall=13:24 est 
labels inertia    1/1000... rate=348.57 hz, eta=0:00:02, total=0:00:00, wall=13:24 est 
labels inertia  257/1000... rate=382.73 hz, eta=0:00:01, total=0:00:00, wall=13:24 est 
labels inertia  382/1000... rate=382.87 hz, eta=0:00:01, total=0:00:00, wall=13:24 est 
labels inertia  764/1000... rate=389.35 hz, eta=0:00:00, total=0:00:01, wall=13:24 est 
labels inertia  792/1000... rate=389.13 hz, eta=0:00:00, total=0:00:02, wall=13:24 est 
labels inertia 1000/1000... rate=390.99 hz, eta=0:00:00, total=0:00:02, wall=13:24 est 
mbkm.labels_ = array([ 972, 1783,  797, ..., 3203, 3363, 2020], dtype=int32)

```

verbosity 2 can be a bit much, so when verbosity=1 a clearline sequence will tell the terminal to delete the previous verbosity line before it prints the next one. this has a nice where you see a single line in the terminal update every once in awhile. obviously i can't show updates in static text, but at the end of the script it looks like this: 

```
init cluster centers with k-means++
kmeans++ 4000/4000... rate=1260.10 hz, eta=0:00:00, total=0:00:03, wall=13:28 est 
inertia for init 1/2: 169.317605
init cluster centers with k-means++
kmeans++ 4000/4000... rate=1243.40 hz, eta=0:00:00, total=0:00:03, wall=13:28 est 
inertia for init 2/2: 169.461913
begining mini-batch iterations
minibatch      1/100000... rate=24.85 hz, eta=1:07:03, total=0:00:00, wall=13:28 est inertias: batch=0.024289, ewa=0.024289 
[minibatchkmeans] reassigning 50 cluster centers.
minibatch     12/100000... rate=36.89 hz, eta=0:00:00, total=0:00:00, wall=13:28 est inertias: batch=0.022055, ewa=0.024292 
converged (lack of improvement in inertia) at iteration 12/100000
computing label assignment and total inertia
labels inertia 1000/1000... rate=451.42 hz, eta=0:00:00, total=0:00:02, wall=13:28 est 
mbkm.labels_ = array([ 972, 1783,  797, ..., 3203, 3363, 2020], dtype=int32)
```



##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 227551

###Profanity Found
**Text**
#### reference issue

fixes #8499

#### what does this implement/fix? explain your changes.

scikit-learn version of liblinear had tow leaks:

- missing free of the problem struct
- missing free of number of iterations

the former was present in the initial version of ``liblinear_helper.c``
while latter appeared after c8c72fd96e13f9a7fd80362311248321949b8de5
which introduced ``n_iter``.

#### any other comments?

i'm surprised these leaks survived for so long :)

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 228005

###Profanity Found
**Text**
continuing work from #4237 and #2387. 

rather than minimizing the funcsvd-type lost functions specified in the previous attempts, this pr follows advice from @amueller and @gaelvaroquaux , and imports softimpute from [fancyimpute](https://github.com/hammerlab/fancyimpute) instead. 

here is the new cost function being minimized:

![image](https://user-images.githubusercontent.com/1597013/29642894-342457c8-8820-11e7-9acc-93c1e9e27f40.png)


#### what this implements/fixes

a new transformer `sklearn.preprocessing.factorizationimputer`, that uses tests/structure originally created by the previous author as part of #4237

#### what i'd like to hear back

1. any general feedback on how to improve this.
2. how i can add the fancyimpute dependency to scikit-learn

#### other comments

thanks to @sergeyf and iskandr, the authors who created this initial implementation of softimpute in python.

here is [the original paper](http://web.stanford.edu/~hastie/papers/mazumder10a.pdf) where the softimpute algorithm was introduced. here is [another helpful introduction](https://web.stanford.edu/~hastie/swdata/softimpute/vignette.html) to how the algorithm works.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 228350

###Profanity Found
**Text**
the old code generates random points, ignoring the data magnitude.
then all initial centers can be in an arbitrarily bad starting point, and it will take a long time to converge.
the proposed patch just chooses some data samples as initial centers, which is the usual random initialization strategy also with k-means.

<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.


#### any other comments?


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 228929

###Profanity Found
**Text**
added missing square brackets to allow initial classifier prediction example to work correctly.

<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.


#### any other comments?


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 228954

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs

towards #10404 

supersedes and closes #10457. supersedes and closes #10618

<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.


#### any other comments?

todo:

- [x] handle the dense case
- [x] handle the sparse case
- [x] additional test for scale function
- [x] additional test for partial fit
- [x] unit testing of the helper functions in `sparsefuncs`
- [x] back-compatibility of attribute `n_samples_seen_` -> #11235
- [x] address initial comment @ogrisel @jnothman 
- [x] address error message nan and infinity
- [x] optional benchmark


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229161

###Profanity Found
**Text**
this is an initial implementation of what i suggested in https://github.com/scikit-learn/scikit-learn/pull/8022#discussion_r196659219 (ping @amueller).

the idea is to put the test configuration for an estimator class on the class. this provides:
* advantage: can instantiate meta-estimators which have required args
* advantage: can see the test parametrisation clearly on the class
* disadvantage: code limiting `max_iter`, etc., is repetitive (this pr adds lines and decentralises functionality)
* disadvantage: harder for reviewers to point out to a contributor that these changes are needed

the key changes are to [`base.py`](https://github.com/scikit-learn/scikit-learn/pull/11324/files#diff-f392a01b355b04b8c90c84175d118fdc), [`test_common.py`](https://github.com/scikit-learn/scikit-learn/pull/11324/files#diff-b6e2c29089c86706dc868c7bfd58c1d6) and [`estimator_checks.py`](https://github.com/scikit-learn/scikit-learn/pull/11324/files#diff-a95fe0e40350c536a5e303e87ac979c4)

todo:
* [ ] documentation
* [ ] use `_generate_test_params` when calling check_estimator on a class
* [ ] replace `check_parameters_default_constructible`
* [x] work out how to still do `check_no_attributes_set_in_init`
* [ ] test exception when running check_estimator on class requiring parameters

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229230

###Profanity Found
**Text**
unless really intended to error out (not to "fail") if initial import fails for some reason (didn't figure out yet why), then code might end up in exception handling without `message` variable been defined.

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229442

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
fixes  #11996 
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.
currently contains 3 edits:

1. tests to check handle_missing and missing_values are passed and have correct values
2. an update to the onehotencoder docstring and the preprocessing module.
3. an initial implementation logic of the required features as stated by #11996 




##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229628

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
fixes  #11996 
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.
currently contains 3 edits:

1. tests to check handle_missing and missing_values are passed and have correct values
2. an update to the onehotencoder docstring and the preprocessing module.
3. an initial implementation logic of the required features as stated by #11996 




##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229634

###Profanity Found
**Text**
fixes #10302, fixes #12429, fixes #2691

gradient boosting used to fail when init was a sklearn estimator, which is a bit ironic :)
issue was that the predict output didn't have the expected shape. and apparently there was no test for the init parameter with other estimator than default.

*edit* also accept initial estimator which does not support sample weights as long as the gradient boosting is not fitted with sample weights

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229866

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.

in `test_logistic.py`, the test `test_log_reg_cv_penalty` randomly fails.
setting an rng seed to 6 will make it fail invariably:

```python
@pytest.mark.filterwarnings('ignore: default multi_class will')  # 0.22
@pytest.mark.filterwarnings('ignore: you should specify a value')  # 0.22
def test_logreg_cv_penalty():
    # test that the correct penalty is passed to the final fit.
    rng = np.random.randomstate(6)
    x, y = make_classification(n_samples=50, n_features=20, random_state=rng)
    lr_cv = logisticregressioncv(penalty="l1", cs=[1.0], solver='saga',
                                 random_state=rng)
    lr_cv.fit(x, y)
    lr = logisticregression(penalty="l1", c=1.0, solver='saga',
                            random_state=rng)
    lr.fit(x, y)
    assert_equal(np.count_nonzero(lr_cv.coef_), np.count_nonzero(lr.coef_))
```

this pr sets a rng, changes the penalty from l1 to l2, and checks that the coefficients are almost equal instead of checking the sparsity of the coefficients with l1.

note: i tried keeping the initial loss l1, but with `rng = np.random.randomstate(6)` the coefficients would still be slightly different and the tests would fail. i think this is because the rng is consumed differently in `logisticregression` and in `logisticregressioncv`

#### any other comments?


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229959

###Profanity Found
**Text**
#### reference issues/prs
this is a draft implementation of #6424.
it doesn't really introduce anything new in the api, but i'm happy to move this to a slep.
below is an initial description. happy to include feedback in the slep.


#### what does this implement/fix? explain your changes.
the main idea of this is to make compound scikit-learn estimators less opaque by providing "feature names" as strings.

#### motivation
we've been making it easier to build complex workflows with the columntransformer and i expect it will find wide adoption. however, using it results in very opaque models, even more so than before.
we have a great usage example in the gallery that applies a classifier to the titanic data set. to me this is a very simple standard usecase.

markdown doesn't let me paste this as details, so just look here:
https://scikit-learn.org/dev/auto_examples/compose/plot_column_transformer_mixed_types.html

however, it's impossible to interpret or even sanity-check the ``logisticregression`` instance that's produced here, because the correspondence of the coefficients to the input features is basically impossible to figure out.
this pr enables using ``get_feature_names`` to obtain the semantics for the coefficients:
```python
preprocessor.get_feature_names(x.columns)
```
```
['num__age',
 'num__fare',
 'cat__embarked_c',
 'cat__embarked_q',
 'cat__embarked_s',
 'cat__embarked_missing',
 'cat__sex_female',
 'cat__sex_male',
 'cat__pclass_1',
 'cat__pclass_2',
 'cat__pclass_3']
```

i think this is essential information in any machine learning workflow and it's imperative that we allow the user to get to this information in some way.

the proposed api will add a method ``get_feature_names`` to all supported (see below) transformers, with a (possibly optional, see below) parameter "input features" which is an array-like of strings.

#### alternative interfaces
to me there are four main options for interfaces to enable this:

1) implement transformative ``get_feature_names`` as in this pr
2) implement a more comprehensive feature description language (as done in eli-5, i think)
3) tie in more strongly with pandas and use dataframes  / column names
 a) to output feature semantics.
 b) to determine feature semantics
4) leave it to the user.

while i think 2) and 3) a) is are valid option for the future, i think trying to implement this now will probably result in a gridlock and/or take too much time. i think we should iterate and provide something that solves the 80% use-case quickly. we can create a more elaborate solution later, in particular since this proposal/pr doesn't introduce any concepts that are not in sklearn already.
3 b) is discussed below.

i don't think 4) is a realistic option. i assume we can agree that the titanic example above is a valid use-case, and that getting the semantics of features is important. below is the code that the user would have to write to do this themselves. this will become even harder in the future if the pipeline will do cloning.
<details>
i'm hardcoding that the second imputer uses "constant" and the first one doesn't otherwise this would get way too messy. this also hard-codes several other things, like the order of the transformers in the column transformer. it also already makes use of a transformative ``get_feature_names`` in the ``onehotencoder`` without which it would be completely impossible.

```python
numeric_fitted = preprocessor.named_transformers_.num

num_features_transformed = np.array(numeric_features)[np.logical_not(np.isnan(numeric_fitted.named_steps.imputer.statistics_))]
categorical_fitted = preprocessor.named_transformers_.cat
cat_features_transformed = categorical_fitted.named_steps.onehot.get_feature_names(categorical_features)

feature_names = np.hstack([num_features_transformed, cat_features_transformed])
```
</details>


#### scope
i suggest we limit ``get_feature_names`` to transformers that either:
- leave columns unchanged
- select a subset of columns
- create new columns where each column depends on at most one input column.
- polynomialfeatures (or possibly algorithms that create combinations of o(1) features)

also, i want the string to only convey presence or absence of features, or constant functions of the features. so scaling would not change a feature_name, while a log-transformation (or polynomial) might. this limits the complexity of the string (but also it's usefulness somewhat).

together, these mean that there will be no support for multivariate transformations like pca or nmf or kmeans.

#### implementation
given the above scope and api, and the current implementation of ``get_feature_names`` in ``columntransformer`` there are two main mechanism that need to be implemented.

1. allow pipeline to pass around names
2. provide a mechanism for meta-estimators (columntransformer and pipeline and feature union) to "know what to do".

there are basically three cases the meta-estimators need to take care of:
a) the transformer does a non-trivial column transformation, like onehotencoder or feature selection
b) the transformer does "nothing" to the columns, like standardscaler.
c) the transformer does a "too complex" operation to the columns, like pca.

for a), only the estimator can handle this case, so the estimator needs to provide a function to do that - already implemented in several cases as a transformative ``get_feature_names``. for b) the meta-estimator can simply do a pass-through, so we need to "flag" these in some way. there is no way for the meta-estimator to really handle c) so if the estimator is not "tagged" as being trival and doesn't implement ``get_feature_names`` the meta-estimator needs to bail in some way.

i added a "onetoonemixin" to tag the trivial transformations. it would be possible to just use this as a tag, and let the meta-estimators handle the pass-through. given that we already have the mechanism to handle the pass-through, i thought it would be simpler to just implement a pass-through ``get_feature_names`` (another alternative would be to add an estimator tag, but that also seems less elegant).

right now the bail in case c) is a typeerror.

#### limitations
- the general api requires "input features". in ``polynomialfeatures`` this was optional. unfortunately we have no way to know the input dimensionality of a fitted transformer in general, so automatically generating ``x1``, ``x2``, etc is not possible. this could be fixed by adding a required ``n_features_`` to the api, which would probably be helpful but also would be a relatively heavy addition.

- because we don't know the number of input features, there's no way to ensure the user passed the right length of ``input_features``

- the implementation of ``get_feature_names`` in pipeline is a hack, because it includes or excludes the last step based on whether the last step has ``transform``. the reason for this is that given a trained pipeline with a classifier in the end, i want to be able to get the feature names, which would not include the last step. in preprocessing pipelines we always want to include all the steps, though.
the real solution to this in my opinion is always to include the last step, and allow slicing the pipeline (#2568) to get the feature names for a pipeline with a final supervised step.

- bailing to a typeerror if any "complex" transformation happens is a bit of a bummer. we could try to generate names like ``pca_1``, ``pca_2``, ... but to do this automatically we would need to know the output dimensionality, which we don't (unless we add ``n_outputs_`` as required attribute to the api similar to ``n_features_`` above)

#### open questions

- do we want to require ``get_feature_names`` to accept ``input_features``? right now the vectorizers don't and it makes the code slightly more complex.

- how do we want to handle the hack in pipeline.get_feature_names for the last step?

- do we want to encode fixed univariate transformations ("scale", "log", "rank"?)

#### possible extensions

- don't require ``input_features`` and generate names
- generate names for "complex transformations"
- use pandas column names as ``input_features`` if available (3b above)

i already discussed the requirements for the first two extensions (adding ``n_features_`` and ``n_outputs_``).
the last one would require storing the input column names if the input is a pandas dataframe. it shouldn't be hard to do, and would also enable solving #7242 and i'd like to do that, but it's not required for this proposal to be useful.

#### todo

- [ ] add to narrative docs
- [ ] add to remaining estimators (feature selection is the only left?)
- [ ] allow input_feature for all ``get_feature_names`` methods?

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 229962

###Profanity Found
**Text**
<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->

closes #12436 , continuation of the work from @jeremiedbb 

#### what does this implement/fix? explain your changes.

this pr:

- [x] fixes the use of the `init` estimator parameter in gbdts
- [x] exposes `init='zero'` which was supported but undocumented.
- [x] deprecates all the losses and init estimators in `gradient_boosting.py`
  - [x] the loss classes have been moved to a `losses.py` file and have a new `get_init_raw_predictions` method
  - [x] the init estimators are replaced by an equivalent instance of `dummyclassfier` or `dummyregressor`
- [x] renames `y_pred` into `raw_predictions`, and relevant (private) methods as well.
- [x] fixes some the inaccurate docstrings
- [x] "fixes" the initial default prediction for multiclass classification: the raw prediction used to be the classes priors, but it should be the log of the priors. in practice the difference in accuracy is very minimal: over 100 runs, i observed an avg improvement in test accuracy of `0.000388` (std = `0.008266`) between the 2 methods, with `n_estimators=1`, `n_samples=10000`.

the `loss.get_init_raw_predictions(x, predictor)` methods return a `raw_prediction` with the correct shape `(n_samples, k)` where `k` is the number of classes in multiclass classification, else `1`.

those `raw_predictions` are homogeneous to what the trees predict, not homogeneous to what the ensemble predicts. for regression gbdt this is the same thing, but for e.g. binary classification `raw_prediction` is homogeneous to a log-odds ratio.

for more, see https://github.com/scikit-learn/scikit-learn/pull/12436#issuecomment-450037071 and following discussion (not sure if this is much clearer ^^)

#### any other comments?



<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230160

###Profanity Found
**Text**
#### what does this implement/fix? explain your changes.
this is a calibration method which is used to calibrate the probability prediction of binary classification model. this [mimic calibration](https://www.youtube.com/watch?v=cg--sc76i1i) was mentioned by nyc ml meetup talk given by sam steingold.
with my understanding from this talk, i implemented this method. i also provided more detail comments in the code. 

#### outline of mimic calibration.
it is a method to calibrate probability prediction of binary classification model.                                             it requires two inputs, the probability prediction from binary classification model and                                       the binary target (0 and 1).                                                                                                   
here is how it is implemented.                                                                                                 
    1. sort the probabitliy in the ascending. merge neighbor data points into one bin                                              
       until the number of positive equal to threshold positive at each bin. in this initial binning,                              
       only the last bin may have number of positive less than threshold positive.                                                 
    2. calculate the number of positive rate at each bin. merge neighbor two bins if npos rate in the left 
        bin is greater than right bin.                                                                                                  
    3. keep step 2. until the npos rate in the increasing order.                                                                   
    4. in this step, we have information at each bin, such as npos rate, the avg/min/max probability.                              
       the final step is linear interpolation on the prediction.                                                                   
       given probability prediction from binary classification model, we find out which bin it belongs to.                         
       then, we perform linear interpolation in the corresponding bin.

let me know if there is anything unclear. or some people are already working on this. please let me know. thanks!

<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230362

###Profanity Found
**Text**
#### what does this fix:
while trying to make my intent classifier training deterministic in my [nlu lib](https://github.com/snipsco/snips-nlu) i noticed that i couldn't because the `basesgdclassifier._fit_multiclass` method is non deterministic.

to reproduce you have to initialize the `sgdclassifier` with a `randomstate` instance:
```python
from sklearn.linear_model import sgdclassifier
from sklearn.utils import check_random_state


def sgd_test():
    seed = 1
    random_state = check_random_state(seed)

    num_classes = 3
    num_examples = 10
    x = random_state.normal(0.0, 1, size=(num_examples, num_classes))
    y = random_state.randint(num_classes, size=num_examples)

    num_iter = 1000
    ref_coef = none
    for i in range(num_iter):
        print("iter %s" % i)
        random_state = check_random_state(seed)
        clf = sgdclassifier(
            random_state=random_state, n_jobs=num_classes).fit(x, y)
        if ref_coef is none:
            ref_coef = clf.coef_.tolist()
        assert ref_coef == clf.coef_.tolist()


if __name__ == '__main__':
    sgd_test()
```

i added a small print statement just before the joblib threads pass their seed to the `plain_sgd` or `average_sgd` function. this gives me the following output (and will give you a different output on your machine but will eventually fail):
```
iter 0
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 1
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 2
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 3
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 4
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 5
thread: 0, seed 1791095845
thread: 1, seed 2135392491
thread: 2, seed 946286476
iter 6
thread: 0, seed 1791095845
thread: 2, seed 2135392491
thread: 1, seed 946286476
traceback (most recent call last):
  file "test_sgd_seed.py", line 27, in <module>
    sgd_test()
  file "test_sgd_seed.py", line 23, in sgd_test
    assert ref_coef == clf.coef_.tolist()
assertionerror

process finished with exit code 1
````

what is happening is that the joblib threads share the `basesgdclassifier.random_state` and set a seed in the `fit_binary` function before it's passed to the `plain_sgd` or `average_sgd` function. depending on the order on which the threads reach the seed setting, the output of the sgd can differ.

the other reason is that the estimator random state was not passed in the `make_dataset` function.

i think the bug was not noticeable in the unit tests because the sgd estimators were initialized with `int` random states. in this case, the input of the `check_random_state` function in the `fit_binary` function is the integer seed, and each thread is actually returning the exact same random state and then sample the exact same random seed for the sgd.

#### how does this fixes the bug:
- i added an optional `seed` argument to the `fit_binary` function which default to `none`. if the seed is not `none` then it will be used otherwise the seed is set with the estimator `random_state`. this allows to set the jobs seeds before the jobs are distributed to the threads and avoids the non-deterministic behavior
- i passed the estimator random state to the `make_dataset` function
- i had to change a few seeds and doctests here and there to make the unit tests pass again

#### help needed
- do you have any idea on how to properly test my fix ?

(now also fixes #5015.)

#### comment
while fixing the initial but another bug was found and fixed: the `our_rand_r` in the cython code of the `sklearn/utils/seq_dataset.pyx` was not behaving consistently across platforms, see the full bug description and fix [below](https://github.com/scikit-learn/scikit-learn/pull/13422#issuecomment-472894022)

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230400

###Profanity Found
**Text**
hi @jnothman, the initial of this is just to transport the original python code of `linear assignment` into cython. however, i am not very familiar with cython and the code need to be optimized a lot. i sincerely hope that people from the community can help me optimize this program and further improve this algorithm.

> i haven't add compile set in setup.py as to request experts who may want to optimize this cython code, really appreciate it and thanks!

<!--
thanks for contributing a pull request! please ensure you have taken a look at
the contribution guidelines: https://github.com/scikit-learn/scikit-learn/blob/master/contributing.md#pull-request-checklist
-->

#### reference issues/prs
<!--
example: fixes #1234. see also #3456.
please use keywords (e.g., fixes) to create link to the issues or pull requests
you resolved, so that they will automatically be closed when your pull request
is merged. see https://github.com/blog/1506-closing-issues-via-pull-requests
-->


#### what does this implement/fix? explain your changes.

a refactor project of original `linear_assignment_.py`

#### any other comments?


<!--
please be aware that we are a loose team of volunteers so patience is
necessary; assistance handling other issues is very welcome. we value
all user contributions, no matter how minor they are. if we are slow to
review, either the pull request needs some benchmarking, tinkering,
convincing, etc. or more likely the reviewers are simply busy. in either
case, we ask for your understanding during the review process.
for more information, see our faq on this topic:
http://scikit-learn.org/dev/faq.html#why-is-my-pull-request-not-getting-any-attention.

thanks for contributing!
-->


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230448

###Profanity Found
**Text**
patch release for the euclidean distances fix. we can delay this if we want, but it's a pretty high risk issue.

rebase so far looks like:
```
d 0b3aa5e466 doc bump version
d 10249939e5 doc move 0.20 to previous releases
d e7bd8a33e5 fix optics paper typo which resulted in undersized clusters (#13750)
d 384c8ad3d3 enh add a break_ties parameter to svc and nusvc (#12557)
d 13981bdce9 sty remove variable renaming (#13731)
d 19192c0427 maint replace manual checks with `check_is_fitted`  (#13013)
d 905dedc635 dep remove random_state from oneclasssvm (#13802)
d 28480f4cb2 dep change the default of gamma in svm (#13801)
d d0a94fea74 dep remove graph lasso (#13795)
d 7896b21562 mnt change default of solver in logisiticregression (#13805)
d 6525a39dd6 mnt remove imputer in preprocessing (#13796)
d 43f85020c5 dep remove correlation and regression models from gaussianprocess (#13819)
d 2b7a69baca dep remove the batch_size parameter from pariwise_distance_argmin (#13822)
d 53624e8c26 dep remove public function download_20newsgroups (#13829)
d 9631a67388 dep remove scale_face function from lfw (#13830)
d 777f91f114 [mrg] dep removed the reorder parameter from the auc function (#13827)
d 7166ae8ece mnt updated adjusted_mutual_info_score and normalized_mutual_info_score default to 'arithmetic' (#13814)
d 91e019df5e dep remove precomputed parameter in t_sne.trustworthiness (#13820)
d 69eb4d4678 [mrg] dep change default and deprecate iid in searchcv (#13834)
d c7566ea232 disallow input as sparse matrix in affinity propagation function, aff… (#13828)
d 95339a677e [mrg] dep remove pooling_func in agglomerativeclustering (#13821)
d 7fdac52c19 mnt remove backward compatibility of param order in make_column_transformer (#13831)
d 8a8e21b2a3 mnt change the default value of n_estimators in forests (#13803)
d 83656484a8 mnt remove raises and with_setup requiring nose (#13842)
d da9e680996 doc fix the docstring of ami mni regarding new default (#13837)
d eec7614a1f small fixes to maintainer commands
d b243c6aa43 dep change default of contamination in lof (#13815)
d 75967ef20e dep remove deprecated parameters in ellipticenvelope (#13818)
p 17eb3c9ca0 doc update readme.rst (#13879)
p e76984b0a1 [mrg] doc about creating an experimental module (#13865)
p c890ecd923 doc fix missing newline in distancemetric docs (#13888)
d 11de9d60f2 updating missingindicator user guide section (#13849)
d 4e65827b5c [mrg] ridgecv minor refactor to improve readability (#13832)
d 5d240c6a0b maint fixes coverage reporting on pylatest_conda (#13895)
p 2fd1a6725b doc improve documentation of r-squared in user guide (#13867)
p ea58e27ace doc documentation improvement in fbeta_score and onehotencoder (#13904)
p eb93420e87 doc rewrite algorithm selection section for nearest neighbours (#13906)
p 98aefc1fdc fix regression in eulidean distances (float32) related to batch management (#13910)
p 0a2dc72982 tst improve warning reporting (#12597)
d af4247b152 dep remove utilities related to mldata (#13798)
d 0bfa52dad7 dep change default of error_score in cross-validation (#13840)
d 911792b008 enh avoid calling _encode_check_unknown() twice in baseencoder.transform (#13810)
d 57c04f4e8d enh allows setting of initial hyperparameters for bayesianridge (#13618)
d 778b11904e [mrg] dep remove threshold_, change contamination, deprecate behaviour in iforest (#13811)
d c28ef9ef2a dep change the default of multi_class to 'auto' in logistic regression (#13807)
p 62a0bcdbe1 better fix the rng seed in test_fastica_simple (#13848)
p c418761265 fix clip small values in pls cross-decomposition for increased stability (#13903)
d e0532cdea5 maint increase numerical gradient check tolerance to make the test stable (#13885)
p e35f040200 [mrg] fixes get_feature_names results when using drop functionality (#13894)
p dc5e4d8896 fix downcast large matrix indices where possible in sparsefuncs._minor_reduce (fix #13737) (#13741)
```

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230693

###Profanity Found
**Text**
to be merged without squashing.

i thought we should consider if 0.21.3 should be released at some point soon (early july). it's one month since 0.21.2 was released. this branch currently just includes https://github.com/scikit-learn/scikit-learn/milestone/30?closed=1 and https://github.com/scikit-learn/scikit-learn/milestone/34?closed=1. we should review documentation commits that should also be included.

the initial commit selection is:
```
drop 0b3aa5e466 doc bump version
drop 10249939e5 doc move 0.20 to previous releases
drop e7bd8a33e5 fix optics paper typo which resulted in undersized clusters (#13750)
drop 384c8ad3d3 enh add a break_ties parameter to svc and nusvc (#12557)
drop 13981bdce9 sty remove variable renaming (#13731)
drop 19192c0427 maint replace manual checks with `check_is_fitted`  (#13013)
drop 905dedc635 dep remove random_state from oneclasssvm (#13802)
drop 28480f4cb2 dep change the default of gamma in svm (#13801)
drop d0a94fea74 dep remove graph lasso (#13795)
drop 7896b21562 mnt change default of solver in logisiticregression (#13805)
drop 6525a39dd6 mnt remove imputer in preprocessing (#13796)
drop 43f85020c5 dep remove correlation and regression models from gaussianprocess (#13819)
drop 2b7a69baca dep remove the batch_size parameter from pariwise_distance_argmin (#13822)
drop 53624e8c26 dep remove public function download_20newsgroups (#13829)
drop 9631a67388 dep remove scale_face function from lfw (#13830)
drop 777f91f114 [mrg] dep removed the reorder parameter from the auc function (#13827)
drop 7166ae8ece mnt updated adjusted_mutual_info_score and normalized_mutual_info_score default to 'arithmetic' (#13814)
drop 91e019df5e dep remove precomputed parameter in t_sne.trustworthiness (#13820)
drop 69eb4d4678 [mrg] dep change default and deprecate iid in searchcv (#13834)
drop c7566ea232 disallow input as sparse matrix in affinity propagation function, aff… (#13828)
drop 95339a677e [mrg] dep remove pooling_func in agglomerativeclustering (#13821)
drop 7fdac52c19 mnt remove backward compatibility of param order in make_column_transformer (#13831)
drop 8a8e21b2a3 mnt change the default value of n_estimators in forests (#13803)
drop 83656484a8 mnt remove raises and with_setup requiring nose (#13842)
drop da9e680996 doc fix the docstring of ami mni regarding new default (#13837)
drop eec7614a1f small fixes to maintainer commands
drop b243c6aa43 dep change default of contamination in lof (#13815)
drop 75967ef20e dep remove deprecated parameters in ellipticenvelope (#13818)
drop 11de9d60f2 updating missingindicator user guide section (#13849)
drop 4e65827b5c [mrg] ridgecv minor refactor to improve readability (#13832)
drop 5d240c6a0b maint fixes coverage reporting on pylatest_conda (#13895)
drop af4247b152 dep remove utilities related to mldata (#13798)
drop 0bfa52dad7 dep change default of error_score in cross-validation (#13840)
drop 911792b008 enh avoid calling _encode_check_unknown() twice in baseencoder.transform (#13810)
drop 57c04f4e8d enh allows setting of initial hyperparameters for bayesianridge (#13618)
drop 778b11904e [mrg] dep remove threshold_, change contamination, deprecate behaviour in iforest (#13811)
drop c28ef9ef2a dep change the default of multi_class to 'auto' in logistic regression (#13807)
drop e0532cdea5 maint increase numerical gradient check tolerance to make the test stable (#13885)
drop 8f378ca684 doc fix bracket typo in linear_model.rst (#13932)
drop e747376eef [mrg] maint fixes apt by removing the ubuntu-toolchain-r/test repo (#13934)
drop 22b0eabfd0 doc add 0.21.3 entry
pick f3a6a1a6c8 tst avoid nose collecting train_test_split as a test (#13951)
drop db48ebce60 enh add n_components kwarg to spectralclustering. see #13698 (#13726)
pick fa383a4aca fix plot_tree now displays correct criterion (#13947)
drop cebefd4f01 doc adds instructions for building on freebsd (#13953)
drop 69dd9a54e2 doc correct headline level in contributor docs (#13959)
drop 57726672b5 cln remove parent negative loss calculation from for loop to improve performance (#13955)
drop 2a7194de7a fix bin training and validation data separately in gbdts (#13933)
drop be03467b9c fix changed variancethreshold behaviour when threshold is zero. see #13691 (#13704)
drop 9f7e8671dc perf free problem and param sooner in liblinear.train_wrap
drop f283ed6b40 cln removed max_bins from splitter in gbdt (#13927)
drop 54e6c720de cln refactors code (#13966)
pick 7ea7284f22 maint: use explicit value of n_jobs to avoid hangs on windows (#13970)
drop b271e20570 dep remove positive parameter for lars solver (#13863)
drop a98db9a4d6 dep change default and deprecate normalize_components in sparsepca (#13838)
drop 9ee164baa3 [mrg] dep remove legacy mode from onehotencoder (#13855)
drop 9328581ec5 fix use cd solver in face decomposition to use postive parameter (#13975)
drop 9adba491a2 [mrg] dep change the default of cv and n_splits (#13839)
drop 7ee46f1717 fix lazy cython import for pytest to work without cython
drop 3ed200292f added matplotlib to show_versions() (#13983)
drop 233fd6df32 doc add doc example to oneclasssvm
drop ccd6399cad cln gbdts: don't split on last bin (explicitly) (#13919)
drop 896a76eb22 [mrg][doc] fix inconsistencies in clustering doc. (#13946)
drop e871a56d44 doc fixed documentation typos (#13993)
drop 5e0d1a1f04 doc fix typo: omit comma (#13999)
drop 9661a64fae enh avoid uncessary copies in sklearn.preprocessing (#13987)
drop 2e7e06b78f [mrg] doctest with print change only adjusts default options for doctest (#13991)
pick 162216af26 maint: test_encoder_dtypes_pandas reads expected dtype from df (#13997)
drop 15b54340ee [mrg] cln only one function for parallel predict (#14003)
drop ccd3331f7e mnt remove unused imports (#14021)
drop 6675c9e342 maint pass n_samples instead of sample_indices in gbdt (#14017)
drop ec35ed226c ehn add function score_samples to pipeline (#13806)
drop 2b571c039d mnt better message for pillow import error (#14027)
drop abf7721904 tst fix a part of gradient boosting test which wasn't running (#14032)
drop 69dbdf4f9b mnt doc don't warn if a ref with single backtick is not found (#14040)
drop 0f801d7ba8 doc link set_config and config_context in docstrings (#14030)
pick a80d679ff7 mnt doc fix some sphinx warnings on what's new files (#14049)
drop b3d716c924 doc fixes default value for eta0 in sgdregressor (#14047)
drop 8342548ae1 exa remove useless sections in omp example (#14019)
drop 61f6f5bcd1 tst add test to check that all ridge solver give the same results (#13914)
drop c315bf9314 mnt ignore setup.py in the coverage report (#14052)
drop 9d7b804603 maint: adjustments to test_logistic.py::test_dtype_match (#13645)
drop d84a8d17af enh binary only estimator checks for classification (#13875)
drop 4c58057dda doc add what's new for binary only estimator checks (#13875)
drop 9c732e15a8 doc fix typo in manifold documentation (#14073)
drop 227ebc4815 doc fix the default value of learning_rate in docstring of histgbc. (#14072)
drop e669a89aa4 cln removed some unused imports (#14074)
drop 05b12cfcfd perf shrink arrays to size in liblinear helper dense_to_sparse (#14026)
drop 2fc3a85b3f maint use isinstance(x, numbers.integral) to check for integer dtype (#14004)
drop 73caac258c maint fixes lgtm errors (#14041)
drop 50425e1dfe maint remove sudo tag in travis (#14050)
drop d91b0f324b mnt refactor naive bayes tests (#14064)
pick 8fe89ea524 fix wrong usage and occurrence of string tag (#14043)
drop fd1d210362 doc add kcachegrind visualization docs (#8016)
drop 4a6264db68 tst add test for pipeline in partial dependence (#14079)
drop 76ce7c5b63 dep change default validate in functiontransformer to false(#13817)
drop a5743ed36f tst add test for lad-loss and quantile loss equivalence (old gbdt code) (#14086)
pick b580ad5dfd bug fix zero division error in gbdts (#14024)
drop bec83089f7 maint uses pytest-xdist to parallelize tests (#13041)
drop e2a69b7376 doc use train/test split in gaussiannb example (#14080)
drop df7dd83911 enh allow sparse input to incremental pca (#13960)
drop 3ec339a58f added colorblind compatibility (#14091)
pick 36b688eb04 [mrg] fix refit=false error in logisticregressioncv (#14087)
drop b28aadf6ef added fit and score times for learning_curve (#13938)
drop eed5cba610 tst check that estimators are not cloned during pipeline construction (#7633)
pick cb12053c57 doc make parameter, etc listings use small screen width better (#9503)
drop 6ab8c86c38 [mrg] doc doc sklearn.manifold.t_sne.trustworthiness added to classes.rst (#9747)
drop 0eedf99eee maint don't use clean_warnings_registry in tests (#14085)
drop 120009b12a doc fix user guide for learning_curve (#14099)
drop b7c4163690 fix fix off-by-one error in liblinear helper dense_to_sparse (#14103)
pick e2b6bff0ac bug fixes export_text with single feature (#14053)
drop 1015caf54d maint remove imports from sklearn.utils._joblib (#13676)
drop 7ce8b21cd1 perf don't allocate space for bias element if there isn't one (#14108)
pick 197f448eed [mrg] fix nca parameter type check (#14092)
drop 4a325353ef mnt fix some typos in readme (#14122)
drop f9f8974216 doc updated class_weight explanation in glossary (#14121)
drop 801cca8e73 mnt fix suppressing matplotlib warning issue while making docs (#14115)
drop b3030f046f minor fix in gaussian_mixture.py (#14120)
drop 0c110701f9 tst fixed typo in test_column_transformer (#14128)
drop 8632775c23 fix fix memory leak in liblinear helper csr_to_sparse error path (#14118)
drop 842df6f60e maint faster linear_model tests (#14105)
drop ab4b4ec5eb doc add clarification on random forest default params (#13248)
pick 6b811ac2c3 doc add missing what's new to pr 14092 (#14133)
drop 214def06a3 doc contributing guide update (#13961)
drop cf2e60bc1b maint simplify arguments to csr_set_problem and csr_to_sparse (#14135)
drop c0d77d4d37 doc: document resulting nan in simpleimputer.statistics_ (#14129)
drop da96da96f0 ehn add warm_start parameter to histgradientboosting (#14012)
drop 3d997697fd [mrg] error for cosine affinity when zero vectors present (#7943)
drop e94f5de906 fix remove action of normalize_components in sparsepca (#14134)
drop ee8bdd0b61 enh add joblib to the list of dependencies in show_versions (#14141)
drop 8681ece373 enh fix unfriendly error message for documentation checks (#11967)
drop 5674122c97 maint more test runtime optimizations (#14136)
drop 5b8b6277a3 doc fixing the missing fetch upstream in contributing docs (#14142)
drop d710f73096 doc fix suptitle in lda_qda example (#14130)
drop 27bffe63dd ci _changed.html now provides links to compare pr to dev and stable (#14165)
drop a31676b948 exa readability of plot_isotonic_regression.py for color blind persons (#14154)
drop 59612a22b3 doc fixed future warnings by explicitly defining n_estimators = 100 in for the regressor. (#14159)
drop 9bdcf25fda exa fixed convergence warnings by changing solver to 'lbfgs' in plot_mlp_alpha.py (#14158)
drop 8b002f2714 maint fix test_fit_csr_matrix failure on master (#14171)
drop 55a7752f2e exa remove warnings by setting n_quantiles in plot_transformed_target (#14156)
drop f41cd1e856 exa use n_quantiles=500 in plot_map_data_to_normal.py (#14149)
drop 0bdd92036d [mrg] maint adds tag categorical to onehotencoder (#14068)
drop 62d11120c4 doc make more obvious that logistic regression is regularized by default (#14093)
drop a717619b8b exa more color blind friendly colors in plot_map_data_to_normal.py (#wimlds) (#14173)
drop 78ac1ab026 tst add requires_positive_y estimator tag (#14095)
pick 7f50e82663 fix initialize missingindicator with error_on_new = false (#13974)
drop be17713d85 maint upgrade ci to pypy 7.1.1, fix ci failure on master (#13912)
drop eade48eaa2 tst refactor test_truncated_svd (#14140)
drop 24d4b2c2f3 exa fixed convergence warnings on mlp training curves (#14144)
drop a413f88fea tst fix test_truncated_svd.py::test_explained_variance_compone… (#14178)
drop 11d2539444 maint enable ccache in circleci / fix ci on master (#14172)
drop 1dc7b1d84a doc add use_line_collection=true to plt.stem to remove warning (#14146)
drop f6923a2971 fixes #10548 random state description in feature-extraction (#14155)
```

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230853

###Profanity Found
**Text**
a minimal implementation of generalized linear models (glm) from https://github.com/scikit-learn/scikit-learn/pull/9405 by @lorentzenchr 

this only includes l2 penalty with the lbfgs solver. in other words, in excludes l1 penalties (or cd solver), matrix penalties, warm start, some distributions (e.g. `binomialdistribution`), newton-cg & irls solvers from the original glm pr. 

the goals is to get an easier to review initial implementation. benchmarks were done in https://github.com/scikit-learn/scikit-learn/pull/9405#issuecomment-499578511

#### todo
 - [x] fix user manual and comments regarding removed functionality
 - [x] examples may need some more work
 - [x] use a standalone tweedie deviance metric https://github.com/scikit-learn/scikit-learn/pull/14263 once it is merged
 - [x] refactor the lbfs optimizer interface once https://github.com/scikit-learn/scikit-learn/pull/14250 is merged
 - [x] use a common function for `sample_weight` validations https://github.com/scikit-learn/scikit-learn/pull/14307
 - [x] expose objects that are for now not controversial to `sklearn.linear_model`
 - [ ] ~~consider using a diagonal preconditioner as discussed in #15556 and #15583 for logistic regression~~ edit: not in this pr -- roman

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230912

###Profanity Found
**Text**
#### reference issues/prs
attempts to make use of `scipy.stats.mstats.mode` within`simpleimputer(strategy='most_frequent')`. this was suggested in #14325 since a previous bug within the `mstats.mode` function [has been fixed](https://github.com/scipy/scipy/pull/2672).

#### what does this implement/fix? explain your changes.
i'm currently using the updated `mstats.mode` function to impute values for numeric inputs. 

however, it seems that `mstats.mode` will not work with alpha inputs because it requires that the inputs can be cast to floats. this happens [here](https://github.com/scipy/scipy/blob/master/scipy/stats/mstats_basic.py#l151) when `mstats.mode` internally calls `find_repeats`.

#### any other comments?
my initial assumption was that `mstats.mode` would be able to handle all input types (since `scipy.stats.mode` can) and that the code block for `strategy == 'most_frequent'` could be cleanly handled with this single function.

my current understanding is that any non-numeric inputs would have to be handled separately by passing them off to `scipy.stats.mode` -- however this is already the current behavior for all cases (numeric and otherwise). data are being passed into the internal function `_most_frequent`, which is using `scipy.stats.mode`. i could be overlooking something obvious but for now it seems to me that using `mstats.mode` might introduce more complexity into the code.

#### request for feedback
what do you think is the best way forward? do you think there is a simpler way that i could continue on  with `mstats.mode` that i might be missing or does it not seem worth it to include `mstats.mode`?


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 230976

###Profanity Found
**Text**
addresses #14582

i used the following as a guideline to separate sections. also this is just an initial version to get feedback. the new file with developing estimators is pretty bare bones and might need more verbiage.  

ways to contribute - contributing
submitting a bug report or a feature request - contributing
how to make a good bug report
contributing code - contributing
how to contribute
pull request checklist
continuous integration (ci)
stalled pull requests
issues for new contributors
documentation - contributing
building the documentation
guidelines for writing documentation
generated documentation on circleci
testing and improving test coverage - developing
writing matplotlib related tests
workflow to improve test coverage
issue tracker tags - contributing - i don't think this belongs here in any case
coding guidelines - contributing for top matter
input validation - developing?
random numbers - developing
deprecation - contributing
change the default value of a parameter - contributing
python versions supported - contributing
code review guidelines - contributing
apis of scikit-learn objects - developing
different objects
estimators
instantiation
fitting
estimated attributes
optional arguments
pairwise attributes
rolling your own estimator - developing
get_params and set_params
parameters and init
cloning
pipeline compatibility
estimator types
specific models
estimator tags
reading the existing code base - contributing



##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 231110

###Profanity Found
**Text**
hello.

this is proof of concept of geneticsearchcv. it implements genetic algorithm for hyper parameters search.

this is only initial commits to show concept. more docs, tests and code improvements will be added later, as well as removing copy-paste. :)

i just wanted to know you opinion about idea to implement it. :)

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 231254

###Profanity Found
**Text**
**jira ticket**: https://jira.duraspace.org/browse/fcrepo-2761

* part of https://jira.duraspace.org/browse/fcrepo-2753
* prerequisite for https://jira.duraspace.org/browse/fcrepo-2760

# what does this pull request do?
adds servlet container auth shiro authorization realm and filter, and implemented fedoraadmin role checking for webac.

# what's new?
implemented servlet auth classes for shiro that check the servlet request for user principal and roles and log in the user using those "credentials". also created a webac filter class and test config that enables the test auth filter, servlet container auth filter, and webac auth filter. currently the webac filter only checks for the fedoraadmin role. disable failing tests in the webac integration tests since they require implementation of acl parsing in the webac authorization realm.

# how should this be tested?

* run `mvn clean verify` on the fcrepo-auth-common and fcrepo-auth-webac projects

# additional notes:
this is the initial work for using shiro the pick up the servlet container authentication information and the skeleton of the webac filter for doing the actual permission checks. next steps of implementation work will be:

* implement the webac parsing in the authorization realm (https://jira.duraspace.org/browse/fcrepo-2760)
* implement the permission checks in the webac filter based on the nature of the request (current read and write modes, as well as the new append and control modes)

# interested parties
@fcrepo4/committers

##Repo ID: 25216

##Contributer ID: 79831

##Pull Request ID: 251904

###Profanity Found
**Text**
equivalent results to dbscan, but allows execution on arbitrarily large datasets. after initial construction, allows multiple 'scans' to quickly extract dbscan clusters at variable epsilon distances

algorithm is tested and validated, but not yet optimized. tested on 70k points (successful); currently testing on 2 x 10^9 lidar points (pending)

first commit; would appreciate any advice on changes to help code conform to the scikit-learn api

example usage in examples folder


##Repo ID: 25240

##Contributer ID: 129704

##Pull Request ID: 224085

###Profanity Found
**Text**
relates to: https://github.com/archivematica/issues/issues/943

initial attempt at making mcpclient process and resource usage more consistent.

### background ###

we have two somewhat conflicting targets for mcpclient performance: a) processing time for a single large transfer and b) total processing time for many simultaneous transfers. this pr attempts to improve b), without having a signifigant impact on a).

this approach makes no changes to the interface between mcpclient and server (gearman, or the format of data used by gearman. it makes minor changes to the `job` api but it should not require any major rework.

### previous forking model ###

detailed in https://github.com/archivematica/issues/issues/943, the previous model would start a process pool only when processing a client script that required it. a single gearman worker relayed results to mcpserver.

### updated forking model ###

this pr creates a process pool of on initial startup. each process is essentially an independent mcpclient; it receives work via gearman, and communicates the results that way as well. however in this case, unless a client script is marked as safe for concurrent instances, only one process in the pool will handle tasks of that type.

processes are restarted on exit, and will be restarted automatically after processing a certain number of jobs, to try to mitigate any memory leaks.

note that tasks are still broken up into batches, and this pr will probably work better with a lower batch_size setting than the current default of 128.

### todos ###

- [ ] more testing
- [ ] unit test coverage
- [ ] document how things work
- [ ] add config option for number of client processes
- [ ] add config option for reducing the number of processes used by bagit (on top of everything else)


##Repo ID: 25208

##Contributer ID: 79376

##Pull Request ID: 263121

###Profanity Found
**Text**
this add support for some of the popular activerecord callbacks to activeresource: 

before_validation, after_validation, before_save, around_save, after_save, before_create, around_create, after_create, before_update, around_update, after_update, before_destroy, around_destroy, after_destroy.

this an initial work, i will start to work soon adding support for contexts in *_validation callbacks (ex. before_validation :on => create) but first i want do add context support to existing validations (ex. validates :on => :create)


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 232950

###Profanity Found
**Text**
resolution for issue 2074

default values that are dependent on other attributes aren't getting set in after_initialize if create is called with a block to set the initial attributes.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 233176

###Profanity Found
**Text**
it would seem that `formoptionshelper#options_for_select` uses some syntactic sugar (`symbol#to_proc`) which can cause severe performance problems under certain circumstances, when using `ruby 1.8.7` w/ `rails 3-1-stable`

in my case, i was rendering a page with 10 selects of about 700 options each (there is a use case for that, trust me), and after the first couple of requests it would take as long as 8 seconds more, per request (from 300ms to ~9secs). eeek!

after a long session with `perftools.rb` and `rack-perftools_profiler` i managed to track it down to `options_for_select` and its use of `map(&:to_s)`. the symptoms were seemingly random, long, garbage collection pauses, in the middle of a request.

`perftools.rb` pointed me to `array.map` creating tens of thousands of `proc` objects as a side-effect of calling `symbol#to_proc`. 

depending on the initial free memory allocation, garbage collection would not kick in until after 800mb of memory needed to be inspected by the gc. unsurprisingly, my machine would stop responding during those long gc pauses.

i have not managed to reproduce with code the long gc pauses, i guess they need to happen inside the rails rendering pipeline and under a specific memory situation, but i have managed to benchmark a significant improvement when replacing `symbol#to_proc` with a block:

```
https://gist.github.com/1109416
```

the results:

```
using ruby 1.8.7 (2011-02-18 patchlevel 334) [i686-darwin10.7.0], mbari 0x6770, 
ruby enterprise edition 2011.03

rehearsal --------------------------------------------------------
using symbol#to_proc   3.520000   0.060000   3.580000 (  3.594295)
standard call          2.890000   0.020000   2.910000 (  3.038064)
----------------------------------------------- total: 6.490000sec

                           user     system      total        real
using symbol#to_proc   3.750000   0.060000   3.810000 (  3.856077)
standard call          2.690000   0.010000   2.700000 (  2.713586)
```

now, i know 3.1 is only offering token ruby 1.8.7 support and that 3.2 will most likely require 1.9.2, but this can be a real performance problem in real-world applications. one not worth not addressing for the sake of a bit of syntactic sugar...

the fix in this pull request should have zero side-effects and would save the mane of many a developer. 


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 233270

###Profanity Found
**Text**
they existed since initial rails commit by dhh but lost use a long time
ago


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 234612

###Profanity Found
**Text**
remove unused private method `yaml_fixtures_key`.

this method was introduced in the initial commit in 2004, and has been removed form `master` in #4254.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 235775

###Profanity Found
**Text**
...ing, fixes #6393

this happens when a has_many many b and a accepts_nested_attributes b that has a numeric colum
with initial 0 value. so a.update_attributes({:b_attributes => { :id => b.id, :numeric => 'foo' }})
passes the validation test but, the value of :numeric doesn't change.
his commit forces that the update fails with the above conditions.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 236057

###Profanity Found
**Text**
this was changed to use 1.9 string#encode method, however under the initial commit (https://github.com/rails/rails/commit/63cd9432265a32d222353b535d60333c2a6a5125#activesupport/lib/active_support/core_ext/string/output_safety.rb) there was a performance test done (https://gist.github.com/50ec9ab8ae1e223f3b75) by @seanwalbran and i have verified that the results for myself (including our team and server boxes) are consistent with him (results here: https://gist.github.com/3218839).

this issue was found on a project upgrade from 3.0.12 to 3.2.6 making our site 100x slower rendering views. after profiling and such we patched back this method and have got our performance.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 236402

###Profanity Found
**Text**
i'm submitting this pull request because of some confusion i had using this method (and its alias). when i originally tried the method, i attempted to do something like `time_ago_in_words 15.minutes` which now i realize was an error on my part because this method expects its argument to be a `time`.

my initial reaction was that this is a pretty obvious bug in rails since it didn't jump out to me in the docs that the argument must be a `time` and writing it as `time_ago_in_words 15.minutes.ago` felt a little clumsy with the "ago" redundancy.

it was even a little more confusing going from using the `distance_of_time_in_words` method with simple `15.minutes` (because the default `from_time` is simply `0`) to the alias method `distance_of_time_in_words_to_now` and having to supply a `time`.

anyway, at the very least, it seems some minor improvements to the docs (perhaps what i've attached?) may help the situation, and at the most perhaps some retinkering of this api (a job i currently feel unqualified of).

thanks for the awesome work!


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 236507

###Profanity Found
**Text**
we do a lot of isolated tests. this process revelad that some modules of `activemodel` can not be required by itself. i created a test script to verify, that all the parts of `activemodel` can be loaded in isolation. the initial output of the script was:

```
verifying active_model/attribute_methods: failed (uninitialized constant activemodel::attributemethods::activesupport)
verifying active_model/callbacks: done
verifying active_model/conversion: failed (uninitialized constant activesupport::concern)
verifying active_model/dirty: failed (uninitialized constant activemodel::attributemethods::activesupport)
verifying active_model/errors: done
verifying active_model/model: done
verifying active_model/naming: failed (undefined method `delegate' for activemodel::name:class)
verifying active_model/observing: failed (uninitialized constant activesupport::concern)
verifying active_model/serialization: done
verifying active_model/translation: failed (uninitialized constant activemodel::naming)
verifying active_model/validations: failed (undefined method `alias_method_chain' for range:class)
```

i added the necessary require statements to the `activemodel` parts to make every piece loadable.

i placed the script under `test/load_individual_parts.rb` but i was not sure how to integrate it into the test suite. currently you can execute it using:

`bundle exec ruby test/load_individual_parts.rb`
#### cleanup
- there were some broken whitespace (non-breaking). i cleaned those up.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 237115

###Profanity Found
**Text**
following on the initial work of @carlosantoniodasilva in https://github.com/rails/rails/commit/daa7b4e2f0f045af0dbecc6f531976fe68132cab, i decided to apply this change throughout the various projects in this repo.

most of the tests that use `assert !` instead of `refute` were written before minitest was a part of rails. now that we have minitest at our disposal, we should use its features to clean up the tests.

this is a cosmetic change but i believe it makes the tests easier to read, in the same way that `unless` is often (but not always) preferable to `if !`.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 237152

###Profanity Found
**Text**
i'm going to be taking a look at all of the guides as we get closer to the rails 4 release. i've done a bunch of work in docrails already, but with these bigger changes to the guides, i figured that a pull request would be best.

here are some initial thoughts on improving the migration guide. most of the content changes are at the beginning. obviously, this will probably be squashed before it's merged.

/cc @fxn @vijaydev


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 237156

###Profanity Found
**Text**
this class is an initial implementation of html5 sse for rails. currently we provide 2 kinds of ways to implement a sse server. the first is controller level sse, in which we do not distinguish clients and will send data to all the clients that subscribe the same sse source.
the second is client level sse, which we do distinguish clients and the data sent to different client can be totally different.
## controlller level sse:

``` ruby
class mysse < actioncontroller::base
  include actioncontroller::live
  include actioncontroller::serversentevents
  extend actioncontroller::serversentevents::classmethods
end
```

in this way, an action named `sse_source` will be created automaticlly and you can use `mysse.send_sse` or `mysse.send_sse_hash` to send event to all clients that subscribed the sse_source (you should register the action in route.rb manually)
## client level sse(session awared):

``` ruby
class mysse < actioncontroller::base
  include actioncontroller::live
  include actioncontroller::serversentevents

  def event
    start_serve do |sse_client|
      # we can access some session variables here
      sse_client.send_sse sse
      sse_client.send_sse_hash :data => "david"
    end

  end
end
```

please note that controller level sse and client level sse are not meant to
work together in the same controller.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 238255

###Profanity Found
**Text**
in preparing https://github.com/rails/rails/pull/11855, it took me a
minute to understand what was going on due to naming (parts refers first
to an attr_accessor, then to a local, and is then reassigned), but also
because the iterator conditionally builds nulls and then removes them.

i refactored to something much more functional-looking that i find
easier to read, but you may or may not. if you do, great! enjoy! if
not, oh well, i tried. can't win 'em all :)

rationale:
- no name conflict between local var and attr_accessor
- no reassignment of local var
- algorithm spelled out in steps
- unused items in initial list filtered out early
- empty-list case handled early instead of reassigning local var
- no duplication of formatting strings ("0 seconds")

benchmarks (after pr #11855 merged):

```
10000.times do
  1.second.inspect
end

original #inspect
   0.350000   0.000000   0.350000 (  0.354709)
   0.330000   0.000000   0.330000 (  0.331885)
   0.330000   0.000000   0.330000 (  0.334441)

refactored #inspect
   0.340000   0.000000   0.340000 (  0.340080)
   0.340000   0.010000   0.350000 (  0.345069)
   0.330000   0.000000   0.330000 (  0.335873)

10000.times do
  (1.day + 1.month + 2.minutes + 1.day).inspect
end

original #inspect
   0.400000   0.000000   0.400000 (  0.403027)
   0.400000   0.000000   0.400000 (  0.403781)
   0.390000   0.000000   0.390000 (  0.387596)

refactored #inspect
   0.400000   0.010000   0.410000 (  0.399792)
   0.400000   0.000000   0.400000 (  0.404145)
   0.400000   0.000000   0.400000 (  0.403820)
```


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 239491

###Profanity Found
**Text**
this patch prevents leaks on the following global variables:
- `time.zone`
- `activerecord::base.default_timezone`
- `activerecord::base.time_zone_aware_attributes`

the new helper `with_timezone_config` allows to adjust the state for a single test-case and makes sure to restore the initial state. i removed all other assignments to this global state from the test-cases.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 239974

###Profanity Found
**Text**
tldr: always return an object that responds to the query methods from request.format, and do not touch mime::type[] lookup to avoid bugs.

_please do not merge._

---

long version:

the initial issue was about being able to do checks like request.format.html? for request with an unknown format, where request.format would be nil.

this is where the issue came from at first in #7837 and #8085 (merged in cba05887dc3b56a46a9fe2779b6b228880b49622), but the implementation went down the path of adding this to the mime type lookup logic.

this unfortunately introduced subtle bugs, for instance in the merged commit [a test related to send_file had to be changed](https://github.com/rails/rails/commit/cba05887dc3b56a46a9fe2779b6b228880b49622#diff-00933fde66bed68a3d2ec7400b2c0b79l147) to accomodate the introduction of the nulltype.

later another bug was found in #13064, related to the content-type being shown as `#<mime::nulltype:...>` for templates with localized extensions but no format included. this one was fixed in #13133, merged in 43962d6ec50f918c9970bd3cd4b6ee5c7f7426ed.

besides that, custom handlers were not receiving the proper template formats anymore when passing through the rendering process, because of the nulltype addition. that was found while migrating an application from 3.2 to 4.0 that uses the markerb gem (a custom handler that generates both text and html emails from a markdown template).

---

this changes the implementation moving away from returning this null object from the mime lookup, and still fixes the initial issue where request.format.zomg? would raise an exception for unknown formats due to request.format being nil.

it is worth noticing that [all tests](https://github.com/rails/rails/commit/cba05887dc3b56a46a9fe2779b6b228880b49622#diff-cd75c7c20db7e5ab5d2534f7f28227b8r594) that [were added](https://github.com/rails/rails/commit/43962d6ec50f918c9970bd3cd4b6ee5c7f7426ed#diff-38f248f3c2154919879939f3fd0dee42r38) by this "feature" have been kept and are working fine. if that's acceptable i'll backport to 4-0-stable accordingly.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 240504

###Profanity Found
**Text**
see https://github.com/rails/rails/pull/13463#issuecomment-31480799 for full conversation.

i'm still looking into behavior of active record concerning environment variables. i would like to address consistency of behavior across multiple ways ar can be used, and re-visit the bike shed that is naming environment variables.

**tl;dr** i'm working on making behavior of active record consistent across all scenarios with regard to `database_url` being present. i'm also recommending we switch back to using `database_url` in the `database.yml` file. for more info read my super long explanations below.
## consistency of environments

here are all the ways that ar initiates a connection today:
- stand alone (without rails)
  - `rake db:<tasks>`
  - activerecord.establish_connection
- with rails 
  - `rake db:<tasks>`
  - `rails <server> | <console>`
  - `rails dbconsole`

we should make all of these behave exactly the same way, which if you dig into ar is non-trivial. i'm working to see if i can put all of this logic in one place for consistency, but as i mentioned, it's a non-trivial task.

currently ar can be configured via the environment variable `database_url` or by manually injecting a hash of values which is what rails does, reading in `database.yml` and setting ar appropriately. ar expects to be able to use `database_url` without the use of rails, and we cannot rip out this functionality without deprecating imho. this presents a problem though when both config is set, and a `database_url` is present. currently the `database_url` should "win" and none of the values in `database.yml` are used. this is somewhat unexpected to me if i were to set values such as `pool` in the `production:` group of `database.yml` they are ignored. here is my prosed matrix of how this behavior should work:

```
no database.yml
no database_url
=> error
```

```
database.yml present
no database_url
=> use database.yml configuration
```

```
no database.yml
database_url present
=> use database_url configuration
```

```
database.yml present
database_url present
=> merged into `url` sub key. if both specify `url` sub key, the `database.yml` `url` 
   sub key "wins". if other paramaters `adapter` or `database` are specified in yaml, 
   they are discarded as the `url` sub key "wins".
```
### implementation

i'm currently working on getting the above to work and be consistent with **all** environments, the last barrier i have to overcome is the rake tasks. i expect this last bit to take 80% of the effort. this also brings me to my second topic: env var naming.
## env var naming

as i mentioned above, ar already has built in support for `database_url` and as of today if `database_url` is present, the `database.yml` values won't be used at all. if i am able to implement and get accepted my above proposal, this won't be much of an issue but right now it is. 

i was originally :+1: on name-spacing the environment variables with `rails_` though after digging in ar for a few days and thinking about it more, i think we should use non-namespaced urls, so `database_url` instead of `rails_database_url`. why?

`database_url` isn't just a rails concept, it's actually used in other frameworks, most notably: [database_url is used in django](http://django-environ.readthedocs.org/en/latest/#devmode). and there's no reason it cannot be used in other frameworks.

one of the initial reasons for namespacing was to prevent conflicts between different languages running on the same box. i think this is the minority case, a more likely use case would be multiple rails applications on the same box. using the `rails_` namespacing would do nothing to help there. if you wanted truly multi-tennant database url connections they would need to be something like `rails_<appname>_<uuid>_database_url` which is unweildy to work with and likely causes more problems than it solves. 

deployment seems to be leaning towards using containers (through lxc, docker, or similar) which allows you to set a clean `env` per each app. if you need to deploy multiple apps to one box, you can use `.env` files, or your own custom `database.yml` setup. any of these solutions eliminate the problem of cross app env var contamination.

by keeping this value standard, you could have your container generation code create a `database_url` env var by default, and not have to worry about it. the alternative isn't horrible, you just alias `export rails_database_url=$database_url` but as i mentioned before, unless i (or someone else) fixes the above behavior this will cause unexpected behavior in your app, as `database.yml` gets ignored :grimmace:

i'm out to lunch on namespacing of `secret_key_base`, it's not already a pseudo-standard the way that `database_url` has become. i also see no real benefit of keeping the `rails_` namespace. 

i'm interested in talking about this point more, right now i would recommend switching back from `rails_database_url` => `database_url`. i'm happy to do all the conversion work here.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 240618

###Profanity Found
**Text**
this changes `enum` to use string values when the underlying databse column has the type `:string`.

for example:

```
create_table examples do |t|
  t.column :status, :string, default: 'ok'
end

class example < activerecord::base
  enum status: [:ok, :not_ok]
end

example = example.new
example.status = :ok
example.save
# => <example id: 1, status: 'ok'>
```

i'm sure there might be a couple of improvements that could be made to this pr, i would be really grateful for your feedback and glad to make some changes.

one thing i couldn't decide upon while working on this is whether `enum` should inspect the type of the underlying database column or if the user should pass a flag when calling `enum`. i opted for the former, as the latter would require redefining the `enum` method to be something like what follows and i wasn't sure what the policy/procedure for making potentially breaking changes is:

```
def enum(attribute_name, values, use_strings = false) 
  ... 
end
```

edit: after the initial failed travis build i limited this change to only `:string` columns.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 240924

###Profanity Found
**Text**
commit 4f2cd3e9 introduced a bug by reordering the call to
`@controller.recycle!` above the call to `build_request_uri`. the
impact of this was that the `@_url_options` cache ends up not being
reset between building a request uri (occurring within the test
controller) and the firing of the actual request.

we encountered this bug because we had the following setup:

``` ruby
  class minimumreproduciblecontroller < actioncontroller::base
    before_filter { @param = 'param' }

    def index
      render text: url_for(params)
    end

    def default_url_options
      { custom_opt: @param }
    end
  end

  def test_index
    get :index # builds url, then fires actual request
  end
```

the initial call to `get :index` in the test suite would populate the
@_url_options cache. the subsequent call to `url_for` would depend on
the cache, thus never calling the now-updated default_url_options.

this commit fixes this bug calling recycle! twice, and removes a call
to set response_body, which should no longer be needed since we're
recycling the request object explicitly.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 240945

###Profanity Found
**Text**
now the initial value of `activerecord.default_timezone` is always :utc.
but rails guide say 

> although active record defaults to `:local` when used outside of rails.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241050

###Profanity Found
**Text**
prior to rails 4.0.4 when touching a object which doesn't have timestamp
attributes (updated_at / updated_on) rails would still touch all
associations. after 73ba2c14cd7d7dfb2d132b18c47ade995401736f it updates
associations but rollsback because `touch` would return nil since
there's no timestamp attribute.

this sounds a bit insane (touching an object without timestamps) but i came through it today while upgrading and just felt like reporting anyway due to being a change of behaviour between minor releases.

the following would pass on 4.0.3 but fails on 4.0.4

``` ruby
unless file.exist?('gemfile')
  file.write('gemfile', <<-gemfile)
    source 'https://rubygems.org'
    gem 'rails', path: '../rails'
    gem 'sqlite3'
  gemfile

  system 'bundle'
end

require 'bundler'
bundler.setup(:default)

require 'active_record'
require 'minitest/autorun'
require 'logger'

activerecord::base.establish_connection(adapter: 'sqlite3', database: ':memory:')
activerecord::base.logger = logger.new(stdout)

activerecord::schema.define do
  create_table :products do |t|
    t.timestamps
  end

  create_table :assets do |t|
    t.integer :product_id
  end
end

class product < activerecord::base
  has_many :assets
end

class asset < activerecord::base
  belongs_to :product, touch: true
end

class bugtest < minitest::unit::testcase
  def test_association_stuff
    product = product.create!
    image = asset.create! product: product
    initial = product.reload.updated_at
    image.touch

    refute_equal initial, product.reload.updated_at
  end
end
```


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241101

###Profanity Found
**Text**
native ruby `string#prepend` modifies instance in-place, while `activesupport::safebuffer` returns modified version, but the initial object remains unchanged.

``` ruby
a = "bar"           # => "bar"
a.prepend "foo"     # => "foobar"
a                   # => "foobar"
b = "bar".html_safe # => "bar"
b.class             # => activesupport::safebuffer
b.prepend "foo"     # => "foobar"
b                   # => "bar", expected "foobar"
```


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241179

###Profanity Found
**Text**
for example, if i have a model countriesuser which belongs to a relation countries_users, and corresponding table, i'm able to use callback for the model, when add a relation with `country.users << user`. so, for example, the state_machine initial value will set properly, and any callback like, `after_create` will be issued.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241278

###Profanity Found
**Text**
perhaps, raise of error when **same** module gets loaded twice isn't best choice

this happens when module files are loaded first time (e.g. while app reloading) and further required by hand (because some lib don't expect such preloading) - e.g. see ctran/annotate_models#181 for

```
unable to annotate concerns/promotional.rb:
cannot define multiple 'included' blocks for a concern
```

see #10652 and #10650 for initial idea.
also checked, that proc#source_location works on jruby & rbx, too


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241342

###Profanity Found
**Text**
 when an object with a binary column is updated with a nil value in that column, the sql logger would throw an exception when trying to log that nil value. this only occurs when updating a record that already has a non-nil value in that column since an initial nil value isn't included in the sql anyway (at least, when dirty checking is enabled.) the column's new value will now be logged as `<null binary data>` to parallel the existing `<n bytes of binary data>` for non-nil values.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241444

###Profanity Found
**Text**
when an object with a binary column is updated with a nil value in that column, the sql logger would throw an exception when trying to log that nil value. this only occurs when updating a record that already has a non-nil value in that column since an initial nil value isn't included in the sql anyway (at least, when dirty checking is enabled.) the column's new value will now be logged as <null binary data> to parallel the existing <n bytes of binary data> for non-nil values.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241445

###Profanity Found
**Text**
as a result of all of the refactoring that's been done, it's now
possible for us to define a public api to allow users to specify
behavior. this is an initial implementation so that i can work off of it
in smaller pieces for additional features/refactorings.

the current behavior will continue to stay the same, though i'd like to
refactor towards the automatic schema detection being built off of this
api, and add the ability to opt out of automatic schema detection.

use cases:
- we can deprecate a lot of the edge cases around types, now that there
  is an alternate path for users who wish to maintain the same behavior.
- i intend to refactor serialized columns to be built on top of this
  api.
- gem and library maintainers are able to interact with `activerecord`
  at a slightly lower level in a more stable way.
- interesting ability to reverse the work flow of adding to the schema.
  model can become the single source of truth for the structure. we can
  compare that to what the database says the schema is, diff them, and
  generate a migration.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241690

###Profanity Found
**Text**
it seems that #where! is not designed to be used as a chained where.
see initial implementation at 8c2c60511beaad05a218e73c4918ab89fb1804f0.
so, no need to check twice.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 241691

###Profanity Found
**Text**
- this commit adds back the always_permitted_parameters configuration option to strong parameters.
- the initial pull requests where this feature was added are the following:
  - https://github.com/rails/rails/pull/12682
  - https://github.com/rails/strong_parameters/pull/174


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 242195

###Profanity Found
**Text**
the `db:schema:cache:dump` rake task dumps the database schema structure to `db/schema_cache.dump`. if this file is present, the schema details are loaded into the currently checked out connection by a railtie while rails is booting, to avoid having to query the database for its schema.

the schema cache dump is only applied to the initial connection used to boot the application though; other connections from the same pool are created with an empty schema cache, and still have to load the structure of each table directly from the database.

with this change, a copy of the schema cache is associated with the connection pool and applied to connections as they are created.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 243343

###Profanity Found
**Text**
currently the frozen state is not propagated through transaction changes (it's needed to be able to rollback to initial state) and it leads to an exception like #18191

it was introduced in 40496430d5825f55d1b8aa063f6642b82f6c65d5, during the time when `remember_transaction_record_state` was broken and during the revert it's gone unnoticed 9d2146ac6e4c1fdc9cc157d614b1eb9968ac6a2e

this is a rare case, but as the issue above shows still can happen.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 243736

###Profanity Found
**Text**
this is the initial stab at inviting guests. it's **not** ready for in-depth review yet. i would however appreciate any feedback you can throw at me from a high-level pov.

it builds on a couple of other prs, if you have any remarks about those, please file'em there.


##Repo ID: 25206

##Contributer ID: 79267

##Pull Request ID: 247580

###Profanity Found
**Text**
this should support the "my stuff".

there still needs to be some ui stuff associated to this, which is in development. so it's possible this doesn't turn out to meet 100% of the ui requirements. however, here it is for initial review if desired.

built on top of groupprofiles, of course. so that will need to be merged first.


##Repo ID: 25206

##Contributer ID: 177917

##Pull Request ID: 247636

###Profanity Found
**Text**
when logging in with auth method other than ils or multiils, the user doesn't have an initial library card. if one is added, it also needs to be activated so that user isn't prompted for credentials when trying to display loans etc.


##Repo ID: 25234

##Contributer ID: None

##Pull Request ID: 248444

###Profanity Found
**Text**
as already mentioned on the mailing list (http://sourceforge.net/p/vufind/mailman/message/33739794/) we are developing a foundation5 (http://foundation.zurb.com/) based theme for vufind 2.x

today, i am very happy to create the initial pull request with all the amazing work claas kazzer has done on creating the foundation5-based theme. we tested it locally with our vufind 2.4 codebase and it works fine, though there might be some bugs left - please don't hesitate to report those.

we would like to share this theme with the vufind community as an alternative to the bootstrap centered themes. its design is basic, but functional and can be adjusted to personal needs easily by using some styles.
claas has also prepared a detailed documentation what he needed to adjust and how the theme differs from the bootstrap-theme. this should get everyone going with the foundation5-theme. we would be happy to share this documentation e.g. via the vufind-wiki, too.

please let us know what you think!

best,
andré


##Repo ID: 25234

##Contributer ID: None

##Pull Request ID: 248463

###Profanity Found
**Text**
when running a keyword search, then choosing an author hyperlink from
the results to run an author facet search, the next/previous links in the
individual results would be based on the initial keyword search, not the facet
search.

this was for two reasons:
- the resultscroller was not active in the authorcontroller, which
  handles author facet searches
- the resultscroller retrieves the current search from the session to
  create the scrolling links, and author facet searches were configured to not
  be saved in the session

correct these two issues in authorcontroller, but only if
next_prev_navigation is enabled. because authorcontroller also handles
solrauthorfacet searches (searches that produce a list of authors, not a
list of titles by a specific author) and those results cannot be iterated
through by a resultscroller, we also have to make an additional fix in
the resultscroller plugin to handle the case where solrauthorfacet
result is passed to create the resultscroller, and prevent it from
being instantiated.


##Repo ID: 25234

##Contributer ID: None

##Pull Request ID: 248474

###Profanity Found
**Text**
… via ajax.

i've tried to make sure that:

1.) the hash is not updated on initial load of the record page 
2.) the hash is updated on moving to other tabs 
3.) the hash is also updated when moving back to the initial tab

moving some of the code out of the success handler in record.js helps update the tab state faster when loading the tab takes time.


##Repo ID: 25234

##Contributer ID: 181580

##Pull Request ID: 248594

###Profanity Found
**Text**
this is the code snippet to fix vufind-org/vufind#612

i also included some lenghty comment on this issue linking to the above mentioned pr and the initial pr removing the password-check. please feel free to shorten the comment if you think it's a little bit overkill ;)


##Repo ID: 25234

##Contributer ID: 81285

##Pull Request ID: 248698

###Profanity Found
**Text**
this is finally the long-promised proposed implementation of a search/record api for vufind. a very similar api has been in production use in finna for a while now, and for now there haven't been many issues with it.

the following design criteria were followed when the api endpoints were designed:
- easy to use with modern tools (json, cors, swagger specification).
- parameters as similar as possible to the search functionality in the vufind ui so that a search can made and filtered etc. and then parameters can then be easily moved to the api.
- extensible with local fields etc. as necessary.
- take advantage of record processing available in the record drivers to provide data that's ready for re-use.
- include version in the end points from the beginning so that new versions with possible incompatibilities can be created without affecting existing api users.
- use permissions so that e.g. ip address filters can be used to limit access to the api.
- others i can't remember right now :)

this implementation contains groundlaying work for apis and tries to take into account other endpoints too. that's why some of the common functionality is in a trait that can be shared between api controllers that extend other controllers.

there's currently no support for authorization or rate limits. we decided to provide the search functionality without limits, but if e.g. holdings information retrieval or other functionality affecting third parties is added, these will become relevant.

i haven't verified that a fully functional client can be created using the swagger spec, but at least it looks ok in the included swagger ui.

i would appreciate initial reactions before the vufind summit, but there's no rush to get this merged or anything before that.

todo:
- [x] wiki page
- [x] investigate possible issues with fetching records with special characters in the ids
- [x] controller cleanup?
  - [x] fix hierarchical facet translation broken by refactoring (use view helper instead of raw translator?)
- [x] create tests for new formatter classes.
  - [x] facetformatter
  - [x] recordformatter


##Repo ID: 25234

##Contributer ID: 178201

##Pull Request ID: 248903

###Profanity Found
**Text**
this is a discussion about putting a more public road map on the vufind wiki. this will add a readme detailing planned upcoming features of the project.

the benefit to putting a road map here as opposed to on the wiki is that suggestions to the road map can be opened as pull requests and discussed.

this initial push is based on the [share doc](http://tinyurl.com/vufindsummit2016) from the vufind summit 2016.


##Repo ID: 25234

##Contributer ID: 178202

##Pull Request ID: 248911

###Profanity Found
**Text**
i guess this is part of #1833 so the initial load window view can be populated with data. it has an indirect dependency on #1901 in order to make the data actually show up in the interface, but is independent and can be merged with or without it.

there's some obvious follow-on work to make sure we lazy-load manifests instead of immediately dispatching requests for data we might not even use, but this hopefully is sufficient for now.

##Repo ID: 25222

##Contributer ID: 168309

##Pull Request ID: 185071

###Profanity Found
**Text**
<!--- provide a general summary of your changes in the title above -->

## description
firefox tests using the built-in geckodriver have been broken for those running post-quantum (57.0) versions of firefox.  this pr updates the built-in linux and osx drivers, adds a check for os in rails_helper, removes `js:true` from the accessibility tests, and adds an initial readme for running public tests.

## related jira ticket or github issue
<!--- please link to the jira ticket or github issue here: -->

## motivation and context
some built-in firefox tests (those with the `js: true` flag) were failing on osx for users with updated versions of firefox.

## how has this been tested?
<!--- please describe in detail how you tested your changes. -->
<!--- include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
tests passed successfully on two different osx machines running latest stable releases of firefox (v. 63.0).

## screenshots (if appropriate):

## types of changes
<!--- what types of changes does your code introduce? put an `x` in all the boxes that apply: -->
- [x] bug fix (non-breaking change which fixes an issue)
- [ ] new feature (non-breaking change which adds functionality)
- [ ] breaking change (fix or feature that would cause existing functionality to change)

## checklist:
<!--- go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- if you're unsure about any of these, don't hesitate to ask. we're here to help! -->
- [x] my code follows the code style of this project.
- [x] my change requires a change to the documentation.
- [x] i have updated the documentation accordingly.
- [x] i have read the **contributing** document.
- [ ] i have added tests to cover my changes.
- [x] all new and existing tests passed.


##Repo ID: 25209

##Contributer ID: 79414

##Pull Request ID: 181154

###Profanity Found
**Text**
to solve #2411 i reimplemented the plugin system as an react context provider, meaning that the initial render method looks like that:

```
<provider store={this.store}>
  <pluginprovider plugins={plugins} createrootreducer={createrootreducer}>
    <app />
  </pluginprovider>
</provider>
```

there are other ways to do it, but this one seems to me the most react-ish solution.

also i think the plugin preprocessing code is now more expressive.

##Repo ID: 25222

##Contributer ID: 164891

##Pull Request ID: 185384

###Profanity Found
**Text**
in order to change `metadatanode`'s `:mime_type` property, we need to be able to
call `metadatanode.property` without a `.parent_class` set. this isn't possible
normally because `.property` is overridden after the initial definition of
`:mime_type` to patch in delegation to the parent class when a new property is
defined. that delegation fails when `.parent_class` is `nil`, as is the case on
the base `metadatanode` class.

we now only do that delegation if `.parent_class` is defined.

##Repo ID: 22034

##Contributer ID: 146260

##Pull Request ID: 188416

###Profanity Found
**Text**
after some thinking i think this is the cleanest way to change the fastica estimator according to the new compute_sources parameter.

ideally (if there were no users) the estimator wouldn't have a `compute_sources` init argument, because the use case is different: either you use `fastica.fit_transform`, in which case you call the underlying function with `compute_sources=true`, or you use `fastica.fit`, in which case it's more effective not to compute the sources, because presumably the user will subsequently call `.transform` on some other data.  (if they will use the same data, it's their fault for misusing the api)

in order to get there we need to deprecate the `fastica.sources_` attribute. because its computation depends on the initial data passed to `fit` i couldn't compute it lazily, so until the deprecation i propose to just compute it all the time.  (this is identical to what fastica did yesterday night before my nocturnal bugfix anyway).

alternatively if we want to make the estimator be able to save the memory, we could introduce a deprecated-since-birth init attribute `compute_sources`, `true` by default.  however i think this is just confusing for users; if people want to use fastica and save memory they should simply call the function directly.

in general i think the api can be rethought in many places, many estimators have tons of parameters that are only useful for speedup/optimization and all they do is expose the underlying functions with complicated logic.  i think that users who really work at the limit of their resources should go ahead and use the underlying public functions.

opinions?


##Repo ID: 25240

##Contributer ID: 129105

##Pull Request ID: 224221

###Profanity Found
**Text**
`gridcellprovider::__construct()` will store an initial `pkprequest` object, then use this request object for other methods rather than passing it as a parameter.

requires https://github.com/pkp/pkp-lib/pull/2445

part of stage one of pkp/pkp-lib#2444: specifically, the gridcellprovider component.


##Repo ID: 25226

##Contributer ID: 80830

##Pull Request ID: 199192

###Profanity Found
**Text**
this adds an initial [editorconfig](http://editorconfig.org/) to ensure that all files are encoded in utf-8 and end with a new line.

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 196457

###Profanity Found
**Text**
corrected test because of rubocop warning (single ] with no initial [). moving forward, run rubocop on more than just gemfiles. also added a few configuration items and excluded the docs directory.


##Repo ID: 25209

##Contributer ID: 79411

##Pull Request ID: 263571

###Profanity Found
**Text**
**what this pr does / why we need it**: initial documentation for local-to-s3 storage migration

**which issue(s) this pr closes**: 6771

closes #6771 

**special notes for your reviewer**: @landreev and @qqmyers should review

**suggestions on how to test this**: essentially just sql queries. have mercy on my restructured text formatting.

**does this pr introduce a user interface change?**: no

**is there a release notes update needed for this change?**: no

**additional documentation**: none


##Repo ID: 25213

##Contributer ID: 79641

##Pull Request ID: 278698

###Profanity Found
**Text**
---

**future tracking of snapcraft at https://github.com/jabref/jabref/issues/3121**

---

this outlines how we could get into the app store of ubuntu (https://developer.ubuntu.com/en/desktop/ and https://shop.canonical.com/index.php?cpath=19). the issue is that snap is only supported in ubuntu 16.04 lts. <s>thus, this pr fails. we have to interpret following gist https://gist.github.com/evandandrea/c754964bfdfb176844f26f605ebbb8db and try to adapt it.

it seems that the irc channel is the only help out there. the gradle support is very new (see https://github.com/snapcore/snapcraft/pull/912).

is there some linuxer out there who wants to take over?</s>

## howto install and update

- `snap install jabref --edge --devmode`
- `snap refresh jabref --edge --devmode`

## current state

[![snap status](https://build.snapcraft.io/badge/jabref/jabref.svg)](https://build.snapcraft.io/user/jabref/jabref)

- registered at https://build.snapcraft.io/user/koppor
- <s>travis is used for building as currently only circleci 2.0 is supported for building and we use circleci 1.0 for building. a switch to circleci 2.0 is tested at branch [circleci20](https://github.com/jabref/jabref/tree/circleci20), but does currently not work and it does not seem to be easy to get it running</s>
- <s>build takes approx. 9:30min</s>
- build will take place at `master` branch only (currently `snapcraft` only) to avoid much too much development versions at ubuntu.
 - [x] too long version strings (as we use) seem to be forbidden, we just use `4.0-dev`.
- [x] get initial `snapcraft.yaml` working
- [x] publish edge version to ubuntu's snap repository: https://dashboard.snapcraft.io/dev/snaps/7999/
- [ ] publish stable version to ubuntu's snap repository (https://uappexplorer.com/snaps) (currently no version visible) - has to be done manually
- [x] test at ubuntu 16.04
- [x] <s>get travis to work</s>
  - <s>blocked by https://forum.snapcraft.io/t/proxy-errors-on-large-uploads/1228</s>
  - <s>solved by uploading one build at a time</s>
- [x] icon in 256x256 for https://dashboard.snapcraft.io/dev/snaps/7999/update/?step=displaying
- [x] `javafx warning: warning: loading fxml document with javafx api of version 8.0.112 by javafx runtime of version 8.0.111` - we cannot do anything about that: openjfx is [version 8.0.111 in ubuntu zetsy](https://packages.ubuntu.com/de/zesty/openjfx).
- [ ] <s>work on transfer to https://code.launchpad.net/~jabref/+snaps for allowing building on ubuntu instead of build on travis</s>
- [ ] gradle binary cannot be downloaded from http://build.snapcraft.io. see: https://github.com/canonical-websites/build.snapcraft.io/issues/918

## steps after merging

- [ ] <s>adapt `travis.yml` to build snap only at the `master` branch (and not `snapcraft`).</s>

## howto build locally

1. `docker run -it -v /d/git-repositories/jabref/jabref:/tmp/snap koppor/docker-snapcraft-java-de bash`
2. `cd /tmp/jabref`
3. read along at https://snapcraft.io/docs/build-snaps/publish

## references

- http://snapcraft.io/docs/build-snaps/metadata 
- https://snapcraft.io/docs/build-snaps/publish
- https://wiki.ubuntu.com/snapcraft/parts

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 196465

###Profanity Found
**Text**
hello @mfelczak  and @natewr, added in the client's svgs and modified the width along with the source set location in each respective plugin. one thing to note is that there is another utilization of these graphics under /lib/pkp/templates/notification/index.tpl (except the image source set for that is under /lib/pkp/templates/images). i was wondering should i be adding the client's svg images to lib/pkp as well or simply to the plugins that he mentioned in his initial request.

p.s @natewr if the transparent text issue that you mentioned earlier is troublesome i could have a look it in adobe illustrator which supports svg modification and exporting.

thanks

##Repo ID: 25226

##Contributer ID: 80875

##Pull Request ID: 199296

###Profanity Found
**Text**
fixes #1543

modifications:
* collectionbehavior (model)
  * √ after_destroy gets rid of any permission templates for the collection
  * √ new method update_access_controls! add edit_users, edit_groups, read_users, and read_groups to solr doc based on permission template manage access

* permissionsservice
  * call update_access_controls in create_default method so solr_doc is updated with initial create

* permissiontemplate
  * √ new method source_model which returns either and admin set or a collection
  * √ new method collection which returns the collection for the permission template (if it is a collection and it exists; otherwise throws objectnotfound)
  * √ update method admin_set to return the admin_set for the permission template (if it is an admin set and it exists; otherwise throws objectnotfound)

* permissiontemplateform
  * √ delegate source_model to model so it picks up both admin sets and collections
  * √ delegate id to source_model ending up with form method source_id -- gives access to both admin sets and collections
  * update_management now calls `source_model.update_access_controls!` which both admin sets and collections define

* collectioncontroller
  * √ process permissions passed in params with create/update

tests:
* permission_templates factory
  * √ add with_collection support

* collection_spec
  * test after_destroy
  * test update_access_controls!
  * test collection factory

* permission_template_spec
  * test factory's with_collection parameter
  * test source_model returning admin_set, collection
  * test collection method
  * already has test for admin_set method

* permission_template_form_spec
  * update delegation check from admin_set to source_model
  * todo: generalize error message from admin_sets to collections and admin_sets


expected behavior changes:
* when you delete a collection, all related permission templates and access are also deleted
* when you add a participant, the solr doc edit/read access is updated for both admin sets and collections
* fixes bug that did not set admin_set creator with manage access when admin_set is created



##Repo ID: 22050

##Contributer ID: 85019

##Pull Request ID: 191970

###Profanity Found
**Text**
this is the initial commit for a finnish locale for ojs3. includes the ojs translations and some plugins.

tagging @mtub 

edit: pkp-lib in a while

##Repo ID: 25226

##Contributer ID: 80824

##Pull Request ID: 199062

###Profanity Found
**Text**
fix for #2572 
when running get fulltext, the dialog is now a save dialog which enables to select a different folder or even a different filename. the initial filename which jabref assigns is now also visible in the file dialog

<!-- describe the changes you have made here: what, why, ... -->

- [x] change in changelog.md described
~- [ ] tests created for changes~
~- [x] screenshots added (for bigger ui changes)
- [x] manually tested changed features in running jabref
~- [ ] check documentation status (issue created for outdated help page at [help.jabref.org]~(https://github.com/jabref/help.jabref.org/issues)?)
~- [ ] if you changed the localization: did you run `gradle localizationupdate`?~


![savefile](https://cloud.githubusercontent.com/assets/320228/23722891/60519cd2-0447-11e7-8628-ed9d53c99326.png)

![grafik](https://cloud.githubusercontent.com/assets/320228/23722873/530ed71a-0447-11e7-8e1a-be3bd5273eaa.png)


##Repo ID: 25219

##Contributer ID: 80091

##Pull Request ID: 196619

###Profanity Found
**Text**
i'd like to improve the code documentation of jabref to make is easier for newcomers to understand the code. one part of that is to document the ideas behind of some code. this pr adds an initial directory and template for that.

i tried to collect background information at http://adr.github.io/.

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 196806

###Profanity Found
**Text**
this pr is for initial discussion of the new vue.js integration. when reviewing the code, it's not recommended to commit-by-commit. this branch includes a number of early commits which integrated a backbone.js event router, then swapped it out for vue.js.

##Repo ID: 25226

##Contributer ID: 80814

##Pull Request ID: 199139

###Profanity Found
**Text**
is there a case when we never just want to zoom immediately on initial load?

##Repo ID: 25222

##Contributer ID: 79473

##Pull Request ID: 185341

###Profanity Found
**Text**
fixes #1343

(collections extensions sprint)

adds basic model, specs, and a factory for collection types.  the model in this initial iteration does not have validations on fields but can be added as the requirements for them are defined.  it also does not address the questions of participant assignment/permission templates raised in #1343 . 

##Repo ID: 22050

##Contributer ID: 79852

##Pull Request ID: 191846

###Profanity Found
**Text**
many of the selenium tests start by opening a new notebook and writing text in some cells through the interface, just to set up the conditions for what they're really testing. this is slightly awkward, because you need a different method to change the initial empty cell versus adding new cells. it also takes a little bit of time, as it involves a number of selenium calls.

this adds a `prefill_notebook` fixture which can create a notebook file with some content, and then opens that in the browser. the content can be a list of nbformat cell objects or strings (which are treated as code cells). i believe this makes the test code more readable by condensing boilerplate to set up notebook state.

##Repo ID: 25237

##Contributer ID: 178064

##Pull Request ID: 259105

###Profanity Found
**Text**
an initial stab at a second attempt at https://github.com/scikit-learn/scikit-learn/pull/11890, building on top of master, with the test suite to be expanded...

##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 259358

###Profanity Found
**Text**
#### reference issues/prs
fixes issue #14398

#### what does this implement/fix? explain your changes.
by default, sklearn's gmm is initiated by k-means. when the features are of very different scales, this can lead to a poor choice of initial conditions for the gmm parameters and, as a result, a poor fit once trained. have added:

- automatic scaling of data before k-means is used to initiate gmm.

- test where the gmm is trained on data where the features have very different scales.

#### any other comments?

- for the test, data is not generated using the randomdata class as i couldn't see an obvious way of setting the covariance matrix to what we need it to be for this example. my code that generates samples isn't elegant but is hopefully readable.

- the test reflects the example raised in the original issue. 

- the test only looks at the ability of the gmm to estimate the means of the example, as this seemed sufficient. i could add a test of the covariance matrices if we think it's needed?

- over 1000 runs, old code failed the test every time and new code passed every time.


##Repo ID: 25240

##Contributer ID: None

##Pull Request ID: 259697

###Profanity Found
**Text**
i am still facing the following problems:

i wasn't able to update the viewport for newly created windows, because there seems to be an a temporal dependency between the dispatch of `add_window` and `update_viewport`. the viewport can only be updated when the window is already created and there seems to be no possbility to pass an initial viewport configuration when creating a new window.

i wasn't able to update the viewport for newly created windows, because there seems to be an a temporal dependency between the dispatch of `add_window` and `update_viewport`. the viewport can only be updated when the window is already created and there seems to be no possbility to pass an initial viewport configuration when creating a new window.

while trying to write an integration test for the confiugration import i was struggeling with an expect-puppeteer bug (https://github.com/smooth-code/jest-puppeteer/issues/150) that prevents me from fill out the config import textarea. i also tried setting the textarea's value by manipulation the dom element directly:

```
await page.exposefunction('gettextvalue', () => return textvalue ); // textvalue is the stringified config object
await page.waitforselector('#workspace-import-input');
await page.$eval('#workspace-import-input', el => window.gettextvalue());
```

but this way i ran into a timeout.

##Repo ID: 25222

##Contributer ID: 80393

##Pull Request ID: 185118

###Profanity Found
**Text**
i have created an initial port of the fileannotationtab. it is not done yet, as i am not so proficient in gui programming.
fixes https://github.com/jabref/jabref/issues/2922
fixes https://github.com/jabref/jabref/issues/3059

- [x] test if multiple linked files are working
- [x] add reload annotations button
- [x] add copy to clipboard button
- [x] check if this pr fixes  https://github.com/jabref/jabref/issues/3059
- [x] remove unused variables
- [x] is it possible to get a nicer binding? at the moment we have 5 stringproperties instead of one objectproperty<fileannotation>
- [x] fix npe when clicking copy annotations, if there are no annotations
- [x] fix reload annotaitons button
- [x] add fileannotationstab when adding a file (without reopening the entry editor)
- [x] fix design glitches (first line of right side)
- [ ] fix annotation auto-selection when switching between linked files

##Repo ID: 25219

##Contributer ID: 164836

##Pull Request ID: 196823

###Profanity Found
**Text**
this is still a work in progress. i still have to test a few things:
- [ ] check that it works well with different datatypes (the cython code assumes that it's receiving floats)
- [ ] check if it could be a good idea to raise a warning when the factorization isn't working (the gradient is added to multiple items in the factor, thereby they will diverge if the learning rate is too high. but it may no be a good idea to simply reject some learning rate values, because they could work with another initial values of the factors)
- [ ] print warnings if rows/columns only contains missing values
- [ ] add a better way to test the score in the imputer
- [ ] replace the parameters init_\* in the constructor by a different one that could be used with grid_search
- [ ] finish docstrings
- [ ] run pep8, pyflakes, ...
- [ ] fix the build (i have an error with another module, probably a rookie mistake with the imports)


##Repo ID: 25240

##Contributer ID: 129664

##Pull Request ID: 224329

###Profanity Found
**Text**
here is an initial implementation of "frbr" for vufind. this is based on work identification keys in solr index.

about naming: i've used the term "work keys" and similar in the backend code, and "versions" in the front end code. this can be revisited if necessary. like everything here.

also included is sample indexer configuration for creating work keys. this should be good to go. it's not perfect (in this case i don't think anything will be), but should be at least a good starting point. 

this allows versions to work whether the new versions tab is enabled or not. if not, versions are always displayed as a search.

basic principles:

- uniform titles work as keys alone
- other titles need author information with them

i won't be able to work on this much more at the moment due to my leave, but feel free to pick up if you find this interesting enough. :)

todo:

- [ ] should the search link actually contain the record id instead of keys? this would need extra handling in search parameters code, and would also mean that if the record is no longer available, the search wouldn't work either.
- [ ] make the search terms look nicer
- [ ] make indexing ignore non-filing characters
- [ ] make indexing fold the characters to ascii instead of quietly dropping them (see [metadatautils.php](https://github.com/natlibfi/recordmanager/blob/master/src/recordmanager/base/utils/metadatautils.php#l106))?
- [ ] port work keys logic to php so it can be used in xml imports as well.
- [ ] test everything
- [ ] do we want to include alternate script support (880 field in marc 21)?
- [ ] document in wiki when merging.
- [ ] resolve [vufind-120](https://vufind.org/jira/browse/vufind-120) when merging.

##Repo ID: 25234

##Contributer ID: 178201

##Pull Request ID: 263968

###Profanity Found
**Text**
<!-- describe the changes you have made here: what, why, ... -->

i just remembered that my initial motivation to convert the entry editor to javafx came from my desire to display the integrity check messages directly in the entry editor. this pr accomplishes exactly this. 
![image](https://user-images.githubusercontent.com/5037600/29142996-f7732d44-7d53-11e7-9461-bbd06e90697a.png)
the location and style of the tooltip is not perfect but as of now these things cannot be changed since they are hardcoded in `controlsfx` (will create a feature request).

what do you think, should this still merged before the beta3 release? in the end it is only a minor change and shouldn't break anything.

- [x] change in changelog.md described
- [ ] tests created for changes
- [x] screenshots added (for bigger ui changes)
- [x] manually tested changed features in running jabref
- [ ] check documentation status (issue created for outdated help page at [help.jabref.org](https://github.com/jabref/help.jabref.org/issues)?)
- [ ] if you changed the localization: did you run `gradle localizationupdate`?


##Repo ID: 25219

##Contributer ID: 80088

##Pull Request ID: 196828

###Profanity Found
**Text**
<!--- provide a general summary of your changes in the title above -->
response to initial tester feedback from joshua shaw.  this commit includes the following 2 updates:

- public pdf now provides the language of description translation value (not code).
- ead3 export now includes required <p> tags around <descriptivenote>.

## description
<!--- describe your changes in detail -->

## related jira ticket or github issue
<!--- please link to the jira ticket or github issue here: -->
https://archivesspace.atlassian.net/projects/anw/issues/anw-382

## motivation and context
<!--- why is this change required? what problem does it solve? -->

## how has this been tested?
<!--- please describe in detail how you tested your changes. -->
<!--- include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
tested manually.  existing tests passed.

## screenshots (if appropriate):

## types of changes
<!--- what types of changes does your code introduce? put an `x` in all the boxes that apply: -->
- [ ] bug fix (non-breaking change which fixes an issue)
- [x] new feature (non-breaking change which adds functionality)
- [ ] breaking change (fix or feature that would cause existing functionality to change)

## checklist:
<!--- go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- if you're unsure about any of these, don't hesitate to ask. we're here to help! -->
- [x] my code follows the code style of this project.
- [ ] my change requires a change to the documentation.
- [ ] i have updated the documentation accordingly.
- [x] i have read the **contributing** document.
- [ ] i have added tests to cover my changes.
- [x] all new and existing tests passed.


##Repo ID: 25209

##Contributer ID: 79414

##Pull Request ID: 181386

###Profanity Found
**Text**
fixes #1499 this work was sponsored by [palni](http://www.palni.org)

brings in and configures the existing blackight-oai gem. 

this allows each tenant to have a /catalog/oai endpoint which provides oai-pmh access to the collections within.  this is an initial feature offering, so i'm expecting it to become more sophisticated over time.

<img width="1680" alt="screen shot 2019-03-17 at 8 14 45 pm" src="https://user-images.githubusercontent.com/1054448/54504573-72b08500-48f1-11e9-946a-fb93559edf5d.png">


@samvera/hyrax-code-reviewers

##Repo ID: 22047

##Contributer ID: 85058

##Pull Request ID: 190605

###Profanity Found
**Text**
moves forward issue #1349 ; 

the initial collection types index page, markup, and basic ui wired up.  still needs completion of other stories to be fully functional.

@samvera/hyrax-code-reviewers

#### issues addressing remaining work:
 -  #1341 - we added a `collections?` method to the collectionstype model so that we could simulate different modals for empty vs full collection types. this will need to be changed when we have implemented a way to find collections that belong to a collection type.
 - #1524 - added `collection_type.machine_id != 'admin_set'` as a placeholder to check if the collection type was admin set. not sure what the final check will be yet.
 - #1341, #1525 - actual delete functionality not wired up yet
 - #1526 - button to take you to 'view collections of this type' (if unable to delete because collection type has collections) not wired up yet

##Repo ID: 22050

##Contributer ID: 79509

##Pull Request ID: 191862

###Profanity Found
**Text**
<!-- describe the changes you have made here: what, why, ... -->
fixes #2843 and #2851.
this was a tricky bug: javafx creates empty dummy cells at the end of a list view. for some reason the list view for the linked files had an initial size of `1.7976931348623157e308` and, well, creating that many dummy cells takes a while (probably longer than the universe took to create humans) and eventually lead to a freeze of the javafx thread.
the fix was easy, just add `maxheight="100"` and be happy (finally, after trying to debug the problem for ages).

- [ ] change in changelog.md described
- [ ] tests created for changes
- [ ] screenshots added (for bigger ui changes)
- [x] manually tested changed features in running jabref
- [ ] check documentation status (issue created for outdated help page at [help.jabref.org](https://github.com/jabref/help.jabref.org/issues)?)
- [ ] if you changed the localization: did you run `gradle localizationupdate`?


##Repo ID: 25219

##Contributer ID: 80088

##Pull Request ID: 196738

###Profanity Found
**Text**
<!--- provide a general summary of your changes in the title above -->
allows for recording multiple languages of materials (both controlled value language and script pairs, as well as language of material notes) within a resource (required), archival object, digital object, and digital object component.

## description
<!--- describe your changes in detail -->
changes include a database migration, import/export updates, staff-side form updates, staff and public pdf updates, and public display updates.  changes are detailed in the specification for this work linked to https://archivesspace.atlassian.net/browse/anw-382

## related jira ticket or github issue
<!--- please link to the jira ticket or github issue here: -->
https://archivesspace.atlassian.net/browse/anw-697

## motivation and context
<!--- why is this change required? what problem does it solve? -->
to allow for multiple languages of materials to exist in archival description, and to better conform to standards (e.g. ead 3) that support granular specification of languages and scripts, and parallel description.

## how has this been tested?
<!--- please describe in detail how you tested your changes. -->
<!--- include details of your testing environment, and the tests you ran to -->
<!--- see how your change affects other areas of the code, etc. -->
new tests added, existing tests updated.  has also been available as a test branch and undergone an initial series of internal informal user testing.

## screenshots (if appropriate):
new languages subrecord:
<img width="1039" alt="after_anw697" src="https://user-images.githubusercontent.com/15144646/64268009-5cc96780-cf05-11e9-821a-79b7891581d2.png">


## types of changes
<!--- what types of changes does your code introduce? put an `x` in all the boxes that apply: -->
- [ ] bug fix (non-breaking change which fixes an issue)
- [x] new feature (non-breaking change which adds functionality)
- [x] breaking change (fix or feature that would cause existing functionality to change)

## checklist:
<!--- go over all the following points, and put an `x` in all the boxes that apply. -->
<!--- if you're unsure about any of these, don't hesitate to ask. we're here to help! -->
- [x] my code follows the code style of this project.
- [x] my change requires a change to the documentation.
- [ ] i have updated the documentation accordingly.
- [x] i have read the **contributing** document.
- [x] i have added tests to cover my changes.
- [x] all new and existing tests passed.


##Repo ID: 25209

##Contributer ID: 79414

##Pull Request ID: 181395

###Profanity Found
**Text**
here is my attempt to move multi-parameters to activemodel.
it was [discussed in basecamp](https://basecamp.com/1755757/projects/6741427/messages/35654189) with @dhh and we really [need it in activeform](https://github.com/rails/actionform/pull/33#issuecomment-68600577). i also believe there are developers who'd like to use `time_select` helpers in their activemodel forms.

the first attempt by @georgebrock is in https://github.com/rails/rails/pull/8189 but it can't be applied anymore because typecasting in ar was completely refactored.

i had to implement dirty prototype of typecasting in activemodel too, because using multi parameters with date and time requires some kind of typecast.

the initial api is:

``` ruby
class person
  include activemodel::model
  include activemodel::attributeassignment

  attr_accessor :name, birthdate

  typecast_attribute :birthdate, date
  # another possible api is attr_typecasted :birthdate, date
end
```

cc @carlosantoniodasilva @kaspth 


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 265053

###Profanity Found
**Text**
these methods had defined in 2004 by dhh in initial commit and `actiondispatch::request`
class has been inherited from `rack::request` class in 2009 by josh.
in 2014 these methods and more of them defined in `rack::request` class
so we don't need them anymore in rails codebase.

[here](https://github.com/rails/rails/pull/20316#issuecomment-106074576) is the comment about this idea.

/cc @rafaelfranca 


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 265725

###Profanity Found
**Text**
- fixes coloring for sql statements generated with ruby heredoc, which often have spaces preceding the initial sql verb, like:

```
   sql = <<-eos
      select * from things
        where id in (
          select id from things
        )
   eos
```

^ would be colored as magenta in the existing code.
- improves coloring for statements like:

```
    # become white
    select * from (
        select * from mytable for update
    ) ss where col1 = 5;
    lock table table_name in access exclusive mode;

    # becomes red
    rollback
```
- reinstates the coloration of the `payload[:name]` via new method:
  `colorize_payload_name`
  instead of simple alternating colors, adds meaning:
  - `magenta` for `"sql"` or `blank?` payload names
  - `cyan` for model load/exists
- make some `activerecord::logsubscriber` instance methods private for clarity:
  - `colorize_payload_name`
  - `sql_color`
  - `logger`
- introduces specs for sql coloration.
- introduces specs for payload name coloration.

gh #20885


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 266145

###Profanity Found
**Text**
the original documentation didn't explain why a person would use the seeds.rb file instead of a migration when adding data.  this commit elaborates on the purpose of migrations compared to the seeds.rb file and explains how to work with initial data in more detail.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 266302

###Profanity Found
**Text**
the semantic versioning specification uses major.minor.patch – it would
make more sense to set the version to 0.1.0 for initial development
since a patch release cannot be created before a minor feature release.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 266365

###Profanity Found
**Text**
ssl redirect:
- move `:host` and `:port` options within `redirect: { … }`. deprecate.
- introduce `:status` and `:body` to customize the redirect response.
  the 301 permanent default makes it difficult to test the redirect and
  back out of it since browsers remember the 301. test with a 302 or 307
  instead, then switch to 301 once you're confident that all is well.

http strict transport security (hsts):
- ~~security. include the header on http:// responses also. we immediately
  redirect http:// requests to https://, but the header needs to be set
  on the initial response, not just the https:// destination.~~
- shorter max-age. shorten the default max-age from 1 year to ~~18 weeks~~180 days,
  the minimum to qualify for inclusion in browser preload lists.
- disabling hsts. setting `hsts: false` now sets `hsts: { expires: 0 }`
  instead of omitting the header. omitting does nothing to disable hsts
  since browsers hang on to your previous settings until they expire.
  sending `hsts: { expires: 0 }` flushes out old browser settings and
  actually disables hsts:
    http://tools.ietf.org/html/rfc6797#section-6.1.1
- hsts preload. introduce `preload: true` to set the `preload` flag,
  indicating that your site may be included in browser preload lists,
  including chrome, firefox, safari, ie11, and edge. submit your site:
    https://hstspreload.appspot.com


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 266548

###Profanity Found
**Text**
per #21602 @rafaelfranca  suggest.

have to always leave as text in gemfile than initial generation is writing below will cause `(erb):53:in`template': uninitialized constant rails::generators::appgenerator::bundler (nameerror)`

```
<% if bundler::windows -%>
# windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data'
<% end -%>
```


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 266609

###Profanity Found
**Text**
to add initial data after a database is created, the correct command is `rake db:seed`


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 267628

###Profanity Found
**Text**
provides an initial framework for an action cable guide drawing heavily from the readme and code comments, but i restructured them in some areas.

opening pr per @maclover7 in #22673


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 267675

###Profanity Found
**Text**
i want to fix the effect of the initial value parameter of `enumerable#sum` along to `array#sum` introduced in ruby 2.4.

in ruby 2.4, `[1, 2, 3].sum(0.0)` is `6.0` because the initial value `0.0` is a float:

```
$ ruby -ve 'p [1, 2, 3].sum(0.0)'
ruby 2.4.0dev (2016-04-28 trunk 54810) [x86_64-darwin15]
6.0
```

but with activesupport, the result turns to `6`:

```
$ ruby -v -i lib -r active_support/core_ext/enumerable -e 'p [1, 2, 3].sum(0.0)'
ruby 2.4.0dev (2016-04-28 trunk 54810) [x86_64-darwin15]
6
```

this pull-request fixes this issue.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 268782

###Profanity Found
**Text**
### summary

this came from [here](https://github.com/rails/rails/issues/24736). most applications comprise of single-purpose processes which do-one-thing-well. this has been the main selling point of foreman/procfile. i think that most rails apps suffer from a ram boot-time penalty, which is multiplied by the number of processes started from the procfile, and in cloud deployments like heroku, ram is a big cost factor. 

my proposal is: make rails main process act as the parent to all process types. rails is clearly the designated web-process, and most application servers either make it act as standalone process (puma, thin, webrick) or as a master process which forks workers (unicorn, puma cluster, passenger). i'd say, use it also to "fork" the parent background job process (resque, sidekiq, delayed job), the scheduler process (resque-scheduler, rufus, clockwork), basically everything ruby. 

to test my already functioning proof of concept, fork this branch, create a new dev app, add the following: 

``` ruby
# config/application.rb

# don't forget to add "resque" to the gemfile
# this will be the gem maintainers task to provide proper runners in the future
module resque
  # the worker doesn't receive any options, all is coming from env vars
  class runner < rails::forker::runner
    def run!
      worker = resque::worker.new('*')
      worker.log "starting worker #{self}"
      worker.work(5) # interval, will block
    end
  end
end

...
module forkerapp
  class application < rails::application
    ...
    forkers(resque)

end
```

i've tested this in an initial app with `rails server` command building with puma, with `puma`executable, both in standalone as in cluster mode (works only with `--preload`, as the fork hooks are set in config.ru), and these were the results with smem after boot:

```
# cluster mode
  pid user     command                         swap      uss      pss      rss
19401 vagrant  resque-1.26.0: waiting for         0     5.4m    36.2m    68.8m
19340 vagrant  puma 3.4.0 (tcp://0.0.0.0:3        0     8.2m    40.0m    75.2m    
```
### other information

obviously you can see by the diff that there were no unit tests written (yet), i've concentrated on the minimal stuff to make a poc work-and-running, and discuss the viability of such a feature for rails. hopefully afterwards one could discuss some open issues for me:
- railtie api
- abstract runner, and gems-should-implement-runner vs. active-job-like-adapters
- things rails must do by default before and after fork (open threads, reopen file-descriptors)
- "labelize/colorize" logs a-la foreman (maybe foreman-rails extension?)
- how to best configure the options/number of processes
- windows/non-fork environment support

@jeremy for the interest expressed in the issue, @schneems for the interest expressed in lowering the mem footprint of the stack. 


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 268824

###Profanity Found
**Text**
`ssl_set_verify(3)` explains:

```
ssl_verify_fail_if_no_peer_cert
  server mode: if the client did not return a certificate, the tls/ssl
handshake is immediately terminated with a "handshake failure" alert.
this flag must
  be used together with ssl_verify_peer.

  client mode: ignored

ssl_verify_client_once
  server mode: only request a client certificate on the initial tls/ssl
handshake. do not ask for a client certificate again in case of a
renegotiation.
  this flag must be used together with ssl_verify_peer.

  client mode: ignored
```

the smtp connection here uses a openssl socket in client mode,
suggesting invalid/ignored flags is rather misleading.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 269133

###Profanity Found
**Text**
those are assertions that i really do miss from the standard
`activesupport::testcase`. think of those as a more general version of
`assert_difference` and `assert_no_difference` (those can be implemented
by assert_changes, should this change be accepted).

why do we need those? they are useful when you want to check a
side-effect of an operation. `assert_difference` do cover a really
common case, but `assert_changes` gives us more control. having a
global error flag? you can test it easily with `assert_changes`. in
fact, you can be really specific about the initial state and the
terminal one.

``` ruby
error = error.new(:bad)
assert_changes -> { error.current }, from: nil, to: error do
  expected_bad_operation
end
```

`assert_changes` follows `assert_difference` and a string can be given
for evaluation as well.

``` ruby
error = error.new(:bad)
assert_changes 'error.current', from: nil, to: error do
  expected_bad_operation
end
```

check out the test cases if you wanna see more examples.

:beers:


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 269189

###Profanity Found
**Text**
### summary

this adds an initial definition to sti in the documentation. while reading through the file, it took me a minute to figure out what sti stood for. this will help clarify it.

this also adds a statement on the default value for the `:store_full_sti_class` class attribute.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 269241

###Profanity Found
**Text**
adds the initial infrastructure needed to run our internal commands with thor. it unifies the regular app commands and engine commands into one.

i've left the old command files in place in rails/commands and rails/engine/commands to slim the diff and ease review. i'll remove them before the final merge.

in another pr we can add command dependencies and port our rake commands over.

later, we can figure out how to let users add their own commands. it's mostly there; there's lookup code, the app commands just needs to be on the lookup path.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 269846

###Profanity Found
**Text**
### summary

we have a need to use the newer versions of the `listen` gem and the version pinning in `rails` & specifically `railties` is preventing this. when the initial [evented monitor](https://github.com/rails/rails/commit/de6ad5665d2679944a9ee9407826ba88395a1003) feature was written, the latest version of `listen` was the 3.0.x series. since then the `listen` project has moved on to the 3.1.x series. this patch corrects that version pinning by expanding its range to include the 3.1.x branch.
### other information

the `bundle exec rake test` command was run for `railties` & `activesupport` to make sure that there was no regression. `changelog`, `gemfile.lock` and documentation were also updated.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270028

###Profanity Found
**Text**
**update: this pr changed a lot over the course of being open. please refer to the documentation or code in master / 5-1-stable to use system tests**

i'm really excited to open this initial pr for bringing system/acceptance test support to rails through capybara.

the goal of this pr is for rails to take on all the setup that is needed in applications to allow capybara and make system testing default in rails applications.

~~**why is the name rails::systemtestcase?**~~
~~i chose this name because this was the name dhh indicated he preferred in the rails' basecamp long ago. i'm totally open to changing the name but ultimately decided to put it in actionpack with the rails namespace so i could get onto writing code and stop worrying about the name :wink:~~

**the test framework has been moved it it's own gem under the rails name and is now actionsystemtest**
because the gem expects a module and our test frameworks expect a class for inheritance i've made the gem and module name `actionsystemtest` and the class for inheriting test code from `actionsystemtestcase`. open to other names as well but the module and class names can't be the same else ruby gets confused.

**how do i add system tests to my application?**
by default new applications include a base system test much like integration tests. gemfiles generated for new applications will include capybara and the selenium driver.

capybara's selenium driver requires some setup by the programmer, so i've added a layer between capybara and rails so that rails' takes on that work called `railsseleniumdriver`. the default settings are as follows:
- the server is puma (because this is rails' default)
- the browser is chrome (because ff is broken w/ capybara and selenium right now),
- the default port is 28100, and
- the default screen size is [1400, 1400].

the reason i have chosen chrome as the default browser is because firefox doesn't work out of the box. selenium and the current version of firefox don't play nicely together so i've set up the driver to default to chrome, but it can easily be switched to using firefox. i'd also like to provide support for safari.

instead of requiring the programmer to set up the port, browser, server, etc rails handles that setup and frees up the programmer to work on writing their tests.

the rails drivers allow the default configuration to be changed by initializing a new driver:

``` ruby
# config/environments/test.rb
config.system_testing.driver = systemtesting::driveradapters::railsseleniumdriver.new(
  browser: :firefox
)
```

**what if i don't want to use selenium?**
if the programmer wants to use one of capybara's default drivers rather than the provided defaults in rails selenium configuration they can easily change that in the test environment. i've provided a shim in rails so setting the capybara driver is simple. i've named the class `capybaradriver` and it gives access to the 4 capybara drivers: `poltergeist`, `webrick`, `selenium` (with no setup), and `rack_test`:

``` ruby
# config/environments/test.rb
config.system_testing.driver = :poltergeist
```

each of the capybara default drivers that requires a server defaults to puma. any of the settings can be changed by initializing a new `capbyaradriver` object:

``` ruby
# config/environments/test.rb
config.system_testing.driver = systemtesting::driveradapters::capybaradriver.new(
  name: :poltergeist,
  server: :webrick
)
```

**what if i'm making a new application and don't want system testing at all?**
it's easy to skip system testing files in the app generator or the scaffold generator by running with the `--skip-system-test` flag.

**what if i already use capybara and don't want to use rails?**
because rails provides a specific test case name to inherit from you can easily just completely skip the rails version of system testing and use capybara directly.

**i want to try it out!**
i made a test app where you can try out system tests in rails w/ selenium! https://github.com/eileencodes/system_testing_app

---

**cool! what's next?**

below is a list of what is done and what's left to do. once we sort out naming and other issues i'll finish up the items below. 

**what's done?**
- [x] generators: scaffold, individual, and application
- [x] basic documentation
- [x] testing adapter settings (this just tests that rails provides options included, not that capybara and friends work. the assumption is that actual behavior of capybara and friends is tested by themselves, rails tests it's framework for initializing capybara)
- [x] configurable driver adapters w/ `railsseleniumdriver` being the default.
- [x] railtie for configuring system test settings
- [x] support for screenshots
- [x] changelog
- [x] fix the railties tests 😁 
- [x] move to it's own gem under the rails name. 
- [x] rails guides
- [x] other custom but generic helpers we support at basecamp that we'd like to port over, especially activejob and actioncable support
- [x] testing the custom helpers and assertions
- [x]  because capybara and the test suite use 2 different threads, transactions aren't correctly rolled back at the end of the test, leaving data behind. for years databasecleaner has been used to resolve this problem, but it's fixable in rails. see pr #28083 

**future work**
- support for safari (last i checked this wasn't quite ready for prime time)

cc/ @dhh @georgeclaghorn


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270034

###Profanity Found
**Text**
### summary

we have a need to use the newer versions of the `listen` gem and the version pinning in `rails` & specifically `railties` is preventing this. when the initial [evented monitor](https://github.com/rails/rails/commit/de6ad5665d2679944a9ee9407826ba88395a1003) feature was written, the latest version of `listen` was the 3.0.x series. since then the `listen` project has moved on to the 3.1.x series. this patch corrects that version pinning by expanding its range to include the 3.1.x branch.
### other information

the `bundle exec rake test` command was run for `railties` & `activesupport` to make sure that there was no regression. `changelog`, `gemfile.lock` and documentation were also updated.

this is the 5.0 branch version of #26695.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270038

###Profanity Found
**Text**
### summary

this fixes an issue where the default parsers are copied when set on `actiondispatch::request`. from b93c226d19 it seems the initial intent is for the parameter parsers to be a singleton for the middleware stack. later in a087cf4312 things were updated so that existing apps would not break if a parser was added which did not use symbol keys. that update _copied_ the parsers when setting them, even if only the default parser constant was used.

this copying breaks apps which expect the default parsers constant to be mutable in initializers (e.g. `config/initializers/mime_types.rb`), then later used by requests when no other set of parsers has been explicitly set.

in an attempt to reconcile both of these intents this lazy loads the parameter parsers. in the case where the parameters are not set (which is the default as of 53d2b7335a) the default constant will be used - which will reflect modifications by initializers. otherwise, a copy of the custom set it used with symbol keys.

this chooses to implement the lazy loading via a custom reader inside the `classmethods` module to be consistent with the existing code. other implementations that were considered include:

  - eager load `@parameter_parsers` directly in the `included` block

    ```ruby
    included do
      class << self
        attr_reader :parameter_parsers
      end

      @parameter_parsers = default_parsers
    end
    ```

    while this works as expected it doesn't follow existing conventions. to remain consistent with the existing code we won't us this.

  - in the setter check if all keys are symbols and not copying the hash in this case

    this behavior is surprising as sometimes the hash is used directly and other times a copy is used. since this may be surprising we won't use it.

  - drop transposing keys in the setter

    this doesn't appear to be a viable option given the current release cycle, so we won't do this either.

### background

this modification of the `default_parsers` was implemented in a rails 4.2 application based on information from rails-api/active_model_serializers#1027. after updating to rails 5.0.1 this stopped working.

for this app, the custom parser is setup in `config/initializers/mime_types.rb`. the custom parser is used to by-pass realtime parsing for large json data set for a particular endpoint. when the controller receives this particular format it pushes the data into a background job for further processing.

### other information

i wasn't clear on the module's intended behavior based on the above mentioned commits and seeing that the implementation of `params_parsers` delegates directly to `actiondispatch::request.parameter_parsers`. i guessed on the intended behavior based on the prior behavior and the statement _"there is only one set of parameter parsers in an app"_.

also, i was a little concerned that the lazy loading may have threading implications, but i don't have enough knowledge of the rails loading process to make a call on that.

 i'm happy to adjust things as necessary.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270661

###Profanity Found
**Text**
### summary

in postgres, adding foreign keys can cause significant downtime because the transaction needs to acquire some very heavy locks on the table being altered as well as the table being referenced. to illustrate, if i wanted to add a foreign key on my `addresses` table referencing my `users` table:
```
myapp=# begin;
begin
myapp=# alter table addresses add constraint "fk_rails_48c9e0c5a2" foreign key ("user_id") references "users" ("id");
alter table
myapp=# select locktype, relation::regclass, mode, transactionid as tid, virtualtransaction as vtid, pid, granted from pg_locks;
   locktype    |          relation          |        mode         |   tid   |  vtid   |  pid  | granted
---------------+----------------------------+---------------------+---------+---------+-------+---------
 relation      | pg_locks                   | accesssharelock     |         | 2/80438 | 56984 | t
 relation      | users_pkey                 | accesssharelock     |         | 2/80438 | 56984 | t
 relation      | index_addresses_on_user_id | accesssharelock     |         | 2/80438 | 56984 | t
 relation      | addresses_pkey             | accesssharelock     |         | 2/80438 | 56984 | t
 virtualxid    |                            | exclusivelock       |         | 2/80438 | 56984 | t
 relation      | addresses                  | accesssharelock     |         | 2/80438 | 56984 | t
 relation      | addresses                  | accessexclusivelock |         | 2/80438 | 56984 | t
 transactionid |                            | exclusivelock       | 3919702 | 2/80438 | 56984 | t
 relation      | users                      | accesssharelock     |         | 2/80438 | 56984 | t
 relation      | users                      | rowsharelock        |         | 2/80438 | 56984 | t
 relation      | users                      | accessexclusivelock |         | 2/80438 | 56984 | t
(11 rows)
```

...my transaction acquires an `accessexclusivelock` on `users` which is extremely detrimental on a high-traffic table, esp. when postgres performs a potentially lengthy query to validate the check.

on the other hand, i can take a two-step approach which significantly reduces this burden; by introducing an invalid constraint in one transaction and validating it in another, the locks acquired are much less restrictive:
```
myapp=# begin;
begin
myapp=# alter table addresses add constraint "fk_rails_48c9e0c5a2" foreign key ("user_id") references "users" ("id") not valid;
alter table
myapp=# commit;
commit
myapp=# begin;
begin
myapp=# alter table addresses validate constraint "fk_rails_48c9e0c5a2";
alter table
myapp=# select locktype, relation::regclass, mode, transactionid as tid, virtualtransaction as vtid, pid, granted from pg_locks;
   locktype    |          relation          |           mode           |   tid   |  vtid   |  pid  | granted
---------------+----------------------------+--------------------------+---------+---------+-------+---------
 relation      | users_pkey                 | accesssharelock          |         | 2/80443 | 56984 | t
 relation      | index_addresses_on_user_id | accesssharelock          |         | 2/80443 | 56984 | t
 relation      | addresses_pkey             | accesssharelock          |         | 2/80443 | 56984 | t
 relation      | addresses                  | accesssharelock          |         | 2/80443 | 56984 | t
 relation      | users                      | accesssharelock          |         | 2/80443 | 56984 | t
 relation      | users                      | rowsharelock             |         | 2/80443 | 56984 | t
 relation      | pg_locks                   | accesssharelock          |         | 2/80443 | 56984 | t
 virtualxid    |                            | exclusivelock            |         | 2/80443 | 56984 | t
 relation      | addresses                  | shareupdateexclusivelock |         | 2/80443 | 56984 | t
 transactionid |                            | exclusivelock            | 3919706 | 2/80443 | 56984 | t
(10 rows)
```

the first transaction acquires the same `accessexclusivelock` on the `users` table, but "the potentially-lengthy initial check to verify that all rows in the table satisfy the constraint is skipped" (source: [postgres docs](https://www.postgresql.org/docs/9.3/static/sql-altertable.html)). subsequently, the validation step does not block reads or writes on the `users` table. 💯 

so, this pr introduces two things:

- the ability to create invalid foreign keys by specifying the option `valid: false`
- a `validate_foreign_key` method (which takes the same variety of params as the other foreign key methods) to validate a foreign key

i've heard rumors about this being on the roadmap for the postgres team, i.e. skipping the check if the table being altered is empty and marking the constraint valid. in any case, perhaps someday this will be more easily achieved with built-in postgres, but for now it's an issue.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270742

###Profanity Found
**Text**
right now it behaves differently on jruby:

```
--- expected
+++ actual
@@ -1 +1 @@
-#<bigdecimal:5f3c866c,'0.333333333333333333',18(20)>
+#<bigdecimal:16e0afab,'0.3333333333333333',16(20)>
```

my initial pr (https://github.com/rails/rails/pull/27324) offered to let the precision to be decided by the platform and change the test expectation, but other contributors suggested that we should change the default precision in rails to be consistent of all platforms instead.

i got the value of `18` from the max default precision that comes from casting `rational(1/3)` to `bigdecimal`.

@sgrif @matthewd @guilleiguaran 

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 270752

###Profanity Found
**Text**
### summary
i was working on testing our gems and application on 5.1.0.beta1 and one of our internal gems stopped working following this change by @dylanahsmith : https://github.com/rails/rails/pull/26434

i think that it's a good change but we were relying on the nil-ness of `@connection` to know if we had an open connection or not.

this pr adds a flag to quickly know if the connection to mysql is opened or not. it does not mean that it's necessarily active though.

we can't use `active?` because in our use case, that would mean making a ping before every request.

looking at the initial pr we would ideally need to have access to `wrapper->connected` in the `mysql` gem but that's c code.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 271055

###Profanity Found
**Text**
### summary

this refactoring pr extracts the code concerning transactional-test setup/teardown into a separate module from the code concerning test-fixture creation and management. this makes the code easier to read and build upon moving forward since it more cleanly isolates the transaction setup/teardown logic from the fixture-setup logic.

### other information

i consider this pr to be an extension of #19282, which made the initial point that the transactional tests feature "doesn't really have anything to do with fixtures." this pr fully realizes that notion by extracting the transactional-test code into its own module, further clarifying the separation of concerns.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 271067

###Profanity Found
**Text**
we in the ruby world, write lot's of tests. and this is awesome! 🙌

now writing lot's of tests means we do have to manage them somehow. see
my controller tests, taken right from an app i've been working on.

this is restful controller here, that is something a bit more specified:

```ruby
class parentscontrollertest < actiondispatch::integrationtest
  test 'post /v1/parents registers a new parent'
  test 'post /v1/parents allows empty email for the kid'
  test 'post /v1/parents validates timezone a new parent'
  test 'post /v1/parents respond with errors'
  test 'post /v1/parents does not allow duplicate email addresses'

  test 'put /v1/parents/:id updates a parent'
  test 'put /v1/parents/:id can set a card'
  test 'put /v1/parents/:id can update card expiry through :credit_card'
  test 'put /v1/parents/:id can update card expiry through :card'
  test 'put /v1/parents/:id card_token takes priority over {credit_,}card'
  test 'put /v1/parents/:id can set a new email'
  test 'put /v1/parents/:id can set a new password'
  test 'put /v1/parents/:id returns a new token'
  test 'put /v1/parents/:id errors out on empty password'
  test 'put /v1/parents/:id can set a new password and change email at the same time'
  test 'put /v1/parents/:id works only for the parent in the token'
  test 'put /v1/parents/:id can error out with invalid stripe token'

  test 'get /v1/parents returns the partners of a parent'
end
```

and this is a poro test, which can represent something a bit more
generalized:

```ruby
class authorizabletest < activesupport::testcase
  test '#confirm does not confirm a nil input'
  test '#confirm proper token and flags confirmed_at'
  test '#password? is falsy on for blank password_digest'
  test '#password? is truthy on for present password_digest'
  test '#initial_password sets the initial password with confirmation token'
  test '#initial_password with wrong confirmation token'
  test '#initial_password does nothing for already set password'
  test '#reset_password resets a password with correct code'
  test '#reset_password with wrong code'
  test '#reset_password with unconfirmed auth'
  test '#reset_password with blank code'
  test '#reset_password attack for blank password_reset_code'
  test '#new_password_reset_code generates a random 6 digit code'
  test '#new_password_reset_code works for nil passwords'
  test '#change_password can change the password if old_password matches'
  test '#change_password cannot change empty password'
  test '#change_password cannot change empty short passwords'
  test 'password cannot be set or kept to nil after creation'
end
```

when you unroll the tests, it doesn't get that hard to navigate
through , but still, it's a bit noisy. we may argue that this way
structuring tests is not the optimal one. i think, i'm quite the average
testing guy here and lot's of folks tend to converge to this
organizational style. again, or so i think. 😅

now, if we had a way to group those tests by something, even just
organizationally, it would be a bit easier for me to navigate, know
where to put another `#reset_password` test or fold the tests i don't
need to focus on right now in my editor.

here is the controller:

```ruby
class parentscontrollertest < actiondispatch::integrationtest
  describe 'post /v1/parents' do
    test 'registers a new parent'
    test 'allows empty email for the kid'
    test 'validates timezone a new parent'
    test 'respond with errors'
    test 'does not allow duplicate email addresses'
  end

  describe 'put /v1/parents/:id' do
    test 'updates a parent'
    test 'can set a card'
    test 'can update card expiry through :credit_card'
    test 'can update card expiry through :card'
    test 'card_token takes priority over {credit_,}card'
    test 'can set a new email'
    test 'can set a new password'
    test 'returns a new token'
    test 'errors out on empty password'
    test 'can set a new password and change email at the same time'
    test 'works only for the parent in the token'
    test 'can error out with invalid stripe token'
  end

  describe 'get /v1/parents' do
    test 'returns the partners of a parent'
  end
end
```

and here is the poro:

```ruby
class authorizabletest < activesupport::testcase
  describe '#confirm' do
    test 'does not confirm a nil input'
    test 'sets proper token and flags confirmed_at'
  end

  describe '#password?' do
    test 'falsy on for blank password_digest'
    test 'truthy on for present password_digest'
  end

  describe '#initial_password' do
    test 'sets the initial password with confirmation token'
    test 'wrong confirmation token'
    test 'does nothing for already set password'
  end

  describe '#reset_password' do
    test 'resets a password with correct code'
    test 'with wrong code'
    test 'with unconfirmed auth'
    test 'with blank code'
    test 'attack for blank password_reset_code'
  end

  describe '#new_password_reset_code' do
    test 'generates a random 6 digit code'
    test 'works for nil passwords'
  end

  describe '#change_password' do
    test 'can change the password if old_password matches'
    test 'cannot change empty password'
    test 'cannot change empty short passwords'
  end

  test 'password cannot be set or kept to nil after creation'
end
```

i know david doesn't prefer the bdd dsl, but i wanna make a case for
`.describe` here. it doesn't create hidden test-cases or special
environments. it cannot be nested by design, so we don't promote those
levels into levels into levels kind of tests. it's used purely for
organizational work.

@dhh would you be interested in such change?

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 271163

###Profanity Found
**Text**
### summary

while implementing a class that utilizes `activemodel::validations` i noticed that the documentation includes a number of examples that reference `uniqueness` validations which are not implemented in activemodel since there is no persistence layer.

### other information

where possible, i replaced the example with a comparable one that is supported by activemodel.

i also noticed that the examples for the `validator#kind` will raise an exception since they require an `attributes` argument, so instead of:

```ruby
presencevalidator.new.kind   # => :presence
acceptancevalidator.new.kind # => :acceptance
```

the examples should look like this:

```ruby
presencevalidator.new(attributes: [:username]).kind   # => :presence
acceptancevalidator.new(attributes: [:terms]).kind # => :acceptance
```

i did not update these examples as part of this initial change but would be happy to do so either as part of this pr or a separate one.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 271519

###Profanity Found
**Text**
### summary

the underlying purpose is to enable logging of (for example) the request id of the initial http request that triggers a background job when that job is performed - so you could in the logs then easily know which request (and which user, if you include the user as a tag) triggered whatever actions are logged when the job is carried out. 

if there is a better way to accomplish this, i'd be very interested! this pr will hopefully help kickstart the issue.

this pr enables custom tags to be passed into the job to be added to logs by activejob when the job is performed. currently activejob adds the job name and job id to the logger - this would enable additional tags.

by passing an additional argument to perform_later - taking the form {log_tags: ['custom_tag1', 'custom_tag2'...]} - those custom tags will be added to the logs generated within an activejob job.

this means you could, for example, pass in the request_id of the request that fired the job, and have the logs generated as the job is carried out tagged with the request that fired the job. (you would just need to have access to the request at the point the job is enqueued, using, for example, https://github.com/steveklabnik/request_store.)

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 271751

###Profanity Found
**Text**
[code triage](https://www.codetriage.com/) is an app i've maintained for the past 4-5 years with the intent of getting people involved in open source. it sends subscribers a random open issue for them to help "triage". for ruby projects such as "rails/rails" you can also subscribe to documentation. for example you can get a few random documented methods, or if you want to write docs, get undocumented methods.

the initial approach was inspired by seeing the work of the small core team spending countless hours asking "what rails version was this in" and "can you give us an example app". the idea is to outsource these small interactions to a huge team of volunteers and let the core team focus on their work.

the purpose of the badge is to give more people an easier way to start contributing to rails. here's what it currently looks like:

[![code triage badge](https://www.codetriage.com/rails/rails/badges/users.svg)](https://www.codetriage.com/rails/rails)

the number is how many people are currently subscribed (a.k.a. "helpers") to the project on codetriage, the color is based off of the number of open issues in the project. you can see an example of this badge on another popular open source repo [crystal](github.com/crystal-lang/crystal/).

> for context to non-rails core: i also maintain sprockets (though a release hasn't happened in some time, sorry), and i have commit to rails. i'm not some rando trying to push arbitrary links to readmes on github.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272084

###Profanity Found
**Text**
### summary

i introduced this regression in #29662. the previous version would prefer the current `script_name` if one is available in the request for resolving the mount context in engine route helpers. but that would make them incorrect in some cases.

for example (just describing the test i added), if an engine is mounted at

```ruby
resources :fruits do
  mount bukkits::engine => "/bukkits"
end
```

and the current request path is `/fruits/1/bukkits/posts`, calling `fruit_bukkits.posts_path(fruit_id: 2)` would incorrectly return `/fruits/1/bukkits/posts`. this is because the `script_name` present in the request (in this case `/fruits/1/bukkits`) was preferred (by using `reverse_merge!` instead of `merge!` [here](https://github.com/rails/rails/blob/127b475dc251a06942fe0cd2de2e0545cf5ed69f/actionpack/lib/action_dispatch/routing/routes_proxy.rb#l34)).

this patch takes care of fixing that. my initial attempt was changing `reverse_merge!` with `merge!` but although that fixed the specific issue i was having, it broke some other tests. the problem is that the previous script name might contain relevant information that is not known to the `lambda` that resolves the script name from the parameters and the mount point location. for example, any context provided to the specific request via the environment's `script_name` variable is not known to this method.

so instead of preferring the `script_namer` resolution, i merged that with the current script name. so if the previous script name was `/foo/fruits/1/bukkits`, and the resulting one from calling the lambda is `/fruits/2/bukkits`, the resulting script name used for the route helper will be `/foo/fruits/2/bukkits`.

### other information

sorry for the probably not very well explained pr description. i'm not very familliar with rails internals, so it's hard for me to reason about them.

also, excuse the irrelevant commits. i added them while investigating the problem, but then i found out about the imminent release, so i wanted to open this asap to avoid introducing the regression.

**edit**: i tried to improve a bit the description of the problem & the solution.



##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272128

###Profanity Found
**Text**
need to address a few issues:

- [ ] how should the initial migration be seeded? i'm thinking probably just generate it in db/migrations on new apps.
- [ ] move the `direct_upload: true` convenience option from the activestorage helper into actionview.
- [ ] address how rails' ci can run the cloud service integration tests.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272196

###Profanity Found
**Text**
need to address a few issues:

- [ ] how should the initial migration be seeded? i'm thinking probably just generate it in db/migrations on new apps.
- [ ] move the `direct_upload: true` convenience option from the activestorage helper into actionview.
- [ ] address how rails' ci can run the cloud service integration tests.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272215

###Profanity Found
**Text**
need to address a few issues:

- [ ] how should the initial migration be seeded? i'm thinking probably just generate it in db/migrations on new apps.
- [x] move the `direct_upload: true` convenience option from the activestorage helper into actionview.
- [x] address how rails' ci can run the cloud service integration tests.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272216

###Profanity Found
**Text**
### summary

previously, `activesupport::cache::memcachestore#increment` and
`activesupport::cache::memcachestore#decrement` call `dalli::client#incr`
and `dalli::client#decr` as follows.

```ruby
@data.incr(normalize_key(name, options), amount)
@data.decr(normalize_key(name, options), amount)
```

however, considering the method arguments of `dalli::client`,
`options[:expires_in]` and default value for a not stored value
are not passed correctly.

* `dalli::client#incr(key, amt = 1, ttl = nil, default = nil)`
* `dalli::client#decr(key, amt = 1, ttl = nil, default = nil)`

c.f. https://github.com/petergoldstein/dalli/blob/f41bb9cf078246bd58a249cf09b1f56044e4662c/lib/dalli/client.rb#l169-l202

as a result, initial values for not stored values are not correctly set
despite the documentation saying `calling it on a value not stored
with :raw will initialize that value to zero.`

c.f.
https://github.com/aeroastro/rails/blob/9befc197f926272abbba5a1ca1323ce4f15ebd10/activesupport/lib/active_support/cache/mem_cache_store.rb#l117-l120

fortunately, since `ttl` is only applicable when the value is already set,
we have not encountered any bugs regarding `expires_in`.

by this patch, `activesupport::cache::memcachestore` will correctly handle
initialization of counters. also, test on increment/decrement behavior will be
fixed.

### other information

p.s. regarding this initialization, i have posted feature-request on the google group to initialize the not stored value to amount as if it is initialized to 0 **prior to the operation**.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 272731

###Profanity Found
**Text**
this pr introduces initial support for running rails on system in fips mode. these systems do not have access to commonly used hash functions and md5 in particular. attempts to calculate md5 hashes using openssl on a linux system will result in termination of the rails process.

this pr allows to switch from md5 hashes to sha512 hashes by setting ```config.active_support.use_fips_approved_hash_function``` setting to true. 

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 273119

###Profanity Found
**Text**
### summary

from project to project written with rails i spectate the similar snag, when **column definition rows in the schema are shuffled** from time to time (only for `schema.rb` in `:ruby` mode). it's annoying to see the changes in the git index, despite i haven't touched any of them. it's really hard for me to define the steps to reproduce for this bug, but let me put here my thoughts and proposed changes. first consider the next example for better clarity:
```
     t.string "county"
-    t.string "country_code"
     t.datetime "created_at", null: false
     t.datetime "updated_at", null: false
+    t.string "country_code"
     t.string "urn"
```
here "country_code" column definition changed position even though there was no any related migration code.

first of all i thought this behaviour is connected somehow with database engine version or operating system version divergence between developers in our team. so we setup the same version of rails 4.2 (later checked on 5.2) and mysql 5.7.20 on macos sierra 10.12.6 at macbook pro. but there was no luck – i still spectate schema shuffling.

then i decided to dig into the schema dumper code to understand how activerecord retrieves columns information and dumps it to the `schema.rb` file. inside i noticed expected [alphabetical table names sorting](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/schema_dumper.rb#l90):
```
def tables(stream)
  sorted_tables = @connection.tables.sort

   sorted_tables.each do |table_name|
    table(table_name, stream) unless ignored?(table_name)
  end
  ...
```
then i found [table columns info retrievement](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/schema_dumper.rb#l105):
```
def table(table, stream)
  columns = @connection.columns(table)
...
```
so there is no specific ordering. "hmmn" 🤔 , – was sparkled in my – "maybe it's desirable to show columns definition in the same manera as database holds them and don't sort in alphabetical order. but how different databases return schema info and do they comply the result order?". i moved to connection adapters:
• **mysql** ([`activerecord::connectionadapters::abstractmysqladapter`](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/connection_adapters/abstract_mysql_adapter.rb#l801))
```
def column_definitions(table_name) # :nodoc:
  execute_and_free("show full fields from #{quote_table_name(table_name)}", "schema") do |result|
    each_hash(result)
  end
end
```
i haven't found any proof in the [`show columns`](https://dev.mysql.com/doc/refman/5.7/en/show-columns.html) (synonym to `show fields`) mysql official documentation that ordering is present. but i found the next interesting discussions – ["show databases does not order infomation_schema correct"](https://bugs.mysql.com/bug.php?id=14473) and ["return order of mysql show columns
"](https://stackoverflow.com/questions/2544751/return-order-of-mysql-show-columns) – where people argue how mysql handles position of columns info. unfortunately, i'm not able to trace mysql server source code to find the pure evidence. let's assume **all this means `column_definitions`doesn't gauranty the order.** do we have alternatives? yes!
- [`describe`](https://dev.mysql.com/doc/refman/5.7/en/describe.html) (the clone of `show columns`, that leads me to the idea mysql follows the same "there is more than one way to do it" principle as ruby/perl 😄  ) 
- [`information_schema.columns`](https://dev.mysql.com/doc/refman/5.7/en/columns-table.html)

mysql has **ordinal position** of the columns and provides it in `information_schema.columns`. but there is one note, that makes me confused:
> `ordinal_position` is necessary because you might want to say `order by ordinal_position`. unlike `show`, `select` does not have automatic ordering.

seems like thoeretically `show` should keep the order according to what i see in the note, but practically i see the opposite. unlike postgres, [mysql allows to insert column before or after specific one](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html#alter-table-add-drop-column).
 i'd be very pleasant to hear any thoughts and get any references regarding  the columns positioning (logical, physical, virtual, etc.) here.

• **postgres** ([`activerecord::connectionadapters::postgresqladapter`](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/connection_adapters/postgresql_adapter.rb#l748))
```
def column_definitions(table_name)
  query(<<-end_sql, "schema")
              select a.attname, format_type(a.atttypid, a.atttypmod),
                     pg_get_expr(d.adbin, d.adrelid), a.attnotnull, a.atttypid, a.atttypmod,
                     c.collname, col_description(a.attrelid, a.attnum) as comment
                from pg_attribute a
                left join pg_attrdef d on a.attrelid = d.adrelid and a.attnum = d.adnum
                left join pg_type t on a.atttypid = t.oid
                left join pg_collation c on a.attcollation = c.oid and a.attcollation <> t.typcollation
               where a.attrelid = #{quote(quote_table_name(table_name))}::regclass
                 and a.attnum > 0 and not a.attisdropped
               order by a.attnum
  end_sql
end
```
schema info retrievement is pretty straightforward from `pg_attribute` system table. we have explicit `order by a.attnum` ([a.attnum](https://www.postgresql.org/docs/9.4/static/catalog-pg-attribute.html) – the number of the column), which should guarantee the order of attributes i guess. unlike mysql, postgres doesn't allow to insert column before or after specific one.

• **sqlite3** ([`activerecord::connectionadapters::sqlite3adapter`](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/connection_adapters/sqlite3_adapter.rb#l395))
```
def table_structure(table_name)
  structure = exec_query("pragma table_info(#{quote_table_name(table_name)})", "schema")
  ...
```
[`pragma table_info`](https://www.sqlite.org/pragma.html#pragma_table_info) lacks the required knowledge, that's why [activerecord uses](https://github.com/rails/rails/blob/master/activerecord/lib/active_record/connection_adapters/sqlite3_adapter.rb#l516) [`sqlite_master`](http://www.sqlite.org/faq.html#q7) readonly table to get and parse initial table creation sql. as far as we parse the sql statements all the time, it could be considered as columns order guarantee. here is an excerpt from the [`alter table`](http://sqlite.org/lang_altertable.html) official documentation regarding column position specification:
> the add column syntax is used to add a new column to an existing table. the new column is always appended to the end of the list of existing columns.

### alternatives

any sorting, especially if it's not supported in the database, could be performed at schema dumper level. for example, dumper sorts table names in the alphabetical order right now. the same approach could be applied to the columns. moreover we may enforce ordering at both levels – **database query** and **schema dumper table info processing**.

### considertations

how do different databases consider the columns order? afaik, there are 2 points:
- columns order from fixed length to variable length provides performance boost, because it's easier to find the offset of the fixed field. that's why primary key is better to place in the beginning of the table. 
- columns order doesn't much matter from user point of view, because columns order at the logical level could be different from how database spread columns at the physical level. that means you don't have to be bothered with column position tuning, database engine better knows how to store the data.

### proposed changes

- force mysql adapter to retrieve columns definition in the same order.

does all this make sense? please shout out if i have to cover provided changes with specs somewhere else. also i'm happy for any critics 🙇 

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 273593

###Profanity Found
**Text**
### summary

this is a fix for a bug @tenderlove and i have been stepping through together.

`uri.unescape` in rails 4.2 throws an `encoding::compatibilityerror` if the (utf-8 tagged) argument contains actual unicode characters. ~this doesn't happen on 3.x; compare the monkey-patches:~ turns out this was a patch made in our own application. looks like we should be able to just pull this across.

#### ~3.x~ patched

```ruby
      def unescape(str, escaped = /%[a-fa-f\d]{2}/)
        # todo: are we actually sure that ascii == utf-8?
        # yk: my initial experiments say yes, but let’s be sure please
        enc = str.encoding
        enc = encoding::utf_8 if enc == encoding::us_ascii
        str.dup.force_encoding(encoding::ascii_8bit).gsub(escaped) { [$&[1, 2].hex].pack(‘c’) }.force_encoding(enc)
      end
```

#### 4.2

```ruby
    def unescape(str, escaped = /%[a-fa-f\d]{2}/)
      # todo: are we actually sure that ascii == utf-8?
      # yk: my initial experiments say yes, but let’s be sure please
      enc = str.encoding
      enc = encoding::utf_8 if enc == encoding::us_ascii
      str.gsub(escaped) { [$&[1, 2].hex].pack(‘c’) }.force_encoding(enc)
    end
```

the issue is that `[$&[1, 2].hex].pack('c')` returns an ascii-8bit tagged string, which we then fail to gsub into `str`. this wasn't a problem in the ~3.x~ patched variant where the string was tagged as ascii-8bit anyway.

this pr opens by correcting the test; `parser.escape(str)` returns an us-ascii (!) tagged string, so `parser.unescape` succeeds for similar reasons as why the ~3.x~ patched variant succeeded. this corrects the test to resemble the actual use-case: passing utf-8 tagged strings into `uri.unescape`.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 273646

###Profanity Found
**Text**
for multi db applications you always had to create your own rake tasks which made setting up multi db a major pita. this pr is part 1 of a many that adds the initial underpinning for supporting multiple databases through the rake db commands. i'm doing this in small pr's so that reviewing is easier.

this app can be used to test out the features here. just clone and use the commands below to play with testing re rake tasks for create, migrate, drop, and dump. https://github.com/eileencodes/multiple_databases_demo

examples below are assuming a three-tier database.yml like this:

```yaml
development:
  primary:
    <<: *default
    database: multiple_databases_development
  animals:
    <<: *default
    database: multiple_databases_development_animals
    migrations_paths: "db/animals_migrate"

test:
  primary:
    <<: *default
    database: multiple_databases_test
  animals:
    <<: *default
    database: multiple_databases_test_animals
    migrations_paths: "db/animals_migrate"
```

* creates internal databaseconfig objects so it's easier to pass around the configs. we can then ask a databaseconfig for it's env or spec or config directly. this will come in handy for a larger refactoring i'm working on.
* ensures when running `bin/rails db:create`, `bin/rails db:migrate`, `bin/rails db:drop`, and `bin/rails db:schema|structure:dump` that tasks are run for all relevant envs and all databases in that env so given the above config `bin/rails db:create` will create the dev and test dbs for both primary and animals configs.
* adds new rails db tasks that can perform create/migrate/drop on a specific database in an environment
  * `bin/rails db:create:primary` or `bin/rails db:create:animals`
  * `bin/rails db:drop:primary` or `bin/rails db:drop:animals`
  * `bin/rails db:migrate:primary` or `bin/rails db:migrate:animals`

future parts of this work will:
* add more rake task support for multi db as this only does the first 4 major ones
* add documentation for multi-db three-tier database.yml applications
* add documentation for the rake tasks
* refactoring of the connection management to fix the assumption that the config lives directly under development (see https://github.com/rails/rails/pull/32271 for more info there on what i'm talking about).
* eventually porting these to rails commands
* dealing with rw/ro connection setups

cc/ @matthewd @tenderlove @dhh 

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 273699

###Profanity Found
**Text**
[imageprocessing](https://github.com/janko-m/image_processing) gem is a wrapper around minimagick and [ruby-vips](https://github.com/jcupitt/ruby-vips), and implements an interface for common image resizing and processing. this is the canonical image processing gem recommended in [shrine](https://github.com/shrinerb/shrine), and that's where it developed from. the initial implementation was extracted from refile, which also implements on-the-fly transformations.

some features that imageprocessing gem adds on top of minimagick:

  * resizing macros
    - [#resize_to_limit](https://github.com/janko-m/image_processing/blob/master/doc/minimagick.md#resize_to_limit)
    - [#resize_to_fit](https://github.com/janko-m/image_processing/blob/master/doc/minimagick.md#resize_to_fit)
    - [#resize_to_fill](https://github.com/janko-m/image_processing/blob/master/doc/minimagick.md#resize_to_fill)
    - [#resize_and_pad](https://github.com/janko-m/image_processing/blob/master/doc/minimagick.md#resize_and_pad)
  * [automatic orientation](https://www.imagemagick.org/script/command-line-options.php#auto-orient)
  * [automatic thumbnail sharpening](https://github.com/janko-m/image_processing/blob/master/doc/minimagick.md#sharpening)
  * avoids the complex and inefficient `minimagick::image` class
  * will use `magick` cli instead of `convert` on imagemagick 7 in the near future

however, maybe the biggest feature of the imageprocessing gem is that it has an alternative implementation that uses **[libvips](http://jcupitt.github.io/libvips/)**. libvips is an alternative to imagemagick that can process images [very rapidly](https://github.com/jcupitt/libvips/wiki/speed-and-memory-use) (we've seen **up to 10x faster processing** compared to imagemagick).

what's great is that the imageprocessing gem provides the same interface for both implementations. the macros are named the same, and the libvips implementation also does auto orientation and thumbnail sharpening; only the operations/options specific to imagemagick/libvips differ. the integration provided by this pr should work for both implementations.

the pr should maintain almost 100% backwards compatibility; there are two incompatibilities:

* users would now have to include the `image_processing` gem into their gemfiles instead of `mini_magick`
* `:combine_options` was removed because `imageprocessing::minimagick` builds a single `convert` command, so it's not needed anymore

i know that rails 5.2 is on feature freeze before the release, but i think if we agree we want imageprocessing to be used for active storage, it's better to get it in now, due to the two mentioned backwards incompatibilities.

in short, active storage relying on imageprocessing means it will have much better minimagick defaults, it will get **libvips** support *for free* (which is a big deal in terms of performance), it will get convenient resizing macros that work on both implementations, and it means the active storage project will have minimal maintenance in the image processing department.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 273826

###Profanity Found
**Text**
### summary

currently, initial rails console can't load `activejob::arguments`.

```sh
$ ./bin/rails console
> activejob::arguments.serialize(...)
nameerror: uninitialized constant activejob::arguments
```

it is inconvenient for me because i want to check the behavior from the console.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274361

###Profanity Found
**Text**
### summary

a bug [was introduced](https://github.com/rails/rails/pull/31117/commits/15cb4efadb61a8813967d3c25f4adfc9a918a0c0) in activemodel 5.2 that caused the `added?` method to fail if a string parameter for the attribute was used with a symbol for the message.

```ruby
model.added?("name", :blank)
```

issue #33357 includes a test case to demonstrate the behavior and my initial write up of it can be found on [the pr that created the bug](https://github.com/rails/rails/pull/31117#issuecomment-404972922).

this is a fairly simple fix. the details has [normalizes to symbol keys in the add method](https://github.com/rails/rails/blob/master/activemodel/lib/active_model/errors.rb#l309) so we're just forcing the string to a symbol when doing the check in the added method.

i questioned whether it was worth a test of it's own, but decided it was better to be explicit.

is this worth a changelog entry?

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274437

###Profanity Found
**Text**
### summary
fixes https://github.com/rails/rails/issues/33610

looks like the issue is happening at `populate_with_current_scope_attributes` where it shouldn't try to assign the `scope_attributes` on the initial evaluation, which results in a duplicate record.

e.g.) in the test example, when creating a `man` record, the current behaviour with `:create_with` attribute registered in a `relation` is that it will try to create an `interest` record before  the owner `man`, instead of creating `man` first, then build `interest` based on `man`.

making `scope_attributes?` truly returns boolean should fix it instead returning an empty relation that evaluates to true.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274613

###Profanity Found
**Text**
### summary
continuation of 
#28369 (merged but reverted)
#28834 (open but stale) 

#query_conditions_for_initial_load currently loads many more
records than it needs. including the children of composite types
when the parent composites themselves were not loaded.

in the current query a record is returned for each table in the db
but is not used, while this is normally pretty minimal overhead;
in databases with a large number of tables (eg. tenanted app with
multiple schemas) the issue is exacerbated and results in memory
bloat each time a connection is established.

this attempts to reduce the bloat by amending the query to not
include the children of composite types (including the records
for each table) as suggested [here in #28834](https://github.com/rails/rails/pull/28834#issuecomment-312422423)

### other information

created 2 dummy databases using the following [script](
https://gist.github.com/jonathan-wheeler/db266d98c4d61ecd942e3cd466baefdc)
one single tenant with 100 tables and one large multitenant with
1000 schemas each with 100 tables. they contain no data but it
should still illustrate the issue.

10.times { activerecord::base.establish_connection(....).connection }
[full benchmark scripts](https://gist.github.com/jonathan-wheeler/c4c8726773311f9785f22d4d1ca24eeb)
#### memory
##### single tenant
```
calculating -------------------------------------
master_single_tenant_test
                        20.982m memsize (    18.984m retained)
                        23.535k objects (     1.109k retained)
                        50.000  strings (    50.000  retained)

patch_single_tenant_test
                        11.938m memsize (    10.559m retained)
                        16.082k objects (   811.000  retained)
                        50.000  strings (    50.000  retained)

comparison:
patch_single_tenant_test:   11938187 allocated
master_single_tenant_test:   20982362 allocated - 1.76x more
```
##### multitenant
```
calculating -------------------------------------
master_large_multi_tenant_tenant_test
                       493.410m memsize (    18.983m retained)
                         5.069m objects (     1.099k retained)
                        50.000  strings (    50.000  retained)
patch_large_multi_tenant_tenant_test
                        12.843m memsize (    11.337m retained)
                        23.825k objects (     7.024k retained)
                        50.000  strings (    50.000  retained)

comparison:
patch_large_multi_tenant_tenant_test:   12843438 allocated
master_large_multi_tenant_tenant_test:  493410349 allocated - 38.42x more
```

not in the same league of improvement seen in #28834 as this patch is
less aggressive so still includes some clutter but still a
sizeable reduction in allocations to be made. not a huge difference
in retained memory but initial bloat maybe more of an issue as the
number of tables scale (example 10,000 schemas is not huge).

#### speed
##### single tenant
```
rehearsal -------------------------------------------------------------
master_single_tenant_test   0.043770   0.019775   0.063545 (  0.227460)
patch_single_tenant_test    0.039852   0.009767   0.049619 (  0.191569)
---------------------------------------------------- total: 0.113164sec

                                user     system      total        real
master_single_tenant_test   0.034316   0.006944   0.041260 (  0.195248)
patch_single_tenant_test    0.027595   0.006390   0.033985 (  0.179472)
```

##### multitenant
```
rehearsal -------------------------------------------------------------------------
master_large_multi_tenant_tenant_test   4.232676   0.268989   4.501665 ( 12.966424)
patch_large_multi_tenant_tenant_test    0.027335   0.006216   0.033551 ( 13.238648)
---------------------------------------------------------------- total: 4.535216sec

                                            user     system      total        real
master_large_multi_tenant_tenant_test   0.026196   0.005952   0.032148 ( 12.977751)
patch_large_multi_tenant_tenant_test    0.027290   0.006186   0.033476 ( 13.293085)
```

no substantial differences.



##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274632

###Profanity Found
**Text**
### summary

follow up: https://github.com/rails/rails/pull/33134 add missing documentation
details: https://support.cloudflare.com/hc/en-us/articles/115003206852s

two implemented but undocumented features are to help indicate that cache is fresh for 3 hours, and it may continue to be served stale for up to an additional 60 seconds *to parallel requests for the same resource* or up to 5 minutes while errors are being returned back while the initial synchronous revalidation is attempted.

caching re-invalidation may cause thundering herd effect under high load, with these [two new http standardized features](https://tools.ietf.org/html/rfc5861) we can leverage cdn or any proxy caching layer to reduce throughput while cache is being populated with a new response.



##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274724

###Profanity Found
**Text**
under current behavior the `attempts` argument for retry_on includes the initial run of a job. this is confusing and the documentation is not clear. to correct this, the documentation surrounding `retry_on` and `attempts` has been updated.

this addresses #33816

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 274754

###Profanity Found
**Text**
### summary

common sensitive parameter names to consider adding to generated filter parameters for new apps.

the initial commit in this pr is conservative, only adding `:secret` to the current default `[:password]`.

further candidates distilled from the `filter_parameters` config from a number of open source rails projects to consider adding:

```rb
# these will filter exact *and* partial matches,
# e.g. :token would filter: token, api_token, access_token, token_foo
:token,
:_key,
:auth,
:crypt,
:salt,
:certificate,
:otp,
:access,
:private,
:protected,
:birth,
:ssn
```

### other information

similar pull request from 2015 discussing adding to these defaults: https://github.com/rails/rails/pull/19809

the rails apps searched to find these: https://github.com/eliotsykes/real-world-rails/tree/master/apps

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275007

###Profanity Found
**Text**
### summary

indexes often become fragmented in high-write-load tables. one solution to this is to rotate indexes frequently using something like `create index concurrently new_index_name` followed by `delete index old_index_name`, but this becomes a routine maintenance headache.

building indexes with an initial fillfactor less than the default value (on postgresql, 90%), means that there is room in the index pages to store additional values. this is something to be cautious about, because higher fillfactor indexes pack better into memory, but it might be something useful to tweak on occasion.

### other information

this pullrequest does not currently include documentation changes, i wanted to gather feedback about whether this change would be more broadly useful before investing too heavily into it.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275160

###Profanity Found
**Text**
when `word_wrap` processes a block of text in which some lines are indented with white space, it strips white space from both sides of long lines. for example, a paragraph which begins with an initial indent will have that indent removed when wrapped. see example input in #34487.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275179

###Profanity Found
**Text**
### summary
i stumbled upon this error while trying to make a basic.  

```
2.3.4 :008 > activerecord::base.establish_connection(                                                                                          
2.3.4 :009 >       "adapter"  => "sqlite3",                                                                                                    
2.3.4 :010 >       "database" => "path/to/dbfile"                                                                                              
2.3.4 :011?>     )       
```
and it gave out a:
```
argumenterror: wrong number of arguments (given 1, expected 2)                                                                                                                                  
        from /users/sergio/.rvm/rubies/ruby-2.3.4/lib/ruby/site_ruby/2.3.0/rubygems/errors.rb:28:in `initialize'                                                                                
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `exception'                                  
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `raise'                                      
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `rescue in spec'                             
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:190:in `spec'                                       
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/abstract/connection_pool.rb:950:in `establish_connection'                       
        from /users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/active_record/connection_handling.rb:60:in `establish_connection'                                                 
        from (irb):21                                                                                                                                                                           
        from /users/sergio/.rvm/rubies/ruby-2.3.4/bin/irb:11:in `<main>'                                                                                  
```

it seems that i was missing a dependency (sqlite3 _sigh_) , and gem missingspecerror has some problems here in initialisation with this ruby syntax. 

i replicated the offending line:
```
(byebug) raise e.class, "hello", e.backtrace
*** argumenterror exception: wrong number of arguments (given 1, expected 2)

nil
```
just like my initial error.
and again with the ruby `.new` object syntax 
```
(byebug) raise e.class.new("hello", e.backtrace)
*** gem::missingspecerror exception: could not find 'hello' (["/users/sergio/.rvm/rubies/ruby-2.3.4/lib/ruby/site_ruby/2.3.0/rubygems/dependency.rb:308:in `to_specs'", "/users/sergio/.rvm/rubies/ruby-2.3.4/lib/ruby/site_ruby/2.3.0/rubygems/dependency.rb:320:in `to_spec'", "/users/sergio/.rvm/rubies/ruby-2.3.4/lib/ruby/site_ruby/2.3.0/rubygems/core_ext/kernel_gem.rb:65:in `gem'", "/users/sergio/.rvm/gems/ruby-2.3.4/gems/activerecord-5.2.1.1/lib/a

...
```
which looks correct. 

could this be a backward compatibility issue? 
yet, this was made in ruby 2.3 and according to rails
`rails 5 requires ruby 2.2.2 or newer.`
so it should be in the clear.

disc: this might have been a beginners mistake. 


##### edit
tried with ruby 2.4 and activerecord-5.2.1.1
same result 
```
2.4.1 :007 > require 'active_record'
 => true 
2.4.1 :008 > activerecord::base.establish_connection(
2.4.1 :009 >       "adapter"  => "sqlite3",
2.4.1 :010 >       "database" => "path/to/dbfile"
2.4.1 :011?>     )
argumenterror: wrong number of arguments (given 1, expected 2)
        from /users/sergio/.rvm/rubies/ruby-2.4.1/lib/ruby/site_ruby/2.4.0/rubygems/errors.rb:28:in `initialize'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `exception'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `raise'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:203:in `rescue in spec'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/connection_specification.rb:190:in `spec'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_adapters/abstract/connection_pool.rb:950:in `establish_connection'
        from /users/sergio/.rvm/gems/ruby-2.4.1/gems/activerecord-5.2.1.1/lib/active_record/connection_handling.rb:60:in `establish_connection'
        from (irb):8
        from /users/sergio/.rvm/rubies/ruby-2.4.1/bin/irb:11:in `<main>'
2.4.1 :012 > 
```





##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275219

###Profanity Found
**Text**
### summary

having these directories configured as yarn workspaces can cause you to generate an incorrect root yarn.lock when you run `yarn install` if you have stale files in these directories. this can be particularly troubling because the directories are ignored by git so it's not immediately obvious that you have files there which could be causing an invalid lockfile to be generated.

additionally, [@lsylvester said](https://github.com/rails/rails/pull/34588#issuecomment-443547937) that his initial motiviation for including these directories was resolved by relaxing the requirements in the package.json template used by the app generator.

see this thread for more information on the problems this caused: https://github.com/rails/rails/pull/34588#issuecomment-443511651

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275266

###Profanity Found
**Text**
### summary

when generating a new rails application (`rails new`) using a custom template that 
includes gems from an authenticated source, the user has to provide credentials to 
`bundler`.

one way to do this is by [exporting environment variables](https://bundler.io/v1.16/bundle_config.html#credentials-for-gem-sources), for example:

`export bundle_github__com=user:pass`: provides credentials for bundler to fetch
gems from `github.com`.

the problem this pr addresses is that we are currently scrubs all `/bundle_.*/`
environment variables by wrapping our system calls in [`bundler.with_clean_env`](https://github.com/rails/rails/blob/5b5319413a611c949cb796351ff42fa0c0299252/railties/lib/rails/generators/app_base.rb#l381-l388).

we do this because we don't want our commands executed against the generated project
to use the generator's `bundler` environment (e.g. our gems): the generated project should
use it's own configuration.

the problem with `bundler.with_clean_env` is that, on top of restoring environment
variables to their original state, it also scrubs any `/bundle_.*/` variables, which is harmful for authenticated gem sources.

this pr replaces `bundler.with_clean_env` with `bundler.with_original_env`, which only
restores environment variables to their initial state, without additional scrubbing.


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275345

###Profanity Found
**Text**
this is a followup to https://github.com/rails/rails/pull/33615

the removal of array indexes being done only for i18n situation makes for fairly inconsistent results as you can see in the two tests i modified.

@larochelle in your initial patch the `.remove(/\[\d\]/)` was also before the `if`, but then you moved it inside for https://github.com/rails/rails/pull/33615, is there something i'm missing?

@rafaelfranca @edouard-chin @larochelle 


##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275627

###Profanity Found
**Text**
this is purely a refactor with the following simplifications:
* use redefine_singleton_method
* use keyword arguments
* use the `default` value in the initial method definition to avoid an unnecessary method redefinition

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275814

###Profanity Found
**Text**
turbolinks replaces the csp nonce `<meta>` tag on page change, but inline scripts inserted by ujs need the nonce from the initial page load. in general, it doesn't matter to ujs if the nonce changes after the page loads: only the initial value is relevant.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275862

###Profanity Found
**Text**
since the initial value of `config.action_view.raise_on_missing_translations` has been added.
please check.
https://github.com/rails/rails/blob/master/actionview/lib/action_view/base.rb#l161

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275991

###Profanity Found
**Text**
### summary

this pr is currently only a wip, just wanted to gather some opinions before spending more time on it.

it's somewhat a standard nowdays that binstubs are "owned" by bundler and have the initial responsability of loading the appropriate version of a tool for your particular application. of course, users can then further customize the way the tool is launched to fit their needs.

however, the binstub provided by rails deviates from this and instead includes some steps for booting the framework inside this file, while providing the standard `bundler/setup`steps inside the `config/boot.rb` file.

i figured we could standarize this, let the `rails` binstub be a standard `bundler` binstub, and let the few lines currently inside the `rails` binstub live inside the framework.

i'd like to hear some opinions about this.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 275997

###Profanity Found
**Text**
since the initial value of `activesupport :: deprecation.silenced` has been added.
please check.
https://github.com/rails/rails/blob/master/activesupport/lib/active_support/deprecation.rb#l42

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 276006

###Profanity Found
**Text**
### summary

while investigating #29966 i found this related bug that a table created with a comment in a `create_table` call like this 

```ruby
create_table :foo, comment: 'a table comment'
```

will also add the same comment to the primary key column in the database.

### detailed analysis

i traced back the origin of this bug. in the initial pr that added the database comments support, the comment option on the create table was not being passed to the primary key options, as [can be seen here](https://github.com/rails/rails/pull/22911/files#diff-a0775e1ec64264dc76a8ee71a5211ae3r273).

but then, after these 2 subsequent refactors 485e7f25f29ca1ca23bb214b802cf68840dabbb6 and b04c6339640d87b680f1975f3686fed0d885b1bc, the comment option was not being excluded from primary key options anymore and thus the bug.



##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 276437

###Profanity Found
**Text**
load initial database.yml once, and warn if we can't create tasks

for multiple databases we attempt to generate the tasks by reading the
database.yml before the rails application is booted. this means that we
need to strip out erb since it could be reading rails configs.

in some cases like https://github.com/rails/rails/issues/36540 the erb
is too complex and we can't overwrite with the dummycompilier we used in
https://github.com/rails/rails/pull/35497. for the complex causes we
simply issue a warning that says we couldn't infer the database tasks
from the database.yml.

while working on this i decided to update the code to only load the
database.yml once initially so that we avoid having to issue the same
warning multiple times. note that this had no performance impact in my
testing and is merely for not having to save the error off somewhere.
also this feels cleaner.

note that this will not break running tasks that exist, it will just
mean that tasks for multi-db like `db:create:other_db` will not be
generated. if the database.yml is actually unreadable it will blow up
during normal rake task calls.

fixes #36540 

cc/ @tenderlove @jhawthorn @rafaelfranca @klyonrad 

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 276548

###Profanity Found
**Text**
follow up to #36592 

older versions of selenium had `driver_path` on `::selenium::webdriver::chrome` directly, not on `...::service`. this avoids errors on those old versions and will preload properly if webdrivers is installed.

i learned this because i broke tests on 6-0-stable when backporting the initial commit (oops! 😳). we'll probably want to also bump the selenium version on 6-0-stable to make the test added in #36592 pass.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 276571

###Profanity Found
**Text**
ref: https://github.com/shopify/statsd-instrument/pull/184#issuecomment-535425202

this simply a quick proof of concept to showcase a fairly nasty foot gun with some block based assertions. see [this comment chain for the initial discussion](https://github.com/shopify/statsd-instrument/pull/184#issuecomment-535425202), but i'll explain it all here.

### the problem

see the following test case:

```ruby
class countertest < activesupport::testcase
  class counter
    attr_reader :count

    def initialize
      @count = 0
    end

    def increment!
      @count += 1
      raise "omg"
    end
  end

  test "it works" do
    counter = counter.new

    assert_raises runtimeerror do
      assert_no_difference -> { counter.count } do
        counter.increment!
      end
    end
  end
end
```

it passes even though `counter.count` changed from `0` to `1`, this is because `assert_difference` like most other block based assertions (e.g. `assert_enqueued_*`) are totally bypassed when an error happen.

of course the test is arguably broken, the user here should put the `assert_raises` inside the `assert_no_difference`.

but realistically it's not hard to overlook this, so i think it would make sense to consider any raised exception, as an assertion failure.

@rafaelfranca @wvanbergen thoughts?

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277016

###Profanity Found
**Text**
this commit message is really long 😅 but it's got a lot of info in it. we felt it was important to explain what we were trying to solve and why we prefer this approach.

---

this pr is an alternate solution to #37388. while there are benefits
to merging #37388 it changes the public api and swaps around existing
concepts for how connection management works. the changes are
backwards-incompatible and pretty major. this will have a negative impact
on gems and applications relying on how conn management currently works.

**background:**

shopify and other applications need sharding but rails has
made it impossible to do this because a handler can only hold one
connection pool per class. sharded apps need to hold multiple
connections per handler per class.

this pr aims to solve only that problem.

**what this pr does:**

in this pr we've added a `rolemanager` class that can hold multiple
`roles`. each `role` holds the `db_config`,
`connection_specification_name`, `schema_cache` and `pool`. by default
the `rolemanager` holds a single reference from a `default` key to the
`role` instance. a sharded/multi-tenant app can pass an optional second
argument to `remove_connection`, `retrieve_connection_pool`,
`establish_connection` and `connected?` on the handler, thus allowing
for multiple connections belonging to the same class/handler without
breaking backwards compatibility.

by using the `rolemanager` we can avoid altering the public api, moving
around handler/role concepts, and achieve the internal needs for
establishing multiple connections per handler per class.

**a note about why we opened this pr:**

we very much appreciate the work that went into #37388 and in no way mean
to diminish that work. however, it breaks the following public apis:

* `#retrieve_connection`, `#connected?`, and `#remove_connection` are
public methods on handler and can't be changed from taking a spec to a
role.
* the knowledge that the handler keys are symbols relating to a role
(`:writing`/`:reading`) is public - changing how handlers are accessed
will break apps/libraries.

in addition it doesn't solve the problem of mapping a single connection
to a single class since it has a 1:1 mapping of `class (handler) -> role
(writing) -> db_config`. multiple pools in a writing role can't exist
in that implementation.

the new pr solves this by using the `rolemanager` to hold multiple connection
objects for the same class. this lets a handler hold a role manager
which can hold as many roles for that writer as the app needs.

**regarding the `role` name:**

when i originally designed the api for multiple databases, it wasn't
accidental that handler and role are the same concept. handler is the
internal concept (since that's what was there already) and role was the
public external concept. meaning, role and handler were meant to
be the same thing. the concept here means that when you switch a
handler/role, rails automatically can pick up the connection on the
other role by knowing the specification name. changing this would mean not
just that we need to rework how github and many many gems work, but also
means retraining users of rails 6.0 that all these concepts changed.

since this pr doesn't move around the concepts in connection
management and instead creates an intermediary between `handler` and
`role` to manage the connection data (`db_config`, `schema_cache`,
`pool`, and `connection_specification`) we think that `role` and
`rolemanager` are the wrong name.

we didn't change it yet in this pr because we wanted to keep change
churn low for initial review. we also haven't come up with a better
name yet. :smile:

**what this pr does not solve:**

our pr here solves a small portion of the problem - it allows models to
have multiple connections on a class. it doesn't aim to solve any other
problems than that. going forward we'll need to still solve the
following problems:

* `databaseconfig` doesn't support a sharding configuration
* `connects_to`/`connected_to` still needs a way to switch connections for shards
* automatic switching of shards
* `connection_specification_name` still exists

**the end**

thanks for reading this far. these problems aren't easy to solve. john
and i spent a lot of time trying different things and so i hope that
this doesn't come across as if we think we know better. i would have
commented on the other pr what changes to make but we needed to try out
different solutions in order to get here.

ultimately we're aiming to change as little as the api as possible. even
if the handler/role -> manager -> db_config/pool/etc isn't how we'd
design connection management if we could start over, we also don't want
to break public apis. it's important that we make things better while
maintaining compatibility.

the `rolemanager` class makes it possible for us to fix the underlying
problem while maintaining all the backwards compatibility in the public
api.

we all have the same goal; to add sharding support to rails. let me know
your thoughts on this change in lieu of #37388 and if you have questions.

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277221

###Profanity Found
**Text**
`activesupport::hashwithindifferentaccess#convert_value` appeared quite high in some production profile so i took a look and found that weird `binding` access.

digging into the git history to figure the reason, it seems it originate from https://github.com/rails/rails/pull/36758 and then https://github.com/rails/rails/commit/64a430129fbec2320054a8fc85672994f38a9ee0

the initial goal was to reduce the allocation in that hotspot by using keyword arguments. but since `for` is a keyword, `binding.get_local_variable` was used as a workaround. 

however `binding` does allocate a new `binding` instance on each invocation, and is a quite slow method.

but since `convert_value` is a private method, i think we can simply rename the argument, and avoid all of that.

i adapted the benchmark from https://github.com/rails/rails/pull/36758: 

```ruby
require 'bundler/inline'

gemfile(true) do
  source 'https://rubygems.org'
  gem 'activesupport'
  gem 'benchmark-ips'
  gem 'memory_profiler'
end

require 'active_support/all'

class optimizedhashwithindifferentaccess < activesupport::hashwithindifferentaccess
  private

  empty_hash = {}.freeze

  # convert to a regular hash with string keys.
  def to_hash
    _new_hash = hash.new
    set_defaults(_new_hash)

    each do |key, value|
      _new_hash[key] = convert_value(value, conversion: :to_hash)
    end
    _new_hash
  end
  
  def []=(key, value)
    regular_writer(convert_key(key), convert_value(value, conversion: :assignment))
  end
  
  def convert_value(value, conversion: nil) # :doc:
    if value.is_a? hash
      if conversion == :to_hash
        value.to_hash
      else
        value.nested_under_indifferent_access
      end
    elsif value.is_a?(array)
      if conversion != :assignment || value.frozen?
        value = value.dup
      end
      value.map! { |e| convert_value(e, conversion: conversion) }
    else
      value
    end
  end
end

num_values = 25
source = num_values.times.each_with_object({}) { |i, result| result["key#{i}"] = i }

benchmark.ips do |x|
  x.report("original") { activesupport::hashwithindifferentaccess.new(source) }
  x.report("optimized") { optimizedhashwithindifferentaccess.new(source) }
  x.compare!
end

original_memory = memoryprofiler.report do
  activesupport::hashwithindifferentaccess.new(source)
end

optimized_memory = memoryprofiler.report do
  optimizedhashwithindifferentaccess.new(source)
end

puts "memory change: #{(original_memory.total_allocated_memsize - optimized_memory.total_allocated_memsize)} bytes"
```

produce the following output:
```
warming up --------------------------------------
            original    11.834k i/100ms
           optimized    12.398k i/100ms
calculating -------------------------------------
            original    126.947k (±10.8%) i/s -    627.202k in   5.009570s
           optimized    128.584k (±11.3%) i/s -    644.696k in   5.084137s

comparison:
           optimized:   128584.3 i/s
            original:   126946.7 i/s - same-ish: difference falls within error

memory change: 5800 bytes
```

@kaspth @rafaelfranca 

cc @etiennebarrie @edouard-chin @paracycle @morriar @ignacio-chiazzo

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277362

###Profanity Found
**Text**
hello, i found out useful to use explain output sometimes. for example in postgresql it is possible to get estimated rows and in combination with `find_in_batches` it can be used to show estimated progress.

currently it is needed to parse `explain` message or use lower level api:

```ruby
# postgresql example
json.parse(activerecord::base.connection.exec_query("explain (format json) #{relation.to_sql}").to_a[0].values[0]
#=> [{"plan"=>{"node type"=>"result", "parallel aware"=>false, "startup cost"=>0.0, "total cost"=>0.01, "plan rows"=>1, "plan width"=>4}}]
```
in this pull request i'm introducing new optional argument to `relation.explain` and support `:text` (current and also default option) and new `:json` which will return json version of explain output already parsed to `hash` by `json.parse`. it returns  explains of all queries including binds (where possible) in following hash:

```ruby
{ [sql, binds] => explain_plan_hash, ... }
```

:information_source: _this is initial simple and naive implementation just to share some code and start discussion. i still need to check if all supported postgresql and mysql versions support this. also i think some refactorings can be done, for example `activerecord::explain#exec_explain` can be split to two private methods and so on..._

postgresql example:

```ruby
pp car.where(name: "honda").explain(:json)
{["select \"cars\".* from \"cars\" where \"cars\".\"name\" = $1",
  [["name", "honda"]]]=>
  [{"plan"=>
     {"node type"=>"seq scan",
      "parallel aware"=>false,
      "relation name"=>"cars",
      "alias"=>"cars",
      "startup cost"=>0.0,
      "total cost"=>19.75,
      "plan rows"=>4,
      "plan width"=>76,
      "filter"=>"((name)::text = 'honda'::text)"}}]}
```

mysql usage:

```ruby
pp car.where(name: "honda").explain(:json)
{["select `cars`.* from `cars` where `cars`.`name` = 'honda'", []]=>                         
  {"query_block"=>                                                                             
    {"select_id"=>1,                                                                           
     "table"=>
      {"table_name"=>"cars",
       "access_type"=>"all",            
       "rows"=>2,
       "filtered"=>100,
       "attached_condition"=>"cars.`name` = 'honda'"}}}}
```

sqlite3 usage (not supported):

```ruby
pp car.where(name: "honda").explain(:json)
#=> notimplementederror
```

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277437

###Profanity Found
**Text**
i'm using ctes quite often in rails applications and i think they deserve to be first class citizens in active record.

this is initial port of https://github.com/kmurph73/ctes_in_my_pg (which is based on https://github.com/davyjoneslocker/postgres_ext) with removed `pg` dependency and without recursive support. recursive support can be added later if needed, but i'm not sure about the api for now.

:information_source: ~~there is [one known problem](https://github.com/kmurph73/ctes_in_my_pg/issues/6), i'll take a look if it is still present and try to fix it as well.~~ fixed in this pr

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277440

###Profanity Found
**Text**
### summary

the rails guides contain an example of how to raise for a missing
translation when `i18n.t` is called from anywhere, including
non-actionview contexts. the example builds a custom exception handler
that catches and raises any instance of `i18n::missingtranslationdata`
and passes on any other exception to be handled by `i18n` as normally
happens.

unfortunately, while `i18n::missingtranslationdata` is what eventually
should be raised for a missing translation, the initial exception the
handler sees is actually `i18n::missingtranslation`, and
`missingtranslationdata` is the product of calling `#to_exception` on
that exception object. as a result, the example in the guides ends up
not raising for missing translations, silently resulting in the return
of the missing translation key. this issue appears to have first been captured in this issue: https://github.com/rails/rails/issues/13429.

this change updates the guides to with a working example, catching
`i18n::missingtranslation` which results in a raise of
`i18n::missingtranslationdata` with the missing key.

close #13429

##Repo ID: 1

##Contributer ID: None

##Pull Request ID: 277799

###Profanity Found
**Text**
this is only the initial version of how the new error handling could look like. this update utilizes https://github.com/zotero/stream-server/pull/8 , which no longer closes the connection on error, but instead returns it as an error event with a message, code and requestid. this update allows to just use a callback function when creating a subscription, and the function is called when a message from stream-server is received with the same requestid. currently implemented only for subscription creation.

'reconnect on any error' commit makes zotero-api-node/stream.js to handle connection errors (i.e. econnrefused) by itself, instead of allowing them to bubble up to arkivo and crash the process. this is not ideal, because arkivo no longer know about errors inside stream.js. but connection error handler should be wrapped by reconnect logic, and currently the reconnect is handled inside stream.js (zotero-api-node). but for now it's still better than allowing process to crash on typical connection errors.






##Repo ID: 22070

##Contributer ID: 85223

##Pull Request ID: 194282

###Profanity Found
**Text**
add `node` models and api views.

@beneboy i've done a quick initial documentation / partial implementation for this pr. could you take this over. there are several `todo`s and i'm sure you'll see plenty of potential improvements that could be made. 

i've done some preliminary testing using a combination of  the swagger api (when logged in) and `curl` to test unauthenticated response. could you add some unit tests - the `apitestcase`s i wrote in https://github.com/stencila/hub/blob/3ef9233f36c1167c9364ffcda899249b75f0208a/director/api/views_tokens_tests.py might be useful examples.

will also need @alex-ketch's approval that it meets his needs for `gsuita`, including the html response - although those can be iterated on more easily than they api endpoints obviously.

##Repo ID: 25241

##Contributer ID: 167476

##Pull Request ID: 278404

###Profanity Found
**Text**
- add export xml functionality
- add 'close' button to variable view (more styling needed)
- change labels for n and nw
- initial setup for internationalization
- restrict name length to 50 characters for variable groups
- general code cleanup

##Repo ID: 25500

##Contributer ID: 79702

##Pull Request ID: 257231

###Profanity Found
**Text**
i made quite some updates to the addin and now it's a lot more useful than the initial version. the goal is to build something similar with google scholar and mendeley, but within rstudio. i would love to hear some feedback.

<img width="822" alt="screen shot 2018-09-06 at 2 22 19 pm" src="https://user-images.githubusercontent.com/7014590/45177218-557f5900-b1e0-11e8-820a-4a0a08728dd2.png">


##Repo ID: 25985

##Contributer ID: 167216

##Pull Request ID: 216623

###Profanity Found
**Text**
there is a performance penalty when asking for too many rows.
https://wiki.apache.org/solr/solrperformanceproblems#asking_for_too_many_rows

if number of rows is specified and is higher than configured limit (50000),
solr_search first queries solr for a number of records with rows=0.
then the initial number of rows is replaced by real number of records
and solr_search is executed.

##Repo ID: 26049

##Contributer ID: 84102

##Pull Request ID: 217676

###Profanity Found
**Text**
hello, this is a pr to improve on my initial implementation of docdb_update() for src_sqlite() objects (pr #30 ). that implementation just replaced an existing record with a fully new record. 

now, json_patch() of the json1 extension in the sqlite backend is used to enable atomic updates (of parts of the json document), see [https://www.sqlite.org/json1.html#jpatch](https://www.sqlite.org/json1.html#jpatch). 

this is much more appropriate for an docdb_update() method, and i hope you can accept this. thanks for review and comments. 

##Repo ID: 25946

##Contributer ID: 83099

##Pull Request ID: 220084

###Profanity Found
**Text**
bumps [tinymce](https://github.com/tinymce/tinymce-dist) from 5.0.11 to 5.1.4.
<details>
<summary>changelog</summary>

*sourced from [tinymce's changelog](https://github.com/tinymce/tinymce-dist/blob/master/changelog.txt).*

> version 5.1.6 (2020-01-28)
>     fixed `readonly` mode not blocking all clicked links #tiny-4572
>     fixed legacy font sizes being calculated inconsistently for the `fontsize` query command value #tiny-4555
>     fixed changing a tables row from `header` to `body` incorrectly moving the row to the bottom of the table #tiny-4593
>     fixed the context menu not showing in certain cases with hybrid devices #tiny-4569
>     fixed the context menu opening in the wrong location when the target is the editor body #tiny-4568
>     fixed the `image` plugin not respecting the `automatic_uploads` setting when uploading local images #tiny-4287
>     fixed security issue related to parsing html comments and cdata #tiny-4544
> version 5.1.5 (2019-12-19)
>     fixed the ui not working with hybrid devices that accept both touch and mouse events #tny-4521
>     fixed the `charmap` dialog initially focusing the first tab of the dialog instead of the search input field #tiny-4342
>     fixed an exception being raised when inserting content if the caret was directly before or after a `contenteditable="false"` element #tiny-4528
>     fixed a bug with pasting image urls when paste as text is enabled #tiny-4523
> version 5.1.4 (2019-12-11)
>     fixed dialog contents disappearing when clicking a checkbox for right-to-left languages #tiny-4518
>     fixed the `legacyoutput` plugin registering legacy formats after editior initialization, causing legacy content to be stripped on the initial load #tiny-4447
>     fixed search and replace not cycling through results when searching using special characters #tiny-4506
>     fixed the `visualchars` plugin converting html-like text to dom elements in certain cases #tiny-4507
>     fixed an issue with the `paste` plugin not sanitizing content in some cases #tiny-4510
>     fixed html comments incorrectly being parsed in certain cases #tiny-4511
> version 5.1.3 (2019-12-04)
>     fixed sticky toolbar not undocking when fullscreen mode is activated #tiny-4390
>     fixed the "current window" target not applying when updating links using the link dialog #tiny-4063
>     fixed disabled menu items not highlighting when focused #tiny-4339
>     fixed touch events passing through dialog collection items to the content underneath on android devices #tiny-4431
>     fixed keyboard navigation of the help dialog's keyboard navigation tab #tiny-4391
>     fixed search and replace dialog disappearing when finding offscreen matches on ios devices #tiny-4350
>     fixed performance issues where sticky toolbar was jumping while scrolling on slower browsers #tiny-4475
> version 5.1.2 (2019-11-19)
>     fixed desktop touch devices using `mobile` configuration overrides #tiny-4345
>     fixed unable to disable the new scrolling toolbar feature #tiny-4345
>     fixed touch events passing through any pop-up items to the content underneath on android devices #tiny-4367
>     fixed the table selector handles throwing javascript exceptions for non-table selections #tiny-4338
>     fixed `cut` operations not removing selected content on android devices when the `paste` plugin is enabled #tiny-4362
>     fixed inline toolbar not constrained to the window width by default #tiny-4314
>     fixed context toolbar split button chevrons pointing right when they should be pointing down #tiny-4257
>     fixed unable to access the dialog footer in tabbed dialogs on small screens #tiny-4360
>     fixed mobile table selectors were hard to select with touch by increasing the size #tiny-4366
>     fixed mobile table selectors moving when moving outside the editor #tiny-4366
>     fixed inline toolbars collapsing when using sliding toolbars #tiny-4389
>     fixed block textpatterns not treating nbsps as spaces #tiny-4378
>     fixed backspace not merging blocks when the last element in the preceding block was a `contenteditable="false"` element #tiny-4235
>     fixed toolbar buttons that only contain text labels overlapping on mobile devices #tiny-4395
>     fixed quickbars quickimage picker not working on mobile #tiny-4377
>     fixed fullscreen not resizing in an ios wkwebview component #tiny-4413
> version 5.1.1 (2019-10-28)
>     fixed font formats containing spaces being wrapped in `&quot;` entities instead of single quotes #tiny-4275
>     fixed alert and confirm dialogs losing focus when clicked #tiny-4248
>     fixed clicking outside a modal dialog focusing on the document body #tiny-4249
>     fixed the context toolbar not hiding when scrolled out of view #tiny-4265
></tr></table> ... (truncated)
</details>
<details>
<summary>commits</summary>

- [`7fcdd14`](https://github.com/tinymce/tinymce-dist/commit/7fcdd149d2e2f6013c78a965b8fab2bbe011de4f) added version 5.1.4 release.
- [`9332192`](https://github.com/tinymce/tinymce-dist/commit/9332192a57fae1d717780486eabfd2d661e3b7e8) added version 5.1.3 release.
- [`7587e9a`](https://github.com/tinymce/tinymce-dist/commit/7587e9a7d09ea0a2ae16f6628918c1bd18df2baa) added version 5.1.2 release.
- [`782aa38`](https://github.com/tinymce/tinymce-dist/commit/782aa3876f354b8d04fbf1124c4aa440cec9d199) added version 5.1.1 release.
- [`a4eca7a`](https://github.com/tinymce/tinymce-dist/commit/a4eca7a227e4dd97ed4356f708f0f481ab5164cb) added version 5.1.0 release.
- [`7a58a0e`](https://github.com/tinymce/tinymce-dist/commit/7a58a0e3bd83fb3692d4e721c56fa6925e337926) added version 5.0.16 release.
- [`1b86aa4`](https://github.com/tinymce/tinymce-dist/commit/1b86aa4e290ca697a3d645e4e9824a84fdfee388) added version 5.0.15 release.
- [`4ed6cbe`](https://github.com/tinymce/tinymce-dist/commit/4ed6cbe75f468c389a180df9b9c3d050ac3b722c) added version 5.0.14 release.
- [`8595d45`](https://github.com/tinymce/tinymce-dist/commit/8595d45e1dfde79518db8777e5a66836e33ffd46) added version 5.0.13 release.
- [`c5d8e43`](https://github.com/tinymce/tinymce-dist/commit/c5d8e43738cea9b428c50c6ee1d3d9eb6c653a6d) added version 5.0.12 release.
- see full diff in [compare view](https://github.com/tinymce/tinymce-dist/compare/5.0.11...5.1.4)
</details>
<br />

[![dependabot compatibility score](https://dependabot-badges.githubapp.com/badges/compatibility_score?dependency-name=tinymce&package-manager=npm_and_yarn&previous-version=5.0.11&new-version=5.1.4)](https://help.github.com/articles/configuring-automated-security-fixes)

dependabot will resolve any conflicts with this pr as long as you don't alter it yourself. you can also trigger a rebase manually by commenting `@dependabot rebase`.

[//]: # (dependabot-automerge-start)
[//]: # (dependabot-automerge-end)

---

<details>
<summary>dependabot commands and options</summary>
<br />

you can trigger dependabot actions by commenting on this pr:
- `@dependabot rebase` will rebase this pr
- `@dependabot recreate` will recreate this pr, overwriting any edits that have been made to it
- `@dependabot merge` will merge this pr after your ci passes on it
- `@dependabot squash and merge` will squash and merge this pr after your ci passes on it
- `@dependabot cancel merge` will cancel a previously requested merge and block automerging
- `@dependabot reopen` will reopen this pr if it is closed
- `@dependabot close` will close this pr and stop dependabot recreating it. you can achieve the same result by closing it manually
- `@dependabot ignore this major version` will close this pr and stop dependabot creating any more for this major version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this minor version` will close this pr and stop dependabot creating any more for this minor version (unless you reopen the pr or upgrade to it yourself)
- `@dependabot ignore this dependency` will close this pr and stop dependabot creating any more for this dependency (unless you reopen the pr or upgrade to it yourself)
- `@dependabot use these labels` will set the current labels as the default for future prs for this repo and language
- `@dependabot use these reviewers` will set the current reviewers as the default for future prs for this repo and language
- `@dependabot use these assignees` will set the current assignees as the default for future prs for this repo and language
- `@dependabot use this milestone` will set the current milestone as the default for future prs for this repo and language

you can disable automated security fix prs for this repo from the [security alerts page](https://github.com/zotero/web-library/network/alerts).

</details>

##Repo ID: 22068

##Contributer ID: 79283

##Pull Request ID: 259306

###Profanity Found
**Text**
an initial version.

a few points:
- intentionally using docker compose to build and run containers as an alternative to makefiles and/or bash scripts, which would only duplicate what compose does, and may not be compatible on all platforms (ehem, windows).
- relying on docker machine because, as a regular docker user, it's what i use.  i like some of the features that machine provides, and i really don't like logging into the remote machines to perform my `docker` operations.  that said, i'm open to removing the machine dependency, but it would force users to 1) install docker daemon and compose manually on host (as opposed to machine doing it for them), 2) git clone this repo on the host, 3) login to the host to perform all operations.  like i said, this is not my preferred mode of operation.
- pinning jupyterhub dependencies to git commits.  currently relies on jupyterhub commits > 0.5.0, and i haven't quite figured out the release cadence of dockerspawner or oauthenticator.


##Repo ID: 25449

##Contributer ID: 166393

##Pull Request ID: 253671

###Profanity Found
**Text**
## description of the issue/feature this pr addresses

this pr ensures the order of grouped items

## current behavior before pr

grouped items order not kept

## desired behavior after pr is merged

grouped items keep initial order

--
i confirm i have tested this pr thoroughly and coded it according to [pep8][1]
and [plone's python styleguide][2] standards.

[1]: https://www.python.org/dev/peps/pep-0008
[2]: https://docs.plone.org/develop/styleguide/python.html


##Repo ID: 22014

##Contributer ID: 163942

##Pull Request ID: 186968

###Profanity Found
**Text**
these are initial finnish translations for messages not in the original messages.xml.


##Repo ID: 22102

##Contributer ID: 85764

##Pull Request ID: 194404

###Profanity Found
**Text**
this makes it easier to iterate on a debug image which has the same tag.

when debugging, in config.yaml, set:

```bash
hub:
  imagepullpolicy: always
```

after that, change image code and re-upload docker image. there's no need
to edit config.yaml after each reupload.

when not debugging, we default to ifnotpresent.

here's [another explanation](https://kukulinski.com/10-most-common-reasons-kubernetes-deployments-fail-part-2/#10containerimagenotupdating).

how did i test this?

* step 1: i've set imagepullpolicy to "always" in config.yaml.

* step 2: upload initial image, it adds a line to `jupyterhub_config.py`.
```bash
$ kubectl exec hub-deployment-2875592925-659z1  -- cat /srv/jupyterhub_config.py | grep "hi there"
# hi there!
```

* step 3: update this line to say "hi there 2", rebuild image, upgrade.
```bash
helm upgrade kubehub ~/work/github/helm-chart-fork/jupyterhub/ -f ./config.yaml --debug

$ kubectl exec hub-deployment-3530821855-4qw0k  -- cat /srv/jupyterhub_config.py | grep "hi there"
# hi there 2!
```

* step 4: remove “always” from config.yaml. we're now defaulting to "ifnotpresent"

```bash
$ helm upgrade kubehub ~/work/github/helm-chart-fork/jupyterhub/ -f ./config.yaml --debug

$ kubectl exec hub-deployment-568529703-9jc03  -- cat /srv/jupyterhub_config.py | grep "hi there"
# hi there!
```

so the default works too.

i don't know why when using "ifnotpresent" it defaults to version 1 and not version 2, but it's not a problem.


##Repo ID: 25463

##Contributer ID: 142875

##Pull Request ID: 253169

###Profanity Found
**Text**
there is a bug in the read_table fxn when a single column is queried. to see the problem, try (e.g., which cruises are available in this table?):

erddap_table(x='erdcalcofieggcntpos', store=memory(),
             fields=c('cruise'), orderby='cruise', distinct=true)

this is caused by the "[-1,]" used to remove the initial blank record in the read statements. two changes are needed. first, that blank line doesn't occur in single-column tables. so the read functions need to use "blank.lines.skip=false" to prevent a valid row from being removed in single-column queries. second, need to add "drop=false" to the bracket selection so that single-column results aren't reduced to vectors. 


##Repo ID: 26017

##Contributer ID: 83737

##Pull Request ID: 217065

###Profanity Found
**Text**
the "disk(overwrite=t)" currently  is not honored in the erddap_table fxn. so if a user changes his mind about a table saved to disk, he has to delete the file before getting new data. for example:
# initial table

cruises <- erddap_table(x='erdcalcofieggcntpos', fields=c('cruise'),
                        orderby='cruise', distinct=true)
cruises
# oops, i forgot i wanted cruise and ship, default is overwrite=t

cruises <- erddap_table(x='erdcalcofieggcntpos', fields=c('cruise', 'ship'),
                        orderby=c('cruise', 'ship'), distinct=true)
# nope, still reading the existing file instead of overwriting

cruises


##Repo ID: 26017

##Contributer ID: 83737

##Pull Request ID: 217066

###Profanity Found
**Text**
@billdueber initial description:
i was having problems with session files not being unlocked when i needed them, resulting in waits of 30s for some of the ajax calls. one solution (that allows you to stick with the file-based sessions) is to close the session for writing except for when you actually need to write it.

these changes localize the session stuff to a class (coralsession.php) that takes care of opening sessions and closing them for writing (leaving them read-only) to avoid this.

this is a pretty big structural change, but i thought i'd at least get a ball in the air and start a discussion.


##Repo ID: 25212

##Contributer ID: 96174

##Pull Request ID: 181436

###Profanity Found
**Text**
 - removed dependencies on `githug`, `tibble`, `statquotes` and `checkmate`
 - implemented `scrub()`
 - implemented `ignore()` and `unignore()` (closes #22)
 - hid shas from users, they can now directly `go_to()`, and `retrieve()` records using integers (closes #61)
  - bunch 'o' bugfixes
 - made `print.timeline()` more minimal, and handle timelines when checking out past commits:
```
   (1) initial commit
    |  2017-10-29 13:27
    |
   (2) set up project structure
    |  2017-10-29 13:27
    |
   (3) added stuff to readme
       2017-10-29 13:27
     
   ...plus 12 future records (15 in total)
```


##Repo ID: 25700

##Contributer ID: 81455

##Pull Request ID: 213628

###Profanity Found
**Text**
as you may know, we have been using the git2r package extensively for development of [workflowr](https://github.com/jdblischak/workflowr).

@jdblischak opened an issue a little while ago (issue #324), and this is an attempt to add functionality to filter commits by file name---specifically, it recapitulates the behavior of `git log` when provided with the `<paths>` argument to return only commits in which the specified paths are modified.

rather than modify the existing `commits` function (which could have unintended consequences), we implemented a new function `touching_commits` (the name could be changed) with fewer options.

note that we are happy to make additional improvements, such as roxygen2 docs, after getting your initial feedback.

finally, we have noticed that in some cases `touching_commits` does not exactly reproduce the behaviour of `git log <paths>`; it fails to identify some of the modifying commits for reasons we don't understand. we suspect that this is a lower level issue that goes beyond our understand of `libgit2`, and hopefully you will be able to identify the issue more quickly than us. (we can provide you with reproducible examples of this bug.)

##Repo ID: 25895

##Contributer ID: 82684

##Pull Request ID: 218883

###Profanity Found
**Text**
this is an initial pr for
https://jira.duraspace.org/browse/ds-2457

it includes all of the following:
- includes a slightly tweaked, enhanced version of @hardyoyo's awesome pr #31 (to allow dspace-vagrant to work for ides). this replaced pr #31 
- upgrades librarian-puppet to latest version (2.0.1)
- upgrades puppet postgresql module to latest version
- fixes 'apt-spy2' bootstrap script to use dns and be more stable (it was erroring out)
- minor fixes to 'dspace' module's init script for installing java & maven
- removes installing maven via a puppet module (we're already also installing via packages)
- removes installing vim via a puppet module (we should do this in the local boostrap script)
- reorganizes the vagrantfile into sections for easier readability
- other minor readme and formatting changes

enhanced to include:
- switch to using puppetlabs tomcat module (instead of custom)
- auto-detect whether to use ssh or https for github (based on whether ssh works or not) - credit goes to @houshuang's pr #32 for the inspiration to make this happen. this would make pr #32 obsolete as it is now automated.
- enhanced configuration (of both puppet & vagrant) in a new `config/default.yaml` (which is a renaming of `config/common.yaml`). these settings can be locally customized in `config/local.yaml`
- turned off "synced" folders by default (it's slooow), but it's easy to turn on in `local.yaml`

this has turned into a major refactoring of 'vagrant-dspace', but i hope you will agree it's much improved with these enhancements.

i've tested this locally and a full `vagrant destroy` and `vagrant up` works like a charm.


##Repo ID: 22112

##Contributer ID: 85035

##Pull Request ID: 194699

###Profanity Found
**Text**
this pr contains the initial add-on code including the api/jsonapi

##Repo ID: 22002

##Contributer ID: 163942

##Pull Request ID: 186775

###Profanity Found
**Text**
this is mostly just tidying of readme. i tried not to be too invasive, but noted a few things with my "fresh eyes" that hadn't looked at it for a while. other than that, mostly only the following minor things:
- named all code chunks
- included some printed output from the table join operation - maybe delete that again if you think it's too much? but i thought it helped to understand things a bit better
- changed the inline `r nrow(x)` calls to `r format(nrow(x), big.mark=",")` coz that's a really cool function that should be used
- re-jigged the initial descriptions of the three procedures (download, read, format) a bit
- put the disclaimer about "crahses" not "accidents" at the outset, coz i think that's important
- replaced all single-quote quotations with double quotes because they render better and more consistently (and there will be browsers and system configs that won't properly render the former)
- included `devtools::install_github("robinlovelace/ukboundaries")`, because i had to search for that myself!
- `geom_smooth()`-ed the hourly plot for visual consistency with preceding seasonal plot, which has the added benefit of clearly highlighted the distinct peaks in - and only in! - cycling data

now i'll just do similar in the vignette, then we should be done

##Repo ID: 26054

##Contributer ID: 81421

##Pull Request ID: 217737

###Profanity Found
**Text**
when running jhove from a terminal it is not possible to turn off an initial logging statement "severe: testing severe level". would like to remove these few "test?" logging lines of code in a future release.


##Repo ID: 25220

##Contributer ID: 80346

##Pull Request ID: 184069

###Profanity Found
**Text**
one thing that could be improved with this initial support for condor is that if req_nprocs or req_memory are not configured, job submission fails, because the statements defining requestmemory and requestcpus are malformed.  it would be nice to omit these statements if the corresponding variable is empty or provide reasonable defaults.

does this problem affect the other batch systems as well?  if so, perhaps we can have a common solution.


##Repo ID: 25444

##Contributer ID: 144121

##Pull Request ID: 252863

###Profanity Found
**Text**
extension of the initial elasticsearch and kibana logging. the changes probably need documentation. the associated kibana dashboard is [here](https://search-parsl-logging-test-2yjkk2wuoxukk2wdpiicl7mcrm.us-east-1.es.amazonaws.com/_plugin/kibana/goto/7bd4e04faf80d90096730951a1f6ad63). current issues include inconsistent reporting by remote apps and an inconsistent logging 'reentrant' error. current features include task status reporting and remote app resource reporting.

##Repo ID: 25238

##Contributer ID: 128910

##Pull Request ID: 221974

###Profanity Found
**Text**
i think this inches forward a tiny bit.  it sets up the config for an initial connection to the linked postgres database.

i had to move the setup.py call outside of the dockerfile, because it needs to actually see the database server, and docker-compose hasn't set that up yet during build.

at this point, the database seems like it isn't quite configured right yet, and i don't know yet how to actually start up the app.

cc @hectcastro @themightychris

```
msarahan@twilightsparkle:~/districtbuilder$ sudo docker-compose up
starting districtbuilder_redis_1
starting districtbuilder_postgres_1
recreating districtbuilder_django_1
attaching to districtbuilder_redis_1, districtbuilder_postgres_1, districtbuilder_django_1
redis_1     | 1:c 15 sep 02:47:23.353 # warning: no config file specified, using the default config. in order to specify a config file use redis-server /path/to/redis.conf
redis_1     |                 _._                                                  
redis_1     |            _.-``__ ''-._                                             
redis_1     |       _.-``    `.  `_.  ''-._           redis 3.2.10 (00000000/0) 64 bit
redis_1     |   .-`` .-```.  ```\/    _.,_ ''-._                                   
postgres_1  | log:  database system was shut down at 2017-09-15 02:46:59 utc
redis_1     |  (    '      ,       .-`  | `,    )     running in standalone mode
postgres_1  | log:  multixact member wraparound protections are now enabled
redis_1     |  |`-._`-...-` __...-.``-._|'` _.-'|     port: 6379
postgres_1  | log:  database system is ready to accept connections
redis_1     |  |    `-._   `._    /     _.-'    |     pid: 1
redis_1     |   `-._    `-._  `-./  _.-'    _.-'                                   
postgres_1  | log:  autovacuum launcher started
redis_1     |  |`-._`-._    `-.__.-'    _.-'_.-'|                                  
redis_1     |  |    `-._`-._        _.-'_.-'    |           http://redis.io        
redis_1     |   `-._    `-._`-.__.-'_.-'    _.-'                                   
redis_1     |  |`-._`-._    `-.__.-'    _.-'_.-'|                                  
redis_1     |  |    `-._`-._        _.-'_.-'    |                                  
redis_1     |   `-._    `-._`-.__.-'_.-'    _.-'                                   
redis_1     |       `-._    `-.__.-'    _.-'                                       
redis_1     |           `-._        _.-'                                           
redis_1     |               `-.__.-'                                               
redis_1     | 
redis_1     | 1:m 15 sep 02:47:23.354 # warning: the tcp backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128.
redis_1     | 1:m 15 sep 02:47:23.354 # server started, redis version 3.2.10
redis_1     | 1:m 15 sep 02:47:23.354 # warning overcommit_memory is set to 0! background save may fail under low memory condition. to fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
redis_1     | 1:m 15 sep 02:47:23.355 # warning you have transparent huge pages (thp) support enabled in your kernel. this will create latency and memory usage issues with redis. to fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. redis must be restarted after thp is disabled.
redis_1     | 1:m 15 sep 02:47:23.355 * db loaded from disk: 0.000 seconds
redis_1     | 1:m 15 sep 02:47:23.355 * the server is now ready to accept connections on port 6379
django_1    | validated config.
django_1    | generated django settings for publicmapping.
django_1    | generated django settings for reporting.
postgres_1  | error:  function postgis_lib_version() does not exist at character 8
postgres_1  | hint:  no function matches the given name and argument types. you might need to add explicit type casts.
postgres_1  | statement:  select postgis_lib_version()
django_1    | traceback (most recent call last):
django_1    |   file "setup.py", line 180, in <module>
django_1    |     main()
django_1    |   file "setup.py", line 138, in main
django_1    |     management.call_command('syncdb', verbosity=options.verbosity, interactive=false)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 134, in call_command
django_1    |     klass = load_command_class(app_name, name)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 69, in load_command_class
django_1    |     module = import_module('%s.management.commands.%s' % (app_name, name))
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/utils/importlib.py", line 35, in import_module
django_1    |     __import__(name)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/core/management/commands/syncdb.py", line 8, in <module>
django_1    |     from django.core.management.sql import custom_sql_for_model, emit_post_sync_signal
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/core/management/sql.py", line 6, in <module>
django_1    |     from django.db import models
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/db/__init__.py", line 40, in <module>
django_1    |     backend = load_backend(connection.settings_dict['engine'])
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/db/__init__.py", line 34, in __getattr__
django_1    |     return getattr(connections[default_db_alias], item)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/db/utils.py", line 93, in __getitem__
django_1    |     conn = backend.databasewrapper(db, alias)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/base.py", line 11, in __init__
django_1    |     self.ops = postgisoperations(self)
django_1    |   file "/usr/local/lib/python2.7/site-packages/django/contrib/gis/db/backends/postgis/operations.py", line 108, in __init__
django_1    |     'template?' % self.connection.settings_dict['name']
django_1    | django.core.exceptions.improperlyconfigured: cannot determine postgis version for database "district_builder". geodjango requires at least postgis version 1.3. was the database created from a spatial database template?
django_1    | usage: manage.py subcommand [options] [args]
django_1    | 
django_1    | options:
django_1    |   -v verbosity, --verbosity=verbosity
django_1    |                         verbosity level; 0=minimal output, 1=normal output,
django_1    |                         2=verbose output, 3=very verbose output
django_1    |   --settings=settings   the python path to a settings module, e.g.
django_1    |                         "myproject.settings.main". if this isn't provided, the
django_1    |                         django_settings_module environment variable will be
django_1    |                         used.
django_1    |   --pythonpath=pythonpath
django_1    |                         a directory to add to the python path, e.g.
django_1    |                         "/home/djangoprojects/myproject".
django_1    |   --traceback           print traceback on exception
django_1    |   --version             show program's version number and exit
django_1    |   -h, --help            show this help message and exit
django_1    | 
django_1    | type 'manage.py help <subcommand>' for help on a specific subcommand.
django_1    | 
django_1    | available subcommands:
django_1    | 
django_1    | [auth]
django_1    |     createsuperuser
django_1    | 
django_1    | [compressor]
django_1    |     compress
django_1    |     mtime_cache
django_1    | 
django_1    | [django]
django_1    |     cleanup
django_1    |     compilemessages
django_1    |     createcachetable
django_1    |     dbshell
django_1    |     diffsettings
django_1    |     dumpdata
django_1    |     flush
django_1    |     loaddata
django_1    |     makemessages
django_1    |     reset
django_1    |     runfcgi
django_1    |     shell
django_1    |     sql
django_1    |     sqlall
django_1    |     sqlclear
django_1    |     sqlcustom
django_1    |     sqlflush
django_1    |     sqlindexes
django_1    |     sqlinitialdata
django_1    |     sqlreset
django_1    |     sqlsequencereset
django_1    |     startapp
django_1    |     startproject
django_1    |     syncdb
django_1    |     test
django_1    |     testserver
django_1    |     validate
django_1    | 
django_1    | [djcelery]
django_1    |     celery
django_1    |     celerybeat
django_1    |     celerycam
django_1    |     celeryd
django_1    |     celeryd_detach
django_1    |     celeryd_multi
django_1    |     celerymon
django_1    |     djcelerymon
django_1    | 
django_1    | [gis]
django_1    |     inspectdb
django_1    |     ogrinspect
django_1    | 
django_1    | [publicmapping]
django_1    |     changepassword
django_1    | 
django_1    | [redistricting]
django_1    |     database_i18n
django_1    |     exportplans
django_1    |     makelanguagefiles
django_1    |     numusers
django_1    |     reaggregate
django_1    |     removescoreconfig
django_1    |     setup
django_1    | 
django_1    | [staticfiles]
django_1    |     collectstatic
django_1    |     findstatic
django_1    |     runserver
districtbuilder_django_1 exited with code 0
```

##Repo ID: 25236

##Contributer ID: 128283

##Pull Request ID: 220179

###Profanity Found
**Text**
here's an initial set of party helpers which i think is comprehensive of the party module. i consider this pr incomplete as i'd like to still:

- do a pass over the existing code base, docs, and vignettes to see if these changes necessitate changes in other places (e.g., update a vignette or two)
- get your feedback on how i went about this:
    - do we like the function names? e.g., `set_creator` could be called `eml_creator` or `creator`
    - do we want to make these functions to more error checking? they assume sane inputs
    - do we like how i went about writing roxygen docs? specifically prepending the `(class)` to each `@param` and showing that multiple types can be passed with `(type1|type2)`
- improve the examples so each helper function has examples that cover its full abilities

##Repo ID: 25868

##Contributer ID: 147485

##Pull Request ID: 215100

###Profanity Found
**Text**
i found a "bug" when using `get_attributes` to extract attribute metadata from packages on the arctic data center.  it occurs when one or more of the data frames extracted by the following code in `get_attributes` is `null`.  i hesitate to call it a bug because it won't occur when working with a high quality eml.  but i think this is useful as it allows you extract attribute metadata from lower quality emls.  

error occurs if one or more of the following calls returns `null`
```
column_meta <- column_attributes(a)
numerics <- numeric_attributes(a, eml)
chars <- char_attributes(a, eml)
datetimes <- datetime_attributes(a, eml)
factors <- factor_attributes(a, eml)
```
for instance if `datetimes` is `null` then the initial merge (below) in the following call doesn't merge properly.  the function still returns a data.table, but all the information in `numerics` is lost.
```
attr_table <-
merge(merge(merge(numerics, datetimes, all = true), chars, all = true), column_meta, all = true)
```

couple additional notes: 
`devtools::check()` returned a few errors, but i don't think any were related to my branch (i hope!). 

i also noticed a few missing cases of `xml2::` in the various functions called by `get_attributes` that i had to correct before my updated version of `get_attributes` would run locally.  i'd be happy to add these to the pr if you'd like.  

please let me know what you think, i'd be happy to make any changes / suggestions!





##Repo ID: 25868

##Contributer ID: 82447

##Pull Request ID: 215103

###Profanity Found
**Text**
this follows the initial example of using the new() convenience function and the `nexml.tree()` constructor function that wraps that, and expands it to all other classes in the nexml class hierarchy. these constructors are now also exported so that users of the package can program with them
while being insulated from the exact inner workings of initializing and naming classes.

the only classes not receiving a constructor function are the `listofxxx` classes, which are simply glorified lists but not otherwise embedded in the hierarchy (they also don't inherit from base).

also adds documentation, specifically here for the toplevel class (`nexml`). (it turns out that once you start documenting `r cmd check` pulls you into a bottomless documentation pit, because now you can't even miss a single slot, accidentally or on purpose (internal use slots, anyone? 😞)


##Repo ID: 26016

##Contributer ID: 167142

##Pull Request ID: 217039

###Profanity Found
**Text**
## overview

this commit adds the initial config file for pa, with only the minimal amount of configuration needed to have a functional instance.

### checklist

- [x] pr has a name that won't get you publicly shamed for vagueness
- [x] files changed in the pr have been `yapf`-ed for style violations

## testing instructions

 * download `pa_3785.zip` into `/data`
 * `vagrant ssh`
 * `./scripts/configure_custom_data pa_3785.zip`
 * browse to: `http://localhost:8080/` and verify that the instance is minimally functional and contains pa data.


##Repo ID: 25236

##Contributer ID: 128271

##Pull Request ID: 220242

###Profanity Found
**Text**
prior to this commit, there were two ways in which a task would be launched,
depending on whether there were dependencies pending when the task was
created or not.

these two ways were similar but not identical.

this commit makes a single `launch_if_ready` method which captures one of those
launch behaviours - the case where a launch had been deferred.

this commit also changes the initial submission to always submit as if
dependencies were pending, and then immediately calls `launch_if_ready`.

this makes the code easier to follow, i think, as tidying up the separation
of creating a non-running task first, and then separately visiting it
to decide if it can be run.

there is a (hopefully minor) increased expense in visiting all of the dependencies
twice to see if they are done, on task creation (as launch_if_ready always checks
dependencies, even if task creation has just done so).

this refactoring also means that `launch_if_ready` can be called *anywhere* where
there is a possibility that a task has become ready for launch, without needing
further co-ordination of that launching.

##Repo ID: 25238

##Contributer ID: 128900

##Pull Request ID: 222044

###Profanity Found
**Text**
probably not needed, but here's a testplan.
without this pr:
1. submit a new resource with the api_form, but don't fill in the neededby date input. (it should be hidden unless you check the 'urgent' checkbox.)
2. look at the new resource record and you'll see an initial note with a neededby date of 12/31/1969 or 01/01/1970.

with this pr:
2. you should not see a neededby date at all in the initial note section.

##Repo ID: 25212

##Contributer ID: 79580

##Pull Request ID: 194982

###Profanity Found
**Text**
this pr adds support for a cleaner admin check.
the `isadmin`, `istenantadmin` and `isglobaladmin` methods are now exposed on the `user` model. the methods that were on the `context` object have been removed so it now only holds `tenant` and `user` methods.

you can check if a user is an admin by doing:

``` javascript
if (ctx.user().isadmin()) {
...
}
```

a global admin gets created once on server startup  with the default account/password: `administrator/administrator` there is no functionality for logging in but that should be coming up shortly.

i've started to move some initial logic into oae-tests/lib/ so we don't replicate code all over our unit tests.


##Repo ID: 25206

##Contributer ID: 79267

##Pull Request ID: 178713

###Profanity Found
**Text**
this adds support for sf for the main functions associated with spatiallinesnetworks. the function names remain the same so do not require changes to switch from sp to sf.

using a very slightly modified version of @mpadge's code from the bikedata vignette (see below), there is a significant speed improvement from the use of sf (primarily as it avoids the conversion process). i'm sure there is a better way to write some of the code to take more of an advantage of sf but as an initial attempt this seems to work.

```
library(bikedata)
library(stplanr)
library(dplyr)

store_bikedata (city = 'la', bikedb = 'bikedb', quiet = true)

bikedata_sftest <- function() {

  stns <- bike_stations (bikedb = 'bikedb', city = 'la')
  ntrips <- bike_tripmat (bikedb = 'bikedb', city = 'la', long = true)
  
  xlims_la <- range (stns$longitude)
  ylims_la <- range (stns$latitude)
  # expand those limits slightly
  ex <- 0.1
  xlims_la <- xlims_la + c (-ex, ex) * diff (xlims_la)
  ylims_la <- ylims_la + c (-ex, ex) * diff (ylims_la)
  bbox <- c (xlims_la [1], ylims_la [1], xlims_la [2], ylims_la [2])
  # then the actual osmdata query to extract all openstreetmap highways
  highways <- osmdata::opq (bbox = bbox) %>%
    osmdata::add_feature (key = 'highway') %>% osmdata::osmdata_sf()
  
  la_net <- stplanr::spatiallinesnetwork (sl = highways$osm_lines)
  # find the closest node to each station
  nodeid <- stplanr::find_network_nodes (la_net, stns$longitude, stns$latitude)
  # convert start and end station ids in trips table to node ids in `la_net`
  startid <- nodeid [match (ntrips$start_station_id, stns$stn_id)]
  endid <- nodeid [match (ntrips$end_station_id, stns$stn_id)]
  ntrips$start_station_id <- startid
  ntrips$end_station_id <- endid
  
  bike_usage <- sum_network_links (la_net, data.frame (ntrips))
  
  tmap::tm_shape (bike_usage, bbox = matrix(sf::st_bbox(bike_usage[which(bike_usage$numtrips > 10),]),ncol = 2),
                  is.master=true) + 
    tmap::tm_lines (col="numtrips", lwd="numtrips", title.col = "number of trips",
                    breaks = c(0, 200, 400, 600, 800, 1000, inf),
                    legend.lwd.show = false, scale = 5) + 
    tmap::tm_layout (bg.color="gray95", legend.position = c ("right", "bottom"),
                     legend.bg.color = "white", legend.bg.alpha = 0.5)
}

bikedata_sptest <- function() {
  
  stns <- bike_stations (bikedb = 'bikedb', city = 'la')
  ntrips <- bike_tripmat (bikedb = 'bikedb', city = 'la', long = true)
  
  xlims_la <- range (stns$longitude)
  ylims_la <- range (stns$latitude)
  # expand those limits slightly
  ex <- 0.1
  xlims_la <- xlims_la + c (-ex, ex) * diff (xlims_la)
  ylims_la <- ylims_la + c (-ex, ex) * diff (ylims_la)
  bbox <- c (xlims_la [1], ylims_la [1], xlims_la [2], ylims_la [2])
  # then the actual osmdata query to extract all openstreetmap highways
  highways <- osmdata::opq (bbox = bbox) %>%
    osmdata::add_feature (key = 'highway') %>% osmdata::osmdata_sp ()
  
  stns_tbl <- bike_stations (bikedb = 'bikedb')
  stns <- sp::spatialpointsdataframe (coords = stns_tbl[,c('longitude','latitude')],
                                      proj4string = sp::crs("+init=epsg:4326"), 
                                      data = stns_tbl)
  stns <- sp::sptransform (stns, highways$osm_lines@proj4string)
  
  la_net <- stplanr::spatiallinesnetwork (sl = highways$osm_lines)
  # find the closest node to each station
  nodeid <- stplanr::find_network_nodes (la_net, stns$longitude, stns$latitude)
  # convert start and end station ids in trips table to node ids in `la_net`
  startid <- nodeid [match (ntrips$start_station_id, stns$stn_id)]
  endid <- nodeid [match (ntrips$end_station_id, stns$stn_id)]
  ntrips$start_station_id <- startid
  ntrips$end_station_id <- endid
  
  bike_usage <- sum_network_links (la_net, data.frame (ntrips))
  
  tmap::tm_shape (bike_usage, bbox = sp::bbox(bike_usage[which(bike_usage$numtrips > 10),]), is.master=true) + 
    tmap::tm_lines (col="numtrips", lwd="numtrips", title.col = "number of trips",
                    breaks = c(0, 200, 400, 600, 800, 1000, inf),
                    legend.lwd.show = false, scale = 5) + 
    tmap::tm_layout (bg.color="gray95", legend.position = c ("right", "bottom"),
                     legend.bg.color = "white", legend.bg.alpha = 0.5)
  
}
```

speed difference:
```
> microbenchmark::microbenchmark(bikedata_sptest(), bikedata_sftest(), times = 1)
unit: seconds
              expr       min        lq      mean    median        uq       max neval
 bikedata_sptest() 253.11791 253.11791 253.11791 253.11791 253.11791 253.11791     1
 bikedata_sftest()  56.07455  56.07455  56.07455  56.07455  56.07455  56.07455     1
```

##Repo ID: 26056

##Contributer ID: 82038

##Pull Request ID: 217903

###Profanity Found
**Text**
- ensure branch cleanup happens (if `yield` raises due to test failure, cleanup was being skipped)
- echo build messages to stdout, so they will be in 'captured stdout' report on test failure
- use f-strings because we're on python 3.6! 🎉 

i made two small commits directly to staging to get the build working, since it was preventing successful deploy:

- 056181f403f959b12b3d023bf0b28518da6ec289 ensures the deploy key is used in the initial clone, because *a* key is required to clone with ssh. local testing doesn't run into this because most of us will have a default ssh key that works.
- 657214fa390219d44577e1e3b438029776c91230 fixes permissions on the deploy private key, which git-crypt was unpacking as world-readable and ssh refused to use private keys with open permissions

##Repo ID: 25465

##Contributer ID: 128296

##Pull Request ID: 255220

###Profanity Found
**Text**
this is initial architecture for a mechanism to gather data on the tools users are using, as discussed with @njsmith.

for now, there are two kinds of data we wanted to collect: what versions of packages are in use, and how many users call particular features (especially deprecated features, to inform when they can be removed). obviously there are many more things that might be interesting, but i think we should be taking a minimal, well justified set of data from users rather than just getting whatever we can.

my current thinking is that each of these will be a set, aggregated by month on the user's machine. so you'll see, for instance, that during the last month, a user has used numpy versions x and y, and has called deprecated features a and b. you won't see how many times features were called - i don't think that's terribly useful anyway, because one call to a particular function inside a loop could be called millions of times. four weeks after the last submission, or the next time after that that the server is started, it will submit and discard its data, and start collecting again.

users who haven't previously made a choice will see a prompt of some kind in the notebook interface (not yet implemented) asking them to choose. we don't send any data until they agree, and if they say no, we don't ask again.
### down to the technical details:

to make this mechanism readily available to all kernels, the kernels record data by sending it over a new zmq push socket to the server. the connection file contains an extra entry `"analytics_port": n` if analytics are enabled - this shouldn't cause any problems for kernels that don't know about it. a single pull socket on the server receives information from all kernels.

for now, the analytics messages are single-frame unsigned json messages, rather than routing them through our serialisation machinery. i don't think security is a big concern here - the only malicious possibility i can see is spamming the record of what's in use, and i don't see how we can prevent that given that it would ultimately be submitting to some public server.

this also requires some changes in jupyter_client (coming up) and ipykernel (not yet started). i was thinking of making a separate small package with the api to record information, so that projects wishing to use it could depend on that without depending on all the ipython/jupyter machinery.


##Repo ID: 25237

##Contributer ID: 166466

##Pull Request ID: 220308

###Profanity Found
**Text**
this contribution add to the dspace the ability to import from the major bibliographic database both online than local (file based).
out-of-box it provides plugins to import from:
- doi via crossref api
- pubmedid via webservices
- arxiv
- local bibtex files
- local files in isi plain text format

support for additional providers can be easily implemented, the import is done via ui (currently only the jspui is supported but extension to xmlui should be an easy task for any xmlui experts).
the feature can be turned on/off in configuration, the available plugins are also configurated via dspace.cfg.

mapping from the import format (crossref, pubmed, etc.) to your local dspace metadata is done in external properties files in config/crosswalk (standard mapping is provided).
in mapping files you can define different mapping rule basing on the destination collection (dspace form name) and origin "type" (for example in bibtex you have: @chapter, @book, etc.)
additional hacks for alter the imported values after the initial import or add other values automatically are provided (see the sanitezeimportedmetadata and the enhanceimportedmetadata interfaces).

please note that the bibtex importer use the javabib library (gpl) that can be found here: http://code.google.com/p/javabib/source/browse/#svn%2ftrunk%2freleases%2f20040801

http://dev.davidsoergel.com/nexus/content/groups/public/com/javabib/javabib-bin/

if you want to install them in your local maven repository you can use the following command
mvn install:install-file -dfile=javabib-bin.jar -dgroupid=com.javabib -dartifactid=javabib-bin -dversion=20040801 -dpackaging=jar


##Repo ID: 22104

##Contributer ID: 79682

##Pull Request ID: 194509

###Profanity Found
**Text**
this is an initial pass at updating the readme. i'm going to self merge. my expectation is that there will be future prs on the readme, and this pr is simply to notify users of the current content.

##Repo ID: 25462

##Contributer ID: 122355

##Pull Request ID: 264058

###Profanity Found
**Text**
per http://vufind.org/jira/browse/vufind-425, add mappings to schema.org structured data via rdfa lite for basic bibliographic record attributes and holdings information. this builds on eoghan ó carragáin's initial work and is informed by the most recent w3c schema bib extend community group discussions on holdings.


##Repo ID: 25234

##Contributer ID: 146582

##Pull Request ID: 213384

###Profanity Found
**Text**
this is the initial barebones implementation of the workqueue executor.  it does not have any sort of project-name or project-password or log functionality set up at present.

the general idea is that it creates a shared task dictionary to relate parsl tasks to their future, and a queue to send tasks to the worker.

at executor start, a thread is started to handle the workqueue operations, where the executor sends tasks through the queue to this thread.  the python executables are pickled to a file, and this file is sent along with the task to the worker to be executed with the worker script (`work_queue_worker.py`) that is sent along with each task.

the worker thread monitors the queue, and when it takes values from the queue it submits them, and then waits with a threshold of five seconds for a task before repeating.  when a task is completed, it unpickles the result, and updates the futures that were stored in the dictionary previously.

some issues:
- how to identify the location of the worker script without absolute pathnames

##Repo ID: 25238

##Contributer ID: 128031

##Pull Request ID: 222159

###Profanity Found
**Text**
this adds a new metadata form which is available during the transfer. the goal is to allow metadata to be associated with a transfer containing disk images, and all of the fields contained in the initial set are transfer-specific.

this requires updates to the ui and to the database, in order to provide room to save the metadata. 9f82847ae67fecfc11053e23f00566dc40768dda also makes a major change so that each transfer component (directory chosen from the "browse" menu) now creates an individual transfer, instead of combining into one transfer.

this badly needs to be squashed on merge.


##Repo ID: 25208

##Contributer ID: 164562

##Pull Request ID: 178856

###Profanity Found
**Text**
if i count correctly includes:
 - https://github.com/jupyterhub/binderhub/pull/395
   (remove unused formats for clearsans webfont)
 - https://github.com/jupyterhub/binderhub/pull/396
   (allow setting google analytics domain explicitly)
 - https://github.com/jupyterhub/binderhub/pull/397
   (allow setting google analytics domain from helm chart)
 - https://github.com/jupyterhub/binderhub/pull/399
   (updated initial message in form and clarity to ui element title)
 - https://github.com/jupyterhub/binderhub/pull/401
   (consolidate tips/notes)

##Repo ID: 25465

##Contributer ID: 167414

##Pull Request ID: 255306

###Profanity Found
**Text**
contains:
  jupyterhub/binderhub#395
  (remove unused formats for clearsans webfont)
  jupyterhub/binderhub#396
  (allow setting google analytics domain explicitly)
  jupyterhub/binderhub#397
  (allow setting google analytics domain from helm chart)
  jupyterhub/binderhub#399
  (updated initial message in form and clarity to ui element title)
  jupyterhub/binderhub#401
  (consolidate tips/notes)
as well as incident report of previous deployment to staging.


##Repo ID: 25465

##Contributer ID: 167414

##Pull Request ID: 255307

###Profanity Found
**Text**
- add travis.yml for setting up tests
- dev-requirements installs pytest, pytest-asyncio
- tests/test_authenticator has a single basic test for the initial authenticate
- add missing dependency on jupyterhub

##Repo ID: 25457

##Contributer ID: 128296

##Pull Request ID: 252962

###Profanity Found
**Text**
i write a first draft of the initial page of our rest contract to move thing ahead and facilitate more discussion.
probably it will be better to split the different sections in dedicated sub-pages. i have reserved the (not yet created) endpoints.md page for the discussion around each endpoint but i have preferred to keep all the other things in a single page at the start so that anyone can fastly check "the whole"

##Repo ID: 22118

##Contributer ID: 79682

##Pull Request ID: 194743

###Profanity Found
**Text**
this is a starting point proposal for the contract of the workflow endpoints in the new rest api.
the implementation of a workflow state machine actions is widely debated question and there are lot of discussion about the best way to implement them in a restful way or criticism about which implementation is not really restful.
this is a good summary of the different possible approaches
http://www.kennethlange.com/posts/modeling-workflows-in-rest-apis.html

these are also useful resource to listen different opinions, pro and contros
https://restful-api-design.readthedocs.io/en/latest/methods.html#actions
https://github.com/interagent/http-api-design/issues/58
https://www.gvj-web.com/blog/custom-actions-your-rest-api


at the end my preferred approach is in the middle between the approach "2. transition links" and "3. transition subresource" of the above summary.

we have explicit tasks resources that help us to drive the state change. we can post on such resources and delete tasks. at the start i was uncertain about the use of post but it should be noted that post doesn't allow the client to expect to be able to make a subsequent get request on the same resource to retrieve the data that was sent, so it is the right http verb compared to put.

on the proposed contract i don't like the way that "command" are executed on the existent workflow action. for instance we have an action state name "editaction" in the dspace xml workflow that can receive two commands: approve or reject. there is no standard way to know which commands are allowed for which action state. i plan to fix that later introducing subresources so that on a specific tasks the client known which are the available commands i.e.
- /api/claimedtasks/1/approve
- /api/claimedtasks/1/reject

anyway, i have preferred to share the current contract that we are implementing to provide initial workflow capabilities in dspace 7 to start the discussion. 

##Repo ID: 22118

##Contributer ID: 79682

##Pull Request ID: 194754

###Profanity Found
**Text**
as promised, here's my library of (averaged) perceptrons, adapted from initial code by leif johnson.

still todo:
- ~~design an online learning interface~~
- ~~rewrite the sparse version using scipy.sparse (previous attempts failed as they got very slow) or cython~~
- ~~write tests~~
- ~~add bias vector~~
- adapt to linear classifier interface (coef_ etc.)?


##Repo ID: 25240

##Contributer ID: 129063

##Pull Request ID: 223089

###Profanity Found
**Text**
this adds a new "transcribe files" microservice. the primary initial usecase is ocr. transcription commands are fpr commands, like normalization. ocr should be saved into a sip in objects/metadata/ocrfiles.

ocr data will be included in a dip if it exists, and will be copied into an `ocrfiles` directory at the root of the dip.

requirements are here: https://www.archivematica.org/wiki/ocr_text_in_dip

this depends on #22.

~~note that this isn't 100% ready to merge: i need to unify the post-normalization chains first. currently transcribefile is only called in one of them.~~


##Repo ID: 25208

##Contributer ID: 164562

##Pull Request ID: 178877

###Profanity Found
**Text**
this issue is related to some sirsi customers experiencing long resource search load times when they have 100,000 + resources in their system. it is related to #256, but uses a much simpler fix than the one i proposed there.

as explained in #256, the root cause is the order by statement. but this can be overridden in the [configuration file](https://github.com/coral-erm/coral/blob/master/resources/admin/configuration_sample.ini#l18) by setting default sort to an empty string.

however, after doing this we still saw load times upwards of 30 seconds because the resource index page makes 2 queries per page load. one to [get the resources](https://github.com/coral-erm/coral/blob/master/resources/ajax_htmldata/getsearchresources.php#l35), and another to get the [search result count](https://github.com/coral-erm/coral/blob/master/resources/ajax_htmldata/getsearchresources.php#l24). 

both queries do a number of left joins, which was additionally adding to the slow load times. the existing code does some selective joining, but there are a number of ["default" joins](https://github.com/coral-erm/coral/commit/c1fc8501dd7ab17303cf18b4b5ede121cd6ae95b#diff-8a0d6c3284dcd145d52d956effda2e8dl843) which aren't required (specifically for the initial page load and searchcount queries).

this is a different approach to the selective join process, which creates an [array of potential joins](https://github.com/coral-erm/coral/commit/c1fc8501dd7ab17303cf18b4b5ede121cd6ae95b#diff-8a0d6c3284dcd145d52d956effda2e8dr771). each item in the array is a key value pair:

__key__ the sql alias for the joining table
__value__ and array consisting of:
1. __stmt__: the joining sql statement
2. __requires__ (optional): the table that is required to join the desired table to the resource table.

for example:

the at (acquisitiontype) table cannot be directly linked to the resource table. it is linked through the  resourceacquisition table. thus, `"requires" => "ra"` will result in the following sql

```sql
left join resourceacquisition ra on r.resourceid = ra.resourceid
left join acquisitiontype at on ra.acquisitiontypeid = at.acquisitiontypeid
```

##Repo ID: 25212

##Contributer ID: 79572

##Pull Request ID: 258288

###Profanity Found
**Text**
this allows us to do the transcoding on a working copy and not download
the original from fedora to do initial transcoding.

fixes #85 


##Repo ID: 22038

##Contributer ID: 165073

##Pull Request ID: 188746

###Profanity Found
**Text**
based on our discussions earlier, i'm working on a code review guide. this documents the process and best practices from an archivematica point of view - hoping to make this pr an open discussion.

the guide isn't finished, but i'm putting it up in this initial state so we can start discussion right away!

(the actual guide won't live in this repo; it's just made from here so there can be a pr to act as a discussion.)


##Repo ID: 25208

##Contributer ID: 164562

##Pull Request ID: 178900

###Profanity Found
**Text**
i've created an initial version of a sparse implementation of minibatchkmeans clustering based on `scikits.learn.cluster.minibatchkmeans` - i'd like to use this as an sparse clustering prototype to come up with a proper api for sparse clustering algorithms. you can find an document clustering example in examples/document_clustering.py. 

i've implemented the sparse version analogous to the sparse svm or linear_model modules. this, however, requires that the user picks the appropriate implementation for her task at hand (either cluster.minibatchkmeans or cluster.sparse.minibatchkmeans). first, i wanted to integrate the functionality into the existing code base but it turned out that the code base of both versions are fundamentally different due to the different data structures that they use... maybe the original authors of minibatchkmeans can comment on this and prove me wrong.

currently, it only supports `init='random'` and only has a `n_iter` stopping condition.

another conceptual difference to the dense version is that it uses an index array to create the mini batches instead of shuffling the data array and splitting it (my gut feeling says that this should be faster...)

the mini-batch updates are written in cython using similar tricks as in `sgdclassifier` (e.g. centroids are represented by a dense vector + a scaling vactor)) - see sparse/_fast_kmeans.pyx. the current implementation clusters the training set of the 20 newsgroups corpus (~11.000 samples) in about 2 minutes or less depending on how you tune `chunk_size` - most of the time is spent on distance computations (basically a product: csr_matrix \* ndarray ) - maybe we can optimize this further.

note: not ready for merging yet - no tests - not pep8'ed!


##Repo ID: 25240

##Contributer ID: 129068

##Pull Request ID: 223112

###Profanity Found
**Text**
this pr addresses issue #26.

what's posted is actually fine (resulting tree in plotly account is what you expect online).

value `kwargs$filename` is preserved under `tojson()` but then under `postform()` some parsing issue generates the double directory prepending...  which in turns propagates to `fromjson()` -- i'm talking about https://github.com/ropensci/plotly/blob/master/r/plotly.r#l107

that's why i suggest overwriting `resp$filename` with the initial `kwargs$filename` so the returned response is what you expect -- no impact on what's actually sent to plotly (as the web platform).

note that the resulting plotly plot is private by default -- is this what we expect?

/cc @sckott @chriddyp 


##Repo ID: 25968

##Contributer ID: 107305

##Pull Request ID: 216217

###Profanity Found
**Text**
`highlight.js` highlights when the document load is complete, but in the shiny document case the document's already loaded when the reactive doc's content is inserted into the dom, so the load event doesn't fire. 

the fix is to check to see whether `highlight.js` is being injected when the document's initial load is already complete. when it is, we initialize highlighting immediately after control returns to script (after the code blocks below have been added to the dom).  


##Repo ID: 25239

##Contributer ID: 154897

##Pull Request ID: 222547

###Profanity Found
**Text**
this pr adds an initial rest endpoint to track statistics.

https://jira.duraspace.org/browse/ds-3574

##Repo ID: 22118

##Contributer ID: 85848

##Pull Request ID: 194792

###Profanity Found
**Text**
the configurable workflow supports configurable and customizable steps. depending on the workflow step, different features are supported, and different buttons should be displayed.
the configuration should be exposed using the rest contract. this should ensure the ui will be able to identify whether accept, reject and/or edit metadata buttons should be displayed for the basic steps.
more advanced workflow steps such as the select reviewer step and the score review step may need additional configuration, but that part has not been included for this initial rest contract to keep the complexity limited.

sample actions are already documented at https://github.com/dspace/rest7contract/blob/master/claimedtasks.md#post-method-single-resource-level

##Repo ID: 22118

##Contributer ID: 85808

##Pull Request ID: 252472

###Profanity Found
**Text**
simplify configurationmanager by factoring out methods that don't deal with simple properties-like stuff.

i apologize for the large amount of whitespace adjustment in the initial commit.  i think that netbeans was normalizing whitespace in every file that it touched when auto-refactoring.  it's all stuff that should be done, but it does clutter up the diffs.


##Repo ID: 22104

##Contributer ID: 146589

##Pull Request ID: 244575

###Profanity Found
**Text**
if default setup requested, post the initial user and api key to the storage service when registering. if successful, add the ss hostname to the api whitelist.


##Repo ID: 25208

##Contributer ID: 79364

##Pull Request ID: 178954

###Profanity Found
**Text**
i have tried to make the mean shift clustering implementation located in learn/cluster/mean_cluster_.py more scalable.  i have also tried to improve the initialization by allowing initial kernel positions to be specified as an argument, and by providing the function get_bucket_seeds to automatically detect seeds in a scalable manner.

in cases of low dimensionality, i have decresed the computational complexity of the algorithm by using ckdtree from scipy.spatial to to look up all points within a given euclidean distance of the center of a cluster).

i have also removed a bug/problem that was acknowledged in the comments of old mean_shift_implementation which, in the case of duplicate clusters, biased the cluster centers to be near the later-detected duplicate clusters.  instead if there is a duplicate, the position cluster with the most support (points within its bandwidth) is now selected.

i was in contact with alexandre gramfort, one of the authors of the previous mean_shift implementation.  perhaps he would be a good person to look this code over.


##Repo ID: 25240

##Contributer ID: 129140

##Pull Request ID: 223175

###Profanity Found
**Text**
https://jira.sakaiproject.org/browse/sak-29135

portal.mathjax.website.url was part of the initial mathjax feature, however it was removed during one of the revisions.

the sakai.property remains and should be removed. 


##Repo ID: 25229

##Contributer ID: 81000

##Pull Request ID: 205426

###Profanity Found
**Text**
this is an initial implementation of support for hierarchical facets (bootstrap only). includes fixes to issues in hierarchy tree in bootstrap theme (encountered when upgrading jstree).

this is a bit larger than i would have liked due to needing to upgrade jstree. i also found a few bugs in the hierarchy tree code and tried to make it work properly when i converted it to the new jstree. minimal sample records for testing can be found at https://github.com/kdk-alli/ndl-vufind/wiki/hierarchical-facets-sample-json

the urlqueryhelper changes were done because getparamarray is so slow that it caused a severe slowdown and i couldn't come up with a better solution. maybe another solution could be devised for an overall performance improvement.

changes in results.php should also improve performance when retrieving coordinates for map display.


##Repo ID: 25234

##Contributer ID: 96629

##Pull Request ID: 213527

###Profanity Found
**Text**
this attempts to address the changes to the neighbors module which were recently discussed on the mailing list. (see discussion thread <a href="http://sourceforge.net/mailarchive/forum.php?thread_name=cac8mkjzwrhdzb5j1b8fiw5ke%2bbfpqvmzmjfr%3d%3dlb8vftcbpy1q%40mail.gmail.com&forum_name=scikit-learn-general">here</a>)

the basic idea is this: i've written a `nearestneighbors` class which implements all unsupervised neighbors-based learning methods.  it provides a uniform interface for brute force, `balltree`, and `ckdtree`.  i've made `neighborsclassifier` and `neighborsregressor` inherit from `nearestneighbors`.  i think this is the correct thing to do here. it meets the lsp because both of these classes should be valid inputs into functions like `kneighbors_graph`, where only the unsupervised functionality is used.

i've made `kneighbors_graph` and `radius_neighbors_graph` into methods of `nearestneighbors`, and kept the old stand-alone versions as convenience functions.

the new version retains nearly complete backward compatibility with the old version (aside from the order of keyword arguments in some cases).  the test-suite passed with no modification.

a few issues to think about:
- i've included `ckdtree` as an option in `nearestneighbors`.  this adds flexibility for free, but breaks picklability.  i did this mainly to ease the task of comparing execution times for the three neighbors search methods.  if picklability is a concern, we could still keep `ckdtree` and write `__getstate__` and `__setstate__` such that the kd-tree is rebuilt on deserialization.
- for completeness, i'd need to implement a new version of `barycenter_weights` which works in cases where `k` is different for each neighborhood (i.e. in `radius_neighbors_graph`).  @fabianp has mentioned in the past that `barycenter_weights` may be removed at some point.  this would be a great time to make that decision.
- i'm not completely happy with the `classification_type` keyword.  it could be misleading: for example, if someone creates a classifier using `neighborsclassifier(r_neighbors=0.5)`, any prediction will still be performed using `kneighbors()` with the default `n_neighbors=5`, not `radius_neighbors()` as the user may naively expect.  we could try to anticipate this by checking which keywords are passed to the constructor, but this could lead to other sources of confusion.
- the `method='auto'` decision process should be more sophisticated, as mentioned in issue #195.  i'm writing a profiler suite which will help address this.  with the new cython version of `balltree` in place, initial tests make it look like `method='auto'` will simply end up choosing `balltree` in all cases.

i'm waiting on people's input before i fully update tests and documentation, and comb the code-base to make sure the appropriate neighbors object is being used in all cases.


##Repo ID: 25240

##Contributer ID: 129062

##Pull Request ID: 223204

###Profanity Found
**Text**
reenables functionality #410 

important point:
- removed one file.exists check in fileutil.java expandpath
  i think one check after replacing / and \ is enough, without checking the expanded path with directory in front.
- cache is filled at initial creation for bibdatabase, therefore no checks against the whole database are done for each file entry
- parse logic for file field should moved from the filelisttablemodel to filefield.java.

we could still improve quite a lot here but maybe its good enough :tm: for now.


##Repo ID: 25219

##Contributer ID: 80087

##Pull Request ID: 195446

###Profanity Found
**Text**
this ticket builds on sak-26069 and sak-28993 which improves the import from site feature to automatically provision existing tools.

this ticket will provide the following features:
1. tools that have names in the sites that have been selected for import, that are different to the standard name for the tool will be shown next to the tool name. this is so that the user can make an informed decision about including that tool, when they might know it by a different name.
2. only tools that contain content will be listed for import. an entity interface will be added that tools can implement that allows them to explicitly say whether or not they have content. there is no point showing a tool for import if it has no content. the initial candidate for this is sitestats but it can be extended to other tools. default will be to include the tool if the interface is not implemented, to maintain backwards compatibility 


##Repo ID: 25229

##Contributer ID: 146614

##Pull Request ID: 205464

###Profanity Found
**Text**
# what this pr does
https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues/476#issuecomment-363972524 - this pr solves the issue that could arise by having more than 50 images on a node.
#477 - i now quite confident it will solve @gerbenwelter issue even though i never pinpointed his issue
#476 - this pr considers my initial issue of finding myself with abandoned k8s resources after helm-upgrade failures by failing future upgrades unless it has been cleaned up.

### about the changes - lower complexity, robust functionality
- i reduced a lot of complexity while maintaining function in the prepuller image code.
- it is no longer is responsible for creating and destroying a daemonset. it will simply wait for the deamonset's status to stabilize ([`desirednumberscheduled == numberready`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.9/#daemonsetstatus-v1-apps)). this requires k8s 1.8+.
- two less rbac resources are now required, and the permission no longer includes daemonset creation.

### techniques utilized
__helm hooks__
```yaml
kind: serviceaccount
metadata:
  annotations:
    # create this resource before the actual helm upgrade is made...
    "helm.sh/hook": pre-install,pre-upgrade
    # ... and before the image-awaiter job (weight 10) but after the hook-image-puller (weight -10) ...
    "helm.sh/hook-weight": "0"
    # ... and then delete it when the image-awaiter job has finished one way or another
    # note: this requires helm 1.7+
    "helm.sh/hook-delete-policy": hook-succeeded,hook-failed
```

### verified behaviour
- [x] helm upgrades are blocked until fresh images are pulled (demo 1)
- [x] hook resources are deleted after successful upgrades (demo 1)
- [x] fresh nodes get images pulled by the continuous image puller (demo 2)
- [x] tainted nodes are supported out of the box (demo 3)

### todo
- [x] verify algorithm's function if nodes are scaling down.
- [x] verify algorithm's function if nodes are cordoned (gets an `unschedulable` attribute).
- [x] attempt to solve cleanup if a helm upgrade is aborted
- [x] test usage in general

### documentation
- [x] update changelog
- [x] update documentation in optimization.md

### concerns 
aborted helm upgrades might result in abandoned k8s resources that will make future helm upgrades fail saying the a certain resource already exist. if this happens, manual cleaning is needed like below. it is somewhat robust already due to the annotation `"helm.sh/hook-delete-policy": hook-succeeded,hook-failed` but i've seen it fail still.

```shell
# manual cleanup of abandoned resources
kubectl delete all --selector hub.jupyter.org/deletable=true
```

### dependencies
- [x] helm 2.7+
- [x] k8s 1.8+

### demo 1 - hook image puller - you will see...
1. a helm upgrade will initiate two helm `pre-upgrade` hooks, the hook-image-puller daemonset first, and instantly thereafter the image-awaiter job.
2. the hook-image-puller daemonset's pod will pull the required images by using dummy init containers, and the image-awaiter will wait for the daemonset status to seem alright and then exit.
3. the hook resources will autodelete themselves.
4. the actual helm upgrade will begin, a new hub pod is created and the old is terminated.

![hook-image-puller2](https://user-images.githubusercontent.com/3837114/36459891-2342bba0-16b6-11e8-8f5c-2c83b5494945.gif)

### demo 2 - continuous image puller + cluster autoscaler - you will see...
__warning - the gif is 3-4 minutes__
1. many user arrives
2. an additional node is made available by the cluster autoscaler
3. all user leave
4. (not seen in gif - cluster scales down)
![continuous-image-puller-up](https://user-images.githubusercontent.com/3837114/36466460-a5877c94-16da-11e8-9984-5b99b620b6d0.gif)

### demo 3 - tainted and cordoned nodes - you will see...
1. the daemonset status before...
2. ... and that it reacts great after a noschedule taint is applied

__related commands__
```shell
# apply taint
kubectl taint node <nodename> key=value:noschedule
# remove taint
kubectl taint node <nodename> key:noschedule-

# not in demo, but tested (makes the node marked unschedulable)
kubectl cordon <nodename>
kubectl uncordon <nodename>
```

![tainted](https://user-images.githubusercontent.com/3837114/36499910-f2e00bb0-1742-11e8-8838-0b4a32d8eb39.gif)


##Repo ID: 25462

##Contributer ID: 142678

##Pull Request ID: 264264

###Profanity Found
**Text**
this allows for the multi-up panels to be drag-and-droppable on initial block instantiation.


##Repo ID: 25232

##Contributer ID: 79472

##Pull Request ID: 212423

###Profanity Found
**Text**
this is mostly an academic change with zero functional impact for users but i think it's the "correct" approach for adding assertions to r6 classes, so it might be useful as a reference if nothing else. 

in the current implementation assertions are only applied when updating the fields of an existing object, so it's possible to initialize an object with an invalid value:

``` r
config <- vcr:::vcrconfig$new(record = "once")
config$record <- 1
#> error in check_record_mode(value): is.character(x) is not true

vcr:::vcrconfig$new(record = 1)
#> <vcr configuration>
#>   cassette dir: .
#>   record: 1
#>   uri parser: crul::url_parse
#>   match requests on: method, uri
#>   preserve bytes?: false
#>   logging?: false
#>   ignored hosts: 
#>   ignore localhost?: false
#>   write disk path:
```

with this new change, initial arguments are passed to the active binding rather than being assigned directly to their private field, so assertions are applied in both cases:

``` r
config <- vcr:::vcrconfig$new(record = "once")
config$record <- 1
#> error in check_record_mode(value): is.character(x) is not true

vcr:::vcrconfig$new(record = 1)
#> error in check_record_mode(value): is.character(x) is not true
```

<sup>created on 2020-02-19 by the [reprex package](https://reprex.tidyverse.org) (v0.3.0)</sup>

you have way more experience with r6 so i'm curious to see what you think and whether i'm missing something. 

##Repo ID: 26080

##Contributer ID: 82290

##Pull Request ID: 260397

###Profanity Found
**Text**
attempting to cull a user whose server is slow to stop results in a `400 delete` error, which seems to exit the culler process.

user will be deleted in a later round when the server has finished stopping.

the initial request in `call_sync` was failing, which causes the script to exit. this is replaced with an `add_callback`, in which case errors are logged instead of exiting.

closes #522

##Repo ID: 25462

##Contributer ID: 128296

##Pull Request ID: 264276

###Profanity Found
**Text**
commit fe101c585d89d9b2182e7eb5e2d6e3f39bd36970 fixed a bug where the initial value for the "keyword" dropdown, "term", would be sent as an empty string. however, the bug recurs for any subsequent rows that are added using the "add new" button. this fixes this issue by adding a row template as a parameter to the advanced search javascript, and creating both initial and subsequent rows from that template rather than naively.

refs #8292.


##Repo ID: 25208

##Contributer ID: 164562

##Pull Request ID: 179062

###Profanity Found
**Text**
if any other user (or the initial user, in a new tab) starts editing the page,
they should receive an alert that the page is being edited and to proceed with
caution.

![screen shot 2014-11-17 at 1 29 05 pm](https://cloud.githubusercontent.com/assets/111218/5078116/8cc51216-6e5e-11e4-9043-2773ce50dca0.png)

fixes #364 


##Repo ID: 25232

##Contributer ID: 167747

##Pull Request ID: 212458

###Profanity Found
**Text**
following up on the hydra tech call agenda item 2014-10-08.3.e, this
is an initial straw person to push against and help form the ongoing
process for collaborating on hydra::works

see the following link for reference:

  https://wiki.duraspace.org/display/hydra/hydra+tech+call+2014-10-08

related to projecthydra-labs/hydra-works#6


##Repo ID: 22043

##Contributer ID: 164558

##Pull Request ID: 189285

###Profanity Found
**Text**
this pull request was the initial one for #4230 modular configure

##Repo ID: 25213

##Contributer ID: 166606

##Pull Request ID: 181914

###Profanity Found
**Text**
this is an initial implementation that addresses #73. it adds the `files` direct container to works and provides a mechanism for designating one of them as a pcdm.thumbnail.


##Repo ID: 22043

##Contributer ID: 79479

##Pull Request ID: 189317

###Profanity Found
**Text**
closes #182 

note: i have not tested this for my use case yet. @betatim suggested this course of action, and i'm putting it up here for initial comments/redirections while i proceed with testing my binder implementation.

##Repo ID: 25445

##Contributer ID: 135737

##Pull Request ID: 252711

###Profanity Found
**Text**
things that need to be done before we can safely update:

  - [x] integrate `selected` attribute/api with crosstalk framework.
  - [ ] integrate `unselected` attribute/api with crosstalk framework (should `opacitydim` map to `unselected.marker.opacity`, etc?). 
(__update__: i can't think of a good use-case for changing stuff like `marker.color`, `marker.size`, or `textfont.color` for unselected marks, and in fact, i think it just leads to more confusion than usefulness, so i'm not likely going to add integration) 
  - [x] enable persistent selection via 'shift' key (this should work for all valid event types, not just `plotly_selected`)
  - [ ] does it make sense for `selectedpoints` to set an initial crosstalk selection (like `defaultvalues` arg in `highlight()`)?
(__update__: it's definitely not straight-forward how one would use `selectedpoints` in conjunction with crosstalk, and adding support wouldn't enable anything that can't already be done via `defaultvalues` in `highlight()`, so i'm not sure the dev time this would require is necessarily worth it) 
  - [x] wait until fix for https://github.com/plotly/plotly.js/issues/2282 has been included in an official release



##Repo ID: 25968

##Contributer ID: 95318

##Pull Request ID: 216419

###Profanity Found
**Text**
opening this for initial comments, not sure how much time i'll have to follow up in the immediate future.

background
- https://discourse.jupyter.org/t/binderhub-button-pull-from-referrer/1572/
- this also implements some of the "awesome bar" suggestion from https://github.com/jupyterhub/binderhub/issues/844

this adds a new `/autodetect` page that takes the http referrer and converts it to a mybinder url. you can also paste a github repo url, github gist url, gitlab repo url, or zenodo doi into the input box. currently this is a separate page, mostly copied from the main index.html.

example: in a github repo create a readme with a link to `https://binder.example.org/autodetect`, if it works the referrer will be parsed and converted into a link to launch the repo you came from.an earlier example can be seen at https://github.com/manics/mybinder-referrer/tree/demo

![screen shot 2019-07-09 at 17 35 39-fullpage](https://user-images.githubusercontent.com/1644105/60906977-56ee3780-a270-11e9-8af9-602adbf86e32.png)

![screen shot 2019-07-09 at 17 35 58-fullpage](https://user-images.githubusercontent.com/1644105/60906990-5ce41880-a270-11e9-8223-602fd9b5d90b.png)

todo:
- [ ] tests
- [ ] don't hard-code `https://mybinder.org/`

##Repo ID: 25464

##Contributer ID: 142670

##Pull Request ID: 257028

###Profanity Found
**Text**
this shouldn’t have been removed during the initial work as it stops someone changing permissions with a get.


##Repo ID: 25229

##Contributer ID: 80989

##Pull Request ID: 205589

###Profanity Found
**Text**
## description

crosstalk highlight events work by adding/deleting traces as needed. currently, the deleting logic removes _all_ traces added after initial render. this change makes it so only the traces added by crosstalk are removed. 

## example

in the example below you would expect that a new marker is added to the everytime a point is clicked. instead, without this change, only a single marker is added (and moves `x` position after every click)

```r
library(plotly)
library(htmlwidgets)

mtcars %>%
  highlight_key() %>%
  plot_ly(x = ~wt, y = ~mpg) %>%
  add_markers() %>%
  highlight("plotly_click") %>%
  onrender("
    function(el) {
      window.nclicks = 0;
      el.on('plotly_click', function(d) {
        window.nclicks = window.nclicks + 1;
        var trace = {
          x: [window.nclicks],
          y: [10],
          type: 'scatter',
          mode: 'markers'
        }
        plotly.addtraces(el.id, trace);
      })
    }
  ")
```

## testing notes

install `devtools::install_github("ropensci/plotly#1436")` then ensure the example above has the correct behavior


##Repo ID: 25968

##Contributer ID: 95318

##Pull Request ID: 216467

###Profanity Found
**Text**
scaling of variance by samplesize should not be applied to prewhitened data because it belongs to the whitening itself
e.g. https://github.com/scikit-learn/scikit-learn/blob/master/sklearn/decomposition/pca.py#l213

see also my initial comment https://github.com/scikit-learn/scikit-learn/pull/243#issuecomment-1555860
(sorry that i did not brought this to an end)


##Repo ID: 25240

##Contributer ID: 129135

##Pull Request ID: 223352

###Profanity Found
**Text**
i'm not sure if this is what you had in mind, but here's my initial implementation (issue #64)! i'm open to critique and revisions on this. here's what the output looks like for the debug plan:

```
> predict_runtime(plan, envir = envir, from_scratch = t)
import i
import a
import b
import c
import saverds
import 'input.rds'
import readrds
import j
import h
import g
import f
build stage 1 
  targets: myinput 
  est build time: 0s 
build stage 2 
  targets: nextone 
  est build time: 0s 
build stage 3 
  targets: yourinput 
  est build time: 0s 
build stage 4 
  targets: combined 
  est build time: 0s 
build stage 5 
  targets: 'intermediatefile.rds' 
  est build time: 0s 
build stage 6 
  targets: final 
  est build time: 0s 

total build time: 0s 
  0 untimed targets (never built)
  (assuming max_useful_jobs)
  (not including hashing and storage time [yet])
```

##Repo ID: 25864

##Contributer ID: 82355

##Pull Request ID: 214737

###Profanity Found
**Text**
based on the initial ideas in #978 the class singlebibtexfield is extracted and two enumsets are used for implementing the existing functionality.


##Repo ID: 25219

##Contributer ID: 80089

##Pull Request ID: 195624

###Profanity Found
**Text**
## about
i'm reading through most of the initial documentation, up to customizing user environment.

- [the updates i've made in the docs](https://zero-to-jupyterhub-k8s.readthedocs.io/) can be compared with...
- [the current z2jh master docs](https://zero-to-jupyterhub.readthedocs.io/en/latest/)

##Repo ID: 25462

##Contributer ID: 142678

##Pull Request ID: 264448

###Profanity Found
**Text**
- added project skeleton with proposed directories and files
- added build (grunt) with initial includes


##Repo ID: 25222

##Contributer ID: 80420

##Pull Request ID: 184219

###Profanity Found
**Text**
...objects, and integrate it into the viewer. use the addmanifestfromurl method to do initial populating as well. closes #26, closes #29.


##Repo ID: 25222

##Contributer ID: 80390

##Pull Request ID: 184226

###Profanity Found
**Text**
use django's migrations, instead of custom-written sql for database changes.  this assumes #376 will be in 1.5 - fixture data & schema will be re-generated/squashed once that is true.
- add initial schema migration
- load initial data from a fixture using the loaddata command in the data migration
- add migration for changes since 1.5.
- remove all mysql_dev migrations.

todo:
- [x] add fpr migrations & initial data artefactual/archivematica-fpr-admin#14
- [ ] investigate why initial schema migration is slow
- [ ] check for better fixture loading so tests don't have load all production data (or make it faster)
- [ ] test with upgrades
- [x] test with ansible artefactual-labs/ansible-role-archivematica-src#34


##Repo ID: 25208

##Contributer ID: 79364

##Pull Request ID: 179223

###Profanity Found
**Text**
currently the jupyter logo link brings us to the users' dashboard and there is no way to get to the initial screen (containing "stop my server"/"my server"/"admin" buttons)


##Repo ID: 25439

##Contributer ID: 143148

##Pull Request ID: 253808

###Profanity Found
**Text**
solves #779 
the simplest way seems to be by forcing tinymce to spit the original value on initial form load

##Repo ID: 25225

##Contributer ID: 80762

##Pull Request ID: 197816

###Profanity Found
**Text**
use django's migrations, instead of custom-written sql for database changes. 
- add schema migrations for all changes since 1.4.1
- add data migrations for changes since 1.4.1
- use dumpdata fixture for initial data
- update code to reflect data - eg. set auto_now on lastmodified columns, update event creation to actually have unique ids
- includes #395/#417 as a migration
- removes old sql migrations
- includes artefactual/archivematica-fpr-admin#14
- edit: update version & adds version update migration

todo:
- [ ] use data migration instead of loaddata for initial data migration
- [ ] investigate why initial schema migration is slow
- [x] test with upgrades
- [x] test with artefactual-labs/ansible-role-archivematica-src#34


##Repo ID: 25208

##Contributer ID: 79364

##Pull Request ID: 179255

###Profanity Found
**Text**
i'm still working on this, and there's a lot to still do, but i thought i'd leave it open to 
reviewing so long, seeing as i'm still finding my feet with a lot of this stuff..

the code still has lots of comments that will removed later and cleaned up.
the `__main__` function currently houses a little script that i'll turn into an example later.
all the documentation still needs to be done

i'd appreciate any inputs and suggestions with this :)

here's some exerts from the discussion which lead to this (_from the scikit-learn mailing list_)

from **alexandre gramfort**

> hi,
> 
> as soon as we have immanuel's branch with positive lasso [1] merged we
> could have a non-negative
> garotte in the scikit. a quick gist (hopefully not too buggy):
> 
> https://gist.github.com/2351057
> 
> feed back welcome and if someone is willing to cleanly merge this …
> 
> alex

from **jaques grobler**

> here's a wee summary on the non-negative garrote (ng) i pieced together:
> 
> the original non-negative garrote from breiman (1995) is basically a scaled version of the least square >estimate.
> basically take a ols estimator and then shrink that estimator to obtain a more sparse representation.
> the shrinkage is done by multiplying the ols estimator by some shrinkage factor, say `d`,
> which is found by minimising the sum of square residuals, under the restriction that the `d`'s are positive
> and that some are bound by a certain shrinkage parameter.
> 
> the algorithm proposed in this paper, is rather similar to that of the  lars lasso, but with a complicating
> factor being a non-negative constraint on the shrinkage factor. (see eq. (2) in this paper)
> once you've computed  your shrinkage factor, you basically have your regression coefficients
> seeing as your `ng coefficient` = `shrinkage factor` \* `regression coefficient`
> 
> he showed it to be a stable selection method and often outperforms it's competitors like
> subset regression and ridge regression.
> the solution path of the ng is piece-wise linear and it's whole path can be computed quickly.
> it is also path-consistent (a solution that contains at least one desirable estimate) given an appropriate >initial estimate. the path-consistency of the ng is highlighted to be in contrast to the fact that the `lasso` >is not always path consistent (peng zhao & hui zou, personal communication). it is argued that the ng has >the ability to turn
> a consistent estimate into an estimate that is both consistent in terms of estimation and in terms of variable >selection.
> 
> a drawback is the ng's explicit reliance on the full least square estimate, as a small sample size may >cause it to perform poorly - however a ridge regression is suggested as an initial estimate for defining the >ng estimate, instead
> of the least square estimate.

from **jaques grobler**

> appart from trying it ourselves to see how it fares, here're some findings:
> 
> the simulations that are done in the last mentioned paper by ming yuan and yi lin,
> http://www2.isye.gatech.edu/statistics/papers/05-25.pdf,  they find that the ng seems to do
> generally better than the lasso (figure 1)
> 
> their second simulations they consider the 4 different models used in the original lasso paper (tibshirani, >1996)
> which they use to compare the ng with several other popular methods, inluding the lasso.
> the results are shown in table 2 of the above-mentioned paper from which the ng does very well, often >outperforming the other models and being the most successful in variable selection.
> 
> they also include one real example using the prostate cancer dataset from stamey (1989) - the results of >which
> they use to confirm the theory that the path consistency of lasso depends on the correlationo of the >design matrix whilst that of the ng is always path consistent.
> 
> thought it may be of interest

from **alexandre gramfort**

> if you can reproduce this figure 1 using my gist
> 
> it would be a sufficient argument for adding this estimator to the scikit.


##Repo ID: 25240

##Contributer ID: 129069

##Pull Request ID: 223462

###Profanity Found
**Text**
# summary

i have long bemoaned the lack of a suitable message queue, and `liteq` is not working out. however, i implemented `drake`'s own custom message queue (`message_queue.r`) and initial testing is doing far better than the current master branch or the `liteq` branch. there are fewer apparent glitches, and the `"mclapply"`, `"parlapply"`, and `"future_lapply"` backends seem to run a bit faster. the long tests are running as we speak.

after this, #332, and a time buffer to allow more real-world testing, i think `drake` will be ready for a cran update.

# related github issues

- ref: #407

# checklist

- [x] i have read `drake`'s [code of conduct](https://github.com/ropensci/drake/blob/master/conduct.md), and i agree to follow its rules.
- [x] i have read the [guidelines for contributing](https://github.com/ropensci/drake/blob/master/contributing.md).
- [x] i have listed any substantial changes in the [development news](https://github.com/ropensci/drake/blob/master/news.md).
- [x] i have added [`testthat`](https://github.com/r-lib/testthat) unit tests to [`tests/testthat`](https://github.com/ropensci/drake/tree/master/tests/testthat) to confirm that any new features or functionality work correctly.
- [x] i have tested this pull request locally with `devtools::check()`
- [x] this pull request is ready for review.
- [ ] i think this pull request is ready to merge.


##Repo ID: 25864

##Contributer ID: 166911

##Pull Request ID: 214846

###Profanity Found
**Text**
i thought this might have been a deprecated method, but seems like it was just a missing initial slash when trying to initialize the mime.types. http://stackoverflow.com/a/536260

weird error though. maybe could use some better debug messages. the only thing that was coming up up is.

2015-05-27 03:33:57,619  warn localhost-startstop-1 org.sakaiproject.tool.assessment.ui.servlet.initmimetypes - 


##Repo ID: 25229

##Contributer ID: 167349

##Pull Request ID: 205751

###Profanity Found
**Text**
this is an initial shot to get java9 working.

- [x] addresses `java.lang.noclassdeffounderror: javax/xml/bind/jaxbexception` with the solution posted at https://stackoverflow.com/a/43574427/873282.
- [ ] "module config stuff" https://github.com/jabref/jabref/issues/2594#issuecomment-333849933
- [ ] update https://github.com/jabref/org.jabref.gui.customjfx.support
- [ ] update libraries https://github.com/jabref/jabref/issues/2594#issuecomment-331638433
- [ ] make a jar which combines both customfx 8 and customfx 9 - see https://groups.google.com/d/msg/controlsfx-dev/pdaqhp0yfho/qld6eewbagaj
- [ ] circleci update to compile using oraclejdk9 - see <https://github.com/jabref/jabref/wiki/ci> for our general ci strategy

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 196987

###Profanity Found
**Text**
…rterfactory

fixes #3596

this is my initial idea. maybe we can optimize this

<!-- describe the changes you have made here: what, why, ... -->


----

- [ ] change in changelog.md described
- [ ] tests created for changes
- [ ] screenshots added (for bigger ui changes)
- [x] manually tested changed features in running jabref
- [ ] check documentation status (issue created for outdated help page at [help.jabref.org](https://github.com/jabref/help.jabref.org/issues)?)
- [ ] if you changed the localization: did you run `gradle localizationupdate`?


##Repo ID: 25219

##Contributer ID: 80091

##Pull Request ID: 197094

###Profanity Found
**Text**
this addresses https://github.com/jabref/jabref/issues/3586

in the devcall, we decided, that we will try to use gitter and see how it goes.

the main arguments were:
- easy to join for new users
- offer help for new developers since the burden of initial jabref development is high for newcomers - even if we have https://github.com/jabref/jabref/wiki/high-level-documentation and https://github.com/jabref/jabref/wiki/code-howtos
- nearly none of the developers uses slack
- does not clutter the skype chat of the developers
- developers can use [pinned tabs](https://support.mozilla.org/en-us/kb/pinned-tabs-keep-favorite-websites-open) to keep gitter always opened

we will shutdown gitter in case there won't be much support from @jabref/developers there (because lack of time). nevertheless, we give it a chance. 😇 

##Repo ID: 25219

##Contributer ID: 164834

##Pull Request ID: 197109

###Profanity Found
**Text**
add fi locale for the new template added here: https://github.com/pkp/pkp-lib/issues/2434

ps. how do other translators track down these new additions? i think that i follow the development fairly closely but still i did not notice that this new tempalte was added. it was only after a journal contacted me asked whether there could be a template for the initial rejection that i found this. the translator tool does not seem to solve this although it works well with the other translations.


##Repo ID: 25226

##Contributer ID: 80824

##Pull Request ID: 199739

###Profanity Found
**Text**
wip - add external application selection to preferences

this pull request is in regards to #674. 
this initial commit adds a button to the settings panel for each external application which allows the user to select an application to make default. there is currently a problem with this build where the application will not update the pushtoapplicationbutton. i believe the issue has something to do with the interaction between javafx and swing components. also i plan on adding keybinding options as well in the future, it's just taking me a bit of time to familiarize myself with the program between life events. let me know what you think so far and on the direction i am taking.

##Repo ID: 25219

##Contributer ID: 86162

##Pull Request ID: 197298

###Profanity Found
**Text**
hi,
i found a bug where javafx was doing some recalculations during the initial layouting. 
setting `setresizablewithparent` before initial layouting was finished resulted in javafx assuming a wrong fixed width.
i changed that by adding the code to a run later block.

it works good for me on mac. are there any concerns with that?

best regards
kai

- [x] change in changelog.md described
- [ ] tests created for changes
- [x] manually tested changed features in running jabref
- [ ] screenshots added in pr description (for bigger ui changes)
- [ ] [checked documentation](https://docs.jabref.org/): is the information available and up to date? if not: issue created at <https://github.com/jabref/user-documentation/issues>.


##Repo ID: 25219

##Contributer ID: 142180

##Pull Request ID: 261309

###Profanity Found
**Text**
- fix bug in tagbar (added itself instead of newtags)
- wrong number of logger paramters
- inner class may be static
- fix comment typo
- bulk operation can be used instead of iteration
- arrays.aslist with only one element
- optimized count by using numbers earlier
- chained append for stringbuilder
- initialize arraylist by passing the initial contents in the constructor


##Repo ID: 25219

##Contributer ID: 173995

##Pull Request ID: 279348

###Profanity Found
**Text**
this is an initial draft that require further refinements but i suggest to have it committed asap so to work on it collaboratively. 
1. by default now all the collection properties are embedded in response, this is for instance the case of the bitstreams list in the itemrest;

2. linked entities listed in the linksrest annotation of the repository are included only if specified in the resource wrapper instantiation and supported for embedding by the link repository (i.e the relation have suitable default or don't depend on additional parameters) - there is a working commented out code in the browseindexresource to show that

this code is based on the pr #1775 and it has been already applied to the rest 7 demo http://dspace7.4science.it/dspace-spring-rest/

you can see how the bitstreams are currently embedded in the items response
http://dspace7.4science.it/dspace-spring-rest/api/core/items
http://dspace7.4science.it/dspace-spring-rest/api/core/items/9f3288b2-f2ad-454f-9f4c-70325646dcee
http://dspace7.4science.it/dspace-spring-rest/api/discover/browses/dateissued/items

##Repo ID: 22104

##Contributer ID: 79682

##Pull Request ID: 246136

###Profanity Found
**Text**
@kshepherd identified that the initial issue reported in the following ticket was that statistics records with a legacyid in owningitem were not being included in the usage reports.

https://jira.duraspace.org/browse/ds-3602

it appears that the legacy id was also not used in queries for scopeid, owningcoll, and owningcomm.

there is an another pr (https://github.com/dspace/dspace/pull/1774) for this ticket to migrate all legacy ids in statistics records.  this pr is recommended in addition to that pr.  this pr can be merged without merging 1774.

this pr will ensure the accessibility of legacy statistics records until that upgrade is performed.

##Repo ID: 22104

##Contributer ID: 85805

##Pull Request ID: 246140

###Profanity Found
**Text**
fix ds-3659 by ensuring that a read-only connection can never rollback.

https://jira.duraspace.org/browse/ds-3659

as noted in the ticket, this bug seems to result from the fact that a database connection may be shared (within the current running thread). a read-only connection should never revert/rollback previous changes that occurred in the same thread.

this bug was found on demo.dspace.org, with significant help from @alexanders and @tomdesair.  so, a huge thanks to both of them for finding the core issue and the correct fix.  it has been validated as working on http://demo.dspace.org (which was previously unable to recreate initial groups after a full content reset).

##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 246173

###Profanity Found
**Text**
https://jira.duraspace.org/browse/ds-3656
https://jira.duraspace.org/browse/ds-3648

this pr is a replacement/update to #1812 and #1813.  so, credit for some of this work goes to @tomdesair and @ssolim, with additional brainstorming/help from @mwoodiupui and @alexanders on slack.

this pr includes the following:
* the fixes from both #1813 and #1812 (slightly updated to be more robust): https://github.com/dspace/dspace/pull/1824/commits/9dd6bb0f08f64aeaea482c2b8a5e969e8c817245
* a refactor of `context.commit()` to ensure database changes are committed prior to `dispatchevents()`: https://github.com/dspace/dspace/pull/1824/commits/646936a3d8d2d39792bd4a5ebb7e2a536d1a8f6e  this partially fixed some of the initial issues with pr #1813 and the 'authority' consumer (see that pr's comments for more).
* ensure `completestep` actually commits the final submission (instead of just calling `dispatchevents`). this was also necessary to fix the issues with pr #1813 and the 'authority' consumer.: https://github.com/dspace/dspace/pull/1824/commits/d4d61eed68ad9a82cd80ed8387de523d050f1e43

~~as part of this, i've noticed we have several other areas of the code that use `context.dispatchevents()` that likely should be using `context.commit()`.  we need to closely analyze whether they should also be fixed.~~  (update: quickly analyzed other `context.dispatchevents()` calls in #1826 and found them to not be as easily replaced.)

##Repo ID: 22104

##Contributer ID: 85035

##Pull Request ID: 246182