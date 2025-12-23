List of Unused and Legacy Data Tables
=====================================

This page tracks tables that are not part of the current collection/analysis
pipelines, and how we plan to handle them. Tables are grouped into three
categories:

1. **Currently in use** (keep as-is if they are used by the current collection/analysis pipelines)
2. **Legacy (keep for historical data, move to a legacy schema if possible)**
3. **Candidates for removal** (drop once confirmed no longer needed)

Currently in use
----------------

- ``message_sentiment`` and ``message_sentiment_summary``  
  Still used by the message insights / sentiment worker.

Legacy (keep for historical data)
---------------------------------
These tables are no longer written by current workers, but may exist on older
instances. Preserve the data and consider moving them to a dedicated legacy
schema so they do not clutter the active schema.

- ``chaoss_metric_status`` — legacy CHAOSS metric metadata (not populated today).
- ``chaoss_user`` — legacy CHAOSS user metadata.
- ``commit_comment_ref`` — historical commit/message linkage data from earlier releases.
- ``libraries`` / ``library_dependencies`` / ``library_version`` — legacy dependency manifests.
- ``lstm_anomaly_models`` / ``lstm_anomaly_results`` — legacy anomaly model outputs.
- ``repo_group_insights`` — legacy insights table.
- ``repo_groups_list_serve`` — legacy listserv group table.
- ``repo_test_coverage`` — legacy coverage table.
- ``dei_badging`` — one-off DEI badging event data (see #3423).

Candidates for removal
----------------------
These tables have no current code paths and no known active consumers. They can
be dropped after confirming they are empty on the target instance (or after
migrating any preserved rows to a legacy schema):

- ``chaoss_metric_status``
- ``chaoss_user``
- ``libraries``, ``library_dependencies``, ``library_version``
- ``lstm_anomaly_models``, ``lstm_anomaly_results``
- ``repo_group_insights``
- ``repo_groups_list_serve``
- ``repo_test_coverage``

Notes
-----
- For safety, export or move tables in the **Legacy** section to a ``legacy``
  schema before dropping from the active schemas.
- If you are running optional analysis workers that rely on sentiment, keep
  ``message_sentiment`` and ``message_sentiment_summary``.
