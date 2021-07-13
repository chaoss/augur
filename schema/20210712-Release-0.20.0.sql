-- #SPDX-License-Identifier: MIT

-- ----------------------------
CREATE SCHEMA augur_data;
CREATE SCHEMA augur_operations;
CREATE SCHEMA spdx;
-- create the schemas
-- -----------------------

-- ----------------------------
-- Sequence structure for augur_data.repo_insights_ri_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."augur_data.repo_insights_ri_id_seq";
CREATE SEQUENCE "augur_data"."augur_data.repo_insights_ri_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."augur_data.repo_insights_ri_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for chaoss_metric_status_cms_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."chaoss_metric_status_cms_id_seq";
CREATE SEQUENCE "augur_data"."chaoss_metric_status_cms_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."chaoss_metric_status_cms_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for commit_comment_ref_cmt_comment_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."commit_comment_ref_cmt_comment_id_seq";
CREATE SEQUENCE "augur_data"."commit_comment_ref_cmt_comment_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."commit_comment_ref_cmt_comment_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for commit_parents_parent_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."commit_parents_parent_id_seq";
CREATE SEQUENCE "augur_data"."commit_parents_parent_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."commit_parents_parent_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for commits_cmt_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."commits_cmt_id_seq";
CREATE SEQUENCE "augur_data"."commits_cmt_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."commits_cmt_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for contributor_affiliations_ca_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."contributor_affiliations_ca_id_seq";
CREATE SEQUENCE "augur_data"."contributor_affiliations_ca_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."contributor_affiliations_ca_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for contributor_repo_cntrb_repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."contributor_repo_cntrb_repo_id_seq";
CREATE SEQUENCE "augur_data"."contributor_repo_cntrb_repo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."contributor_repo_cntrb_repo_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for contributors_aliases_cntrb_a_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."contributors_aliases_cntrb_a_id_seq";
CREATE SEQUENCE "augur_data"."contributors_aliases_cntrb_a_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."contributors_aliases_cntrb_a_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for contributors_cntrb_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."contributors_cntrb_id_seq";
CREATE SEQUENCE "augur_data"."contributors_cntrb_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."contributors_cntrb_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for contributors_history_cntrb_history_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."contributors_history_cntrb_history_id_seq";
CREATE SEQUENCE "augur_data"."contributors_history_cntrb_history_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."contributors_history_cntrb_history_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for discourse_insights_msg_discourse_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."discourse_insights_msg_discourse_id_seq";
CREATE SEQUENCE "augur_data"."discourse_insights_msg_discourse_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."discourse_insights_msg_discourse_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for discourse_insights_msg_discourse_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."discourse_insights_msg_discourse_id_seq1";
CREATE SEQUENCE "augur_data"."discourse_insights_msg_discourse_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."discourse_insights_msg_discourse_id_seq1" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for issue_assignees_issue_assignee_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."issue_assignees_issue_assignee_id_seq";
CREATE SEQUENCE "augur_data"."issue_assignees_issue_assignee_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."issue_assignees_issue_assignee_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for issue_events_event_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."issue_events_event_id_seq";
CREATE SEQUENCE "augur_data"."issue_events_event_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."issue_events_event_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for issue_labels_issue_label_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."issue_labels_issue_label_id_seq";
CREATE SEQUENCE "augur_data"."issue_labels_issue_label_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."issue_labels_issue_label_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for issue_message_ref_issue_msg_ref_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."issue_message_ref_issue_msg_ref_id_seq";
CREATE SEQUENCE "augur_data"."issue_message_ref_issue_msg_ref_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."issue_message_ref_issue_msg_ref_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for issue_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."issue_seq";
CREATE SEQUENCE "augur_data"."issue_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 31000
CACHE 1;
ALTER SEQUENCE "augur_data"."issue_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for libraries_library_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."libraries_library_id_seq";
CREATE SEQUENCE "augur_data"."libraries_library_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."libraries_library_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for library_dependencies_lib_dependency_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."library_dependencies_lib_dependency_id_seq";
CREATE SEQUENCE "augur_data"."library_dependencies_lib_dependency_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."library_dependencies_lib_dependency_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for library_version_library_version_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."library_version_library_version_id_seq";
CREATE SEQUENCE "augur_data"."library_version_library_version_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."library_version_library_version_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for lstm_anomaly_models_model_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."lstm_anomaly_models_model_id_seq";
CREATE SEQUENCE "augur_data"."lstm_anomaly_models_model_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."lstm_anomaly_models_model_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for lstm_anomaly_results_result_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."lstm_anomaly_results_result_id_seq";
CREATE SEQUENCE "augur_data"."lstm_anomaly_results_result_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."lstm_anomaly_results_result_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for message_analysis_msg_analysis_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."message_analysis_msg_analysis_id_seq";
CREATE SEQUENCE "augur_data"."message_analysis_msg_analysis_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."message_analysis_msg_analysis_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for message_analysis_summary_msg_summary_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."message_analysis_summary_msg_summary_id_seq";
CREATE SEQUENCE "augur_data"."message_analysis_summary_msg_summary_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."message_analysis_summary_msg_summary_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for message_msg_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."message_msg_id_seq";
CREATE SEQUENCE "augur_data"."message_msg_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."message_msg_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for message_sentiment_msg_analysis_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."message_sentiment_msg_analysis_id_seq";
CREATE SEQUENCE "augur_data"."message_sentiment_msg_analysis_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."message_sentiment_msg_analysis_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for message_sentiment_summary_msg_summary_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."message_sentiment_summary_msg_summary_id_seq";
CREATE SEQUENCE "augur_data"."message_sentiment_summary_msg_summary_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."message_sentiment_summary_msg_summary_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for platform_pltfrm_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."platform_pltfrm_id_seq";
CREATE SEQUENCE "augur_data"."platform_pltfrm_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."platform_pltfrm_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_analysis_pull_request_analysis_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_analysis_pull_request_analysis_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_analysis_pull_request_analysis_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_analysis_pull_request_analysis_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_assignees_pr_assignee_map_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_assignees_pr_assignee_map_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_assignees_pr_assignee_map_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_assignees_pr_assignee_map_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_commits_pr_cmt_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_commits_pr_cmt_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_commits_pr_cmt_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_commits_pr_cmt_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_events_pr_event_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_events_pr_event_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_events_pr_event_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_events_pr_event_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_files_pr_file_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_files_pr_file_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_files_pr_file_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25150
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_files_pr_file_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_labels_pr_label_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_labels_pr_label_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_labels_pr_label_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_labels_pr_label_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_message_ref_pr_msg_ref_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_message_ref_pr_msg_ref_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_message_ref_pr_msg_ref_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_message_ref_pr_msg_ref_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_meta_pr_repo_meta_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_meta_pr_repo_meta_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_meta_pr_repo_meta_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_meta_pr_repo_meta_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_repo_pr_repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_repo_pr_repo_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_repo_pr_repo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_repo_pr_repo_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_review_message_ref_pr_review_msg_ref_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_review_message_ref_pr_review_msg_ref_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_review_message_ref_pr_review_msg_ref_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_review_message_ref_pr_review_msg_ref_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_reviewers_pr_reviewer_map_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_reviewers_pr_reviewer_map_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_reviewers_pr_reviewer_map_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_reviewers_pr_reviewer_map_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_reviews_pr_review_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_reviews_pr_review_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_reviews_pr_review_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_reviews_pr_review_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_request_teams_pr_team_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_request_teams_pr_team_id_seq";
CREATE SEQUENCE "augur_data"."pull_request_teams_pr_team_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_request_teams_pr_team_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for pull_requests_pull_request_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."pull_requests_pull_request_id_seq";
CREATE SEQUENCE "augur_data"."pull_requests_pull_request_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."pull_requests_pull_request_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for releases_release_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."releases_release_id_seq";
CREATE SEQUENCE "augur_data"."releases_release_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."releases_release_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_badging_badge_collection_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_badging_badge_collection_id_seq";
CREATE SEQUENCE "augur_data"."repo_badging_badge_collection_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25012
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_badging_badge_collection_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_cluster_messages_msg_cluster_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_cluster_messages_msg_cluster_id_seq";
CREATE SEQUENCE "augur_data"."repo_cluster_messages_msg_cluster_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_cluster_messages_msg_cluster_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_dependencies_repo_dependencies_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_dependencies_repo_dependencies_id_seq";
CREATE SEQUENCE "augur_data"."repo_dependencies_repo_dependencies_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_dependencies_repo_dependencies_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_deps_scorecard_repo_deps_scorecard_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq";
CREATE SEQUENCE "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_deps_scorecard_repo_deps_scorecard_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq1";
CREATE SEQUENCE "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_deps_scorecard_repo_deps_scorecard_id_seq1" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_group_insights_rgi_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_group_insights_rgi_id_seq";
CREATE SEQUENCE "augur_data"."repo_group_insights_rgi_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_group_insights_rgi_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_groups_list_serve_rgls_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_groups_list_serve_rgls_id_seq";
CREATE SEQUENCE "augur_data"."repo_groups_list_serve_rgls_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_groups_list_serve_rgls_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_groups_repo_group_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_groups_repo_group_id_seq";
CREATE SEQUENCE "augur_data"."repo_groups_repo_group_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_groups_repo_group_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_info_repo_info_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_info_repo_info_id_seq";
CREATE SEQUENCE "augur_data"."repo_info_repo_info_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_info_repo_info_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_insights_records_ri_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_insights_records_ri_id_seq";
CREATE SEQUENCE "augur_data"."repo_insights_records_ri_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_insights_records_ri_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_insights_ri_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_insights_ri_id_seq";
CREATE SEQUENCE "augur_data"."repo_insights_ri_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_insights_ri_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_labor_repo_labor_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_labor_repo_labor_id_seq";
CREATE SEQUENCE "augur_data"."repo_labor_repo_labor_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_labor_repo_labor_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_meta_rmeta_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_meta_rmeta_id_seq";
CREATE SEQUENCE "augur_data"."repo_meta_rmeta_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_meta_rmeta_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_repo_id_seq";
CREATE SEQUENCE "augur_data"."repo_repo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_repo_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_sbom_scans_rsb_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_sbom_scans_rsb_id_seq";
CREATE SEQUENCE "augur_data"."repo_sbom_scans_rsb_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_sbom_scans_rsb_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_stats_rstat_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_stats_rstat_id_seq";
CREATE SEQUENCE "augur_data"."repo_stats_rstat_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 25430
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_stats_rstat_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_test_coverage_repo_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_test_coverage_repo_id_seq";
CREATE SEQUENCE "augur_data"."repo_test_coverage_repo_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_test_coverage_repo_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for repo_topic_repo_topic_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."repo_topic_repo_topic_id_seq";
CREATE SEQUENCE "augur_data"."repo_topic_repo_topic_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."repo_topic_repo_topic_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for topic_words_topic_words_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."topic_words_topic_words_id_seq";
CREATE SEQUENCE "augur_data"."topic_words_topic_words_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."topic_words_topic_words_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for utility_log_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."utility_log_id_seq";
CREATE SEQUENCE "augur_data"."utility_log_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."utility_log_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for utility_log_id_seq1
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_data"."utility_log_id_seq1";
CREATE SEQUENCE "augur_data"."utility_log_id_seq1" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_data"."utility_log_id_seq1" OWNER TO "augur";



-- ----------------------------
-- Sequence structure for augur_settings_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_operations"."augur_settings_id_seq";
CREATE SEQUENCE "augur_operations"."augur_settings_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_operations"."augur_settings_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for gh_worker_history_history_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_operations"."gh_worker_history_history_id_seq";
CREATE SEQUENCE "augur_operations"."gh_worker_history_history_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;
ALTER SEQUENCE "augur_operations"."gh_worker_history_history_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for worker_oauth_oauth_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "augur_operations"."worker_oauth_oauth_id_seq";
CREATE SEQUENCE "augur_operations"."worker_oauth_oauth_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1000
CACHE 1;
ALTER SEQUENCE "augur_operations"."worker_oauth_oauth_id_seq" OWNER TO "augur";


-- ----------------------------
-- Sequence structure for annotation_types_annotation_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."annotation_types_annotation_type_id_seq";
CREATE SEQUENCE "spdx"."annotation_types_annotation_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."annotation_types_annotation_type_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for annotations_annotation_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."annotations_annotation_id_seq";
CREATE SEQUENCE "spdx"."annotations_annotation_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."annotations_annotation_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for augur_repo_map_map_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."augur_repo_map_map_id_seq";
CREATE SEQUENCE "spdx"."augur_repo_map_map_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."augur_repo_map_map_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for creator_types_creator_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."creator_types_creator_type_id_seq";
CREATE SEQUENCE "spdx"."creator_types_creator_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."creator_types_creator_type_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for creators_creator_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."creators_creator_id_seq";
CREATE SEQUENCE "spdx"."creators_creator_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."creators_creator_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for document_namespaces_document_namespace_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."document_namespaces_document_namespace_id_seq";
CREATE SEQUENCE "spdx"."document_namespaces_document_namespace_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."document_namespaces_document_namespace_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for documents_creators_document_creator_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."documents_creators_document_creator_id_seq";
CREATE SEQUENCE "spdx"."documents_creators_document_creator_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."documents_creators_document_creator_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for documents_document_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."documents_document_id_seq";
CREATE SEQUENCE "spdx"."documents_document_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."documents_document_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for external_refs_external_ref_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."external_refs_external_ref_id_seq";
CREATE SEQUENCE "spdx"."external_refs_external_ref_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."external_refs_external_ref_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for file_contributors_file_contributor_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."file_contributors_file_contributor_id_seq";
CREATE SEQUENCE "spdx"."file_contributors_file_contributor_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."file_contributors_file_contributor_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for file_types_file_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."file_types_file_type_id_seq";
CREATE SEQUENCE "spdx"."file_types_file_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."file_types_file_type_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for files_file_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."files_file_id_seq";
CREATE SEQUENCE "spdx"."files_file_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."files_file_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for files_licenses_file_license_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."files_licenses_file_license_id_seq";
CREATE SEQUENCE "spdx"."files_licenses_file_license_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."files_licenses_file_license_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for files_scans_file_scan_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."files_scans_file_scan_id_seq";
CREATE SEQUENCE "spdx"."files_scans_file_scan_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."files_scans_file_scan_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for identifiers_identifier_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."identifiers_identifier_id_seq";
CREATE SEQUENCE "spdx"."identifiers_identifier_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."identifiers_identifier_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for licenses_license_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."licenses_license_id_seq";
CREATE SEQUENCE "spdx"."licenses_license_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."licenses_license_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for packages_files_package_file_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."packages_files_package_file_id_seq";
CREATE SEQUENCE "spdx"."packages_files_package_file_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."packages_files_package_file_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for packages_package_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."packages_package_id_seq";
CREATE SEQUENCE "spdx"."packages_package_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."packages_package_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for packages_scans_package_scan_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."packages_scans_package_scan_id_seq";
CREATE SEQUENCE "spdx"."packages_scans_package_scan_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."packages_scans_package_scan_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for projects_package_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."projects_package_id_seq";
CREATE SEQUENCE "spdx"."projects_package_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."projects_package_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for relationship_types_relationship_type_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."relationship_types_relationship_type_id_seq";
CREATE SEQUENCE "spdx"."relationship_types_relationship_type_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."relationship_types_relationship_type_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for relationships_relationship_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."relationships_relationship_id_seq";
CREATE SEQUENCE "spdx"."relationships_relationship_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."relationships_relationship_id_seq" OWNER TO "augur";

-- ----------------------------
-- Sequence structure for scanners_scanner_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "spdx"."scanners_scanner_id_seq";
CREATE SEQUENCE "spdx"."scanners_scanner_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 2147483647
START 1
CACHE 1;
ALTER SEQUENCE "spdx"."scanners_scanner_id_seq" OWNER TO "augur";





CREATE TABLE "augur_data"."analysis_log" (
  "repos_id" int4 NOT NULL,
  "status" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "date_attempted" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."analysis_log" OWNER TO "augur";
CREATE INDEX "repos_id" ON "augur_data"."analysis_log" USING btree (
  "repos_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."chaoss_metric_status" (
  "cms_id" int8 NOT NULL DEFAULT nextval('"augur_data".chaoss_metric_status_cms_id_seq'::regclass),
  "cm_group" varchar COLLATE "pg_catalog"."default",
  "cm_source" varchar COLLATE "pg_catalog"."default",
  "cm_type" varchar COLLATE "pg_catalog"."default",
  "cm_backend_status" varchar COLLATE "pg_catalog"."default",
  "cm_frontend_status" varchar COLLATE "pg_catalog"."default",
  "cm_defined" bool,
  "cm_api_endpoint_repo" varchar COLLATE "pg_catalog"."default",
  "cm_api_endpoint_rg" varchar COLLATE "pg_catalog"."default",
  "cm_name" varchar COLLATE "pg_catalog"."default",
  "cm_working_group" varchar COLLATE "pg_catalog"."default",
  "cm_info" json,
  "cm_working_group_focus_area" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "chaoss_metric_status_pkey" PRIMARY KEY ("cms_id")
);
ALTER TABLE "augur_data"."chaoss_metric_status" OWNER TO "augur";
COMMENT ON TABLE "augur_data"."chaoss_metric_status" IS 'This table used to track CHAOSS Metric implementations in Augur, but due to the constantly changing location of that information, it is for the moment not actively populated. ';

CREATE TABLE "augur_data"."commit_comment_ref" (
  "cmt_comment_id" int8 NOT NULL DEFAULT nextval('"augur_data".commit_comment_ref_cmt_comment_id_seq'::regclass),
  "cmt_id" int8 NOT NULL,
  "msg_id" int8 NOT NULL,
  "user_id" int8 NOT NULL,
  "body" text COLLATE "pg_catalog"."default",
  "line" int8,
  "position" int8,
  "created_at" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "commit_comment_src_node_id" varchar COLLATE "pg_catalog"."default",
  "cmt_comment_src_id" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "commit_comment_ref_pkey" PRIMARY KEY ("cmt_comment_id"),
  CONSTRAINT "commitcomment" UNIQUE ("cmt_id", "msg_id", "cmt_comment_id")
);
ALTER TABLE "augur_data"."commit_comment_ref" OWNER TO "augur";
CREATE INDEX "comment_id" ON "augur_data"."commit_comment_ref" USING btree (
  "cmt_comment_src_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_comment_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "msg_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."commit_comment_ref"."commit_comment_src_node_id" IS 'For data provenance, we store the source node ID if it exists. ';
COMMENT ON COLUMN "augur_data"."commit_comment_ref"."cmt_comment_src_id" IS 'For data provenance, we store the source ID if it exists. ';

CREATE TABLE "augur_data"."commit_parents" (
  "cmt_id" int8 NOT NULL,
  "parent_id" int8 NOT NULL DEFAULT nextval('"augur_data".commit_parents_parent_id_seq'::regclass),
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "commit_parents_pkey" PRIMARY KEY ("cmt_id", "parent_id")
);
ALTER TABLE "augur_data"."commit_parents" OWNER TO "augur";
CREATE INDEX "commit_parents_ibfk_1" ON "augur_data"."commit_parents" USING btree (
  "cmt_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "commit_parents_ibfk_2" ON "augur_data"."commit_parents" USING btree (
  "parent_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."commits" (
  "cmt_id" int8 NOT NULL DEFAULT nextval('"augur_data".commits_cmt_id_seq'::regclass),
  "repo_id" int8 NOT NULL,
  "cmt_commit_hash" varchar(80) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_author_name" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_author_raw_email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_author_email" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_author_date" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_author_affiliation" varchar COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "cmt_committer_name" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_committer_raw_email" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_committer_email" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_committer_date" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_committer_affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "cmt_added" int4 NOT NULL,
  "cmt_removed" int4 NOT NULL,
  "cmt_whitespace" int4 NOT NULL,
  "cmt_filename" varchar(4096) COLLATE "pg_catalog"."default" NOT NULL,
  "cmt_date_attempted" timestamp(0) NOT NULL,
  "cmt_ght_author_id" int4,
  "cmt_ght_committer_id" int4,
  "cmt_ght_committed_at" timestamp(0),
  "cmt_author_timestamp" timestamptz(0),
  "cmt_committer_timestamp" timestamptz(0),
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "commits_pkey" PRIMARY KEY ("cmt_id")
);
ALTER TABLE "augur_data"."commits" OWNER TO "augur";
CREATE INDEX "author_affiliation" ON "augur_data"."commits" USING hash (
  "cmt_author_affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops"
);
CREATE INDEX "author_cntrb_id" ON "augur_data"."commits" USING btree (
  "cmt_ght_author_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "author_email,author_affiliation,author_date" ON "augur_data"."commits" USING btree (
  "cmt_author_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "author_raw_email" ON "augur_data"."commits" USING btree (
  "cmt_author_raw_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cmt-author-date-idx2" ON "augur_data"."commits" USING btree (
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cmt-committer-date-idx3" ON "augur_data"."commits" USING btree (
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cmt_author-name-idx5" ON "augur_data"."commits" USING btree (
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cmt_author_contrib_worker" ON "augur_data"."commits" USING brin (
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cmt_author_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "cmt_cmmter-name-idx4" ON "augur_data"."commits" USING btree (
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cmt_commiter_contrib_worker" ON "augur_data"."commits" USING brin (
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cmt_committer_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "commited" ON "augur_data"."commits" USING btree (
  "cmt_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_cmt_email_cmt_date_cmt_name" ON "augur_data"."commits" USING btree (
  "cmt_author_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_cmt_email_cmt_date_cmt_name2" ON "augur_data"."commits" USING btree (
  "cmt_committer_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_cmt_name_cmt_date2" ON "augur_data"."commits" USING btree (
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_cmt_name_cmt_date_cmt_date3" ON "augur_data"."commits" USING btree (
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_repo_id_cmt_ema_cmt_dat_cmt_nam" ON "augur_data"."commits" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_author_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_repo_id_cmt_ema_cmt_dat_cmt_nam2" ON "augur_data"."commits" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_committer_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_repo_id_cmt_ema_cmt_nam_cmt_dat2" ON "augur_data"."commits" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_author_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "commits_idx_repo_id_cmt_ema_cmt_nam_cmt_dat3" ON "augur_data"."commits" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_committer_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_author_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "committer_affiliation" ON "augur_data"."commits" USING btree (
  "cmt_committer_affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "committer_cntrb_id" ON "augur_data"."commits" USING btree (
  "cmt_ght_committer_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);
CREATE INDEX "committer_email,committer_affiliation,committer_date" ON "augur_data"."commits" USING btree (
  "cmt_committer_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cmt_committer_date" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "committer_raw_email" ON "augur_data"."commits" USING btree (
  "cmt_committer_raw_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,commit" ON "augur_data"."commits" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "cmt_commit_hash" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
COMMENT ON TABLE "augur_data"."commits" IS 'Starts with augur.analysis_data table and incorporates GHTorrent commit table attributes if different. 
Cmt_id is from get
The author and committer ID’s are at the bottom of the table and not required for now because we want to focus on the facade schema’s properties over the ghtorrent properties when they are in conflict. ';

CREATE TABLE "augur_data"."contributor_affiliations" (
  "ca_id" int8 NOT NULL DEFAULT nextval('"augur_data".contributor_affiliations_ca_id_seq'::regclass),
  "ca_domain" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "ca_start_date" date DEFAULT '1970-01-01'::date,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  "ca_last_used" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "ca_affiliation" varchar COLLATE "pg_catalog"."default",
  "ca_active" int2 DEFAULT 1,
  CONSTRAINT "contributor_affiliations_pkey" PRIMARY KEY ("ca_id"),
  CONSTRAINT "unique_domain" UNIQUE ("ca_domain")
);
ALTER TABLE "augur_data"."contributor_affiliations" OWNER TO "augur";
COMMENT ON CONSTRAINT "unique_domain" ON "augur_data"."contributor_affiliations" IS 'Only one row should exist for any given top level domain or subdomain. ';

CREATE TABLE "augur_data"."contributor_repo" (
  "cntrb_repo_id" int8 NOT NULL DEFAULT nextval('"augur_data".contributor_repo_cntrb_repo_id_seq'::regclass),
  "cntrb_id" int8 NOT NULL,
  "repo_git" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "cntrb_category" varchar(255) COLLATE "pg_catalog"."default",
  "event_id" int8,
  "gh_repo_id" int8 NOT NULL,
  "repo_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "created_at" timestamp(0),
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "cntrb_repo_id_key" PRIMARY KEY ("cntrb_repo_id"),
  CONSTRAINT "eventer" UNIQUE ("event_id", "tool_version")
);
ALTER TABLE "augur_data"."contributor_repo" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."contributor_repo"."cntrb_id" IS 'This is not null because what is the point without the contributor in this table? ';
COMMENT ON COLUMN "augur_data"."contributor_repo"."repo_git" IS 'Similar to cntrb_id, we need this data for the table to have meaningful data. ';
COMMENT ON TABLE "augur_data"."contributor_repo" IS 'Developed in Partnership with Andrew Brain. 
From: [
  {
    "login": "octocat",
    "id": 1,
    "node_id": "MDQ6VXNlcjE=",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "gravatar_id": "",
    "url": "https://api.github.com/users/octocat",
    "html_url": "https://github.com/octocat",
    "followers_url": "https://api.github.com/users/octocat/followers",
    "following_url": "https://api.github.com/users/octocat/following{/other_user}",
    "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
    "organizations_url": "https://api.github.com/users/octocat/orgs",
    "repos_url": "https://api.github.com/users/octocat/repos",
    "events_url": "https://api.github.com/users/octocat/events{/privacy}",
    "received_events_url": "https://api.github.com/users/octocat/received_events",
    "type": "User",
    "site_admin": false
  }
]
';

CREATE TABLE "augur_data"."contributors" (
  "cntrb_id" int8 NOT NULL DEFAULT nextval('"augur_data".contributors_cntrb_id_seq'::regclass),
  "cntrb_login" varchar(255) COLLATE "pg_catalog"."default",
  "cntrb_email" varchar COLLATE "pg_catalog"."default",
  "cntrb_company" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_created_at" timestamp(0),
  "cntrb_type" varchar(255) COLLATE "pg_catalog"."default",
  "cntrb_fake" int2 DEFAULT 0,
  "cntrb_deleted" int2 DEFAULT 0,
  "cntrb_long" numeric(11,8) DEFAULT NULL::numeric,
  "cntrb_lat" numeric(10,8) DEFAULT NULL::numeric,
  "cntrb_country_code" char(3) COLLATE "pg_catalog"."default" DEFAULT NULL::bpchar,
  "cntrb_state" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_city" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_location" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_canonical" varchar COLLATE "pg_catalog"."default",
  "gh_user_id" int8,
  "gh_login" varchar(255) COLLATE "pg_catalog"."default",
  "gh_url" varchar(255) COLLATE "pg_catalog"."default",
  "gh_html_url" varchar(255) COLLATE "pg_catalog"."default",
  "gh_node_id" varchar(255) COLLATE "pg_catalog"."default",
  "gh_avatar_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_gravatar_id" varchar(255) COLLATE "pg_catalog"."default",
  "gh_followers_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_following_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_gists_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_starred_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_subscriptions_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_organizations_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_repos_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_events_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_received_events_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_type" varchar(255) COLLATE "pg_catalog"."default",
  "gh_site_admin" varchar(255) COLLATE "pg_catalog"."default",
  "cntrb_full_name" varchar COLLATE "pg_catalog"."default",
  "cntrb_last_used" timestamptz(0) DEFAULT NULL::timestamp with time zone,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "contributors_pkey" PRIMARY KEY ("cntrb_id")
);
ALTER TABLE "augur_data"."contributors" OWNER TO "augur";
CREATE INDEX "cnt-fullname" ON "augur_data"."contributors" USING hash (
  "cntrb_full_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops"
);
CREATE INDEX "cntrb-theemail" ON "augur_data"."contributors" USING hash (
  "cntrb_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops"
);
CREATE INDEX "cntrb_canonica-idx11" ON "augur_data"."contributors" USING btree (
  "cntrb_canonical" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "cntrb_login_platform_index" ON "augur_data"."contributors" USING btree (
  "cntrb_login" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "contributor_delete_finder" ON "augur_data"."contributors" USING brin (
  "cntrb_id" "pg_catalog"."int8_minmax_ops",
  "cntrb_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "contributor_worker_email_finder" ON "augur_data"."contributors" USING brin (
  "cntrb_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "contributor_worker_finder" ON "augur_data"."contributors" USING brin (
  "cntrb_login" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cntrb_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops",
  "cntrb_id" "pg_catalog"."int8_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "contributor_worker_fullname_finder" ON "augur_data"."contributors" USING brin (
  "cntrb_full_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_minmax_ops"
) WITH (PAGES_PER_RANGE = 64);
CREATE INDEX "contributors_idx_cntrb_email3" ON "augur_data"."contributors" USING btree (
  "cntrb_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "login" ON "augur_data"."contributors" USING btree (
  "cntrb_login" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "login-contributor-idx" ON "augur_data"."contributors" USING btree (
  "cntrb_login" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."contributors"."cntrb_login" IS 'Will be a double population with the same value as gh_login for github, but the local value for other systems. ';
COMMENT ON COLUMN "augur_data"."contributors"."cntrb_email" IS 'This needs to be here for matching contributor ids, which are augur, to the commit information. ';
COMMENT ON COLUMN "augur_data"."contributors"."cntrb_type" IS 'Present in another models. It is not currently used in Augur. ';
COMMENT ON COLUMN "augur_data"."contributors"."gh_login" IS 'populated with the github user name for github originated data. ';
COMMENT ON TABLE "augur_data"."contributors" IS 'For GitHub, this should be repeated from gh_login. for other systems, it should be that systems login. ';

CREATE TABLE "augur_data"."contributors_aliases" (
  "cntrb_id" int8 NOT NULL,
  "cntrb_a_id" int8 NOT NULL DEFAULT nextval('"augur_data".contributors_aliases_cntrb_a_id_seq'::regclass),
  "canonical_email" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "alias_email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "cntrb_active" int2 NOT NULL DEFAULT 1,
  "cntrb_last_modified" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "contributors_aliases_pkey" PRIMARY KEY ("cntrb_id", "cntrb_a_id")
);
ALTER TABLE "augur_data"."contributors_aliases" OWNER TO "augur";
CREATE INDEX "alias,active" ON "augur_data"."contributors_aliases" USING btree (
  "alias_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "cntrb_active" "pg_catalog"."int2_ops" ASC NULLS LAST
);
CREATE UNIQUE INDEX "canonical,alias" ON "augur_data"."contributors_aliases" USING btree (
  "canonical_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "alias_email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "issue-alias-cntrb-idx1" ON "augur_data"."contributors_aliases" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issue-alias-cntrb-idx2" ON "augur_data"."contributors_aliases" USING btree (
  "cntrb_a_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON TABLE "augur_data"."contributors_aliases" IS 'An alias will need to be created for every contributor in this model, otherwise we will have to look in 2 places. ';

CREATE TABLE "augur_data"."contributors_history" (
  "cntrb_history_id" int8 NOT NULL DEFAULT nextval('"augur_data".contributors_history_cntrb_history_id_seq'::regclass),
  "cntrb_id" int8 NOT NULL,
  "cntrb_history_timestamp" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "cntrb_history_current_bool" bool,
  "cntrb_organizations_list" json,
  "cntrb_gists_count" int8,
  "cntrb_starred_count" int8,
  "cntrb_following_count" int8,
  "cntrb_follower_count" int8,
  "cntrb_login" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "cntrb_email" varchar(255) COLLATE "pg_catalog"."default",
  "cntrb_company" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_created_at" timestamp(0) NOT NULL,
  "cntrb_type" varchar(255) COLLATE "pg_catalog"."default",
  "cntrb_fake" int2 NOT NULL DEFAULT 0,
  "cntrb_deleted" int2 NOT NULL DEFAULT 0,
  "cntrb_long" numeric(11,8) DEFAULT NULL::numeric,
  "cntrb_lat" numeric(10,8) DEFAULT NULL::numeric,
  "cntrb_country_code" char(3) COLLATE "pg_catalog"."default" DEFAULT NULL::bpchar,
  "cntrb_state" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_city" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_location" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "cntrb_canonical" varchar(128) COLLATE "pg_catalog"."default",
  "gh_user_id" int8,
  "gh_login" varchar(255) COLLATE "pg_catalog"."default",
  "gh_url" varchar(255) COLLATE "pg_catalog"."default",
  "gh_html_url" varchar(255) COLLATE "pg_catalog"."default",
  "gh_node_id" varchar(255) COLLATE "pg_catalog"."default",
  "gh_avatar_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_gravatar_id" varchar(255) COLLATE "pg_catalog"."default",
  "gh_followers_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_following_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_gists_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_starred_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_subscriptions_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_organizations_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_repos_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_events_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_received_events_url" varchar(4000) COLLATE "pg_catalog"."default",
  "gh_type" varchar(255) COLLATE "pg_catalog"."default",
  "gh_site_admin" varchar(255) COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "contributors_history_pkey" PRIMARY KEY ("cntrb_history_id")
);
ALTER TABLE "augur_data"."contributors_history" OWNER TO "augur";
CREATE INDEX "contrb-history-dix1" ON "augur_data"."contributors_history" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "login_index_2" ON "augur_data"."contributors_history" USING btree (
  "cntrb_login" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."contributors_history"."cntrb_history_current_bool" IS 'At some point it would be great to have a boolean updated by a contributor worker that set the most recent contributor data to true. ';
COMMENT ON COLUMN "augur_data"."contributors_history"."cntrb_login" IS 'Will be a double population with the same value as gh_login for github, but the local value for other systems. ';
COMMENT ON COLUMN "augur_data"."contributors_history"."cntrb_email" IS 'This needs to be here for matching contributor ids, which are augur, to the commit information. ';
COMMENT ON COLUMN "augur_data"."contributors_history"."cntrb_type" IS 'Present in another models. It is not currently used in Augur. ';
COMMENT ON COLUMN "augur_data"."contributors_history"."gh_login" IS 'populated with the github user name for github originated data. ';
COMMENT ON TABLE "augur_data"."contributors_history" IS 'For GitHub, this should be repeated from gh_login. for other systems, it should be that systems login. 

At this time the table is not populated. ';

CREATE TABLE "augur_data"."discourse_insights" (
  "msg_discourse_id" int8 NOT NULL DEFAULT nextval('"augur_data".discourse_insights_msg_discourse_id_seq1'::regclass),
  "msg_id" int8,
  "discourse_act" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamptz(6) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "discourse_insights_pkey" PRIMARY KEY ("msg_discourse_id")
);
ALTER TABLE "augur_data"."discourse_insights" OWNER TO "augur";

CREATE TABLE "augur_data"."dm_repo_annual" (
  "repo_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_annual" OWNER TO "augur";
CREATE INDEX "repo_id,affiliation_copy_1" ON "augur_data"."dm_repo_annual" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,email_copy_1" ON "augur_data"."dm_repo_annual" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."dm_repo_group_annual" (
  "repo_group_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_group_annual" OWNER TO "augur";
CREATE INDEX "projects_id,affiliation_copy_1" ON "augur_data"."dm_repo_group_annual" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,email_copy_1" ON "augur_data"."dm_repo_group_annual" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."dm_repo_group_monthly" (
  "repo_group_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "month" int2 NOT NULL,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_group_monthly" OWNER TO "augur";
CREATE INDEX "projects_id,affiliation_copy_2" ON "augur_data"."dm_repo_group_monthly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,email_copy_2" ON "augur_data"."dm_repo_group_monthly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,year,affiliation_copy_1" ON "augur_data"."dm_repo_group_monthly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,year,email_copy_1" ON "augur_data"."dm_repo_group_monthly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."dm_repo_group_weekly" (
  "repo_group_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "week" int2 NOT NULL,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_group_weekly" OWNER TO "augur";
CREATE INDEX "projects_id,affiliation" ON "augur_data"."dm_repo_group_weekly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,email" ON "augur_data"."dm_repo_group_weekly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,year,affiliation" ON "augur_data"."dm_repo_group_weekly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "projects_id,year,email" ON "augur_data"."dm_repo_group_weekly" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."dm_repo_monthly" (
  "repo_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "month" int2 NOT NULL,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_monthly" OWNER TO "augur";
CREATE INDEX "repo_id,affiliation_copy_2" ON "augur_data"."dm_repo_monthly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,email_copy_2" ON "augur_data"."dm_repo_monthly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,year,affiliation_copy_1" ON "augur_data"."dm_repo_monthly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,year,email_copy_1" ON "augur_data"."dm_repo_monthly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."dm_repo_weekly" (
  "repo_id" int8 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "affiliation" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "week" int2 NOT NULL,
  "year" int2 NOT NULL,
  "added" int8 NOT NULL,
  "removed" int8 NOT NULL,
  "whitespace" int8 NOT NULL,
  "files" int8 NOT NULL,
  "patches" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."dm_repo_weekly" OWNER TO "augur";
CREATE INDEX "repo_id,affiliation" ON "augur_data"."dm_repo_weekly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,email" ON "augur_data"."dm_repo_weekly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,year,affiliation" ON "augur_data"."dm_repo_weekly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "affiliation" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_id,year,email" ON "augur_data"."dm_repo_weekly" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "year" "pg_catalog"."int2_ops" ASC NULLS LAST,
  "email" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."exclude" (
  "id" int4 NOT NULL,
  "projects_id" int4 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "domain" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  CONSTRAINT "exclude_pkey" PRIMARY KEY ("id")
);
ALTER TABLE "augur_data"."exclude" OWNER TO "augur";

CREATE TABLE "augur_data"."issue_assignees" (
  "issue_assignee_id" int8 NOT NULL DEFAULT nextval('"augur_data".issue_assignees_issue_assignee_id_seq'::regclass),
  "issue_id" int8,
  "cntrb_id" int8,
  "issue_assignee_src_id" int8,
  "issue_assignee_src_node" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "issue_assignees_pkey" PRIMARY KEY ("issue_assignee_id")
);
ALTER TABLE "augur_data"."issue_assignees" OWNER TO "augur";
CREATE INDEX "issue-cntrb-assign-idx-1" ON "augur_data"."issue_assignees" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."issue_assignees"."issue_assignee_src_id" IS 'This ID comes from the source. In the case of GitHub, it is the id that is the first field returned from the issue events API in the issue_assignees embedded JSON object. We may discover it is an ID for the person themselves; but my hypothesis is that its not.';
COMMENT ON COLUMN "augur_data"."issue_assignees"."issue_assignee_src_node" IS 'This character based identifier comes from the source. In the case of GitHub, it is the id that is the second field returned from the issue events API in the issue_assignees embedded JSON object. We may discover it is an ID for the person themselves; but my hypothesis is that its not.';

CREATE TABLE "augur_data"."issue_events" (
  "event_id" int8 NOT NULL DEFAULT nextval('"augur_data".issue_events_event_id_seq'::regclass),
  "issue_id" int8 NOT NULL,
  "cntrb_id" int8 NOT NULL,
  "action" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "action_commit_hash" varchar COLLATE "pg_catalog"."default",
  "created_at" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "node_id" varchar COLLATE "pg_catalog"."default",
  "node_url" varchar COLLATE "pg_catalog"."default",
  "issue_event_src_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "issue_events_pkey" PRIMARY KEY ("event_id")
);
ALTER TABLE "augur_data"."issue_events" OWNER TO "augur";
CREATE INDEX "issue-cntrb-idx2" ON "augur_data"."issue_events" USING btree (
  "issue_event_src_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issue_events_ibfk_1" ON "augur_data"."issue_events" USING btree (
  "issue_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issue_events_ibfk_2" ON "augur_data"."issue_events" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."issue_events"."node_id" IS 'This should be renamed to issue_event_src_node_id, as its the varchar identifier in GitHub and likely common in other sources as well. However, since it was created before we came to this naming standard and workers are built around it, we have it simply named as node_id. Anywhere you see node_id in the schema, it comes from GitHubs terminology.';
COMMENT ON COLUMN "augur_data"."issue_events"."issue_event_src_id" IS 'This ID comes from the source. In the case of GitHub, it is the id that is the first field returned from the issue events API';

CREATE TABLE "augur_data"."issue_labels" (
  "issue_label_id" int8 NOT NULL DEFAULT nextval('"augur_data".issue_labels_issue_label_id_seq'::regclass),
  "issue_id" int8,
  "label_text" varchar COLLATE "pg_catalog"."default",
  "label_description" varchar COLLATE "pg_catalog"."default",
  "label_color" varchar COLLATE "pg_catalog"."default",
  "label_src_id" int8,
  "label_src_node_id" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "issue_labels_pkey" PRIMARY KEY ("issue_label_id")
);
ALTER TABLE "augur_data"."issue_labels" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."issue_labels"."label_src_id" IS 'This character based identifier (node) comes from the source. In the case of GitHub, it is the id that is the second field returned from the issue events API JSON subsection for issues.';

CREATE TABLE "augur_data"."issue_message_ref" (
  "issue_msg_ref_id" int8 NOT NULL DEFAULT nextval('"augur_data".issue_message_ref_issue_msg_ref_id_seq'::regclass),
  "issue_id" int8,
  "msg_id" int8,
  "issue_msg_ref_src_comment_id" int8,
  "issue_msg_ref_src_node_id" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "issue_message_ref_pkey" PRIMARY KEY ("issue_msg_ref_id")
);
ALTER TABLE "augur_data"."issue_message_ref" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."issue_message_ref"."issue_msg_ref_src_comment_id" IS 'This ID comes from the source. In the case of GitHub, it is the id that is the first field returned from the issue comments API';
COMMENT ON COLUMN "augur_data"."issue_message_ref"."issue_msg_ref_src_node_id" IS 'This character based identifier comes from the source. In the case of GitHub, it is the id that is the first field returned from the issue comments API';

CREATE TABLE "augur_data"."issues" (
  "issue_id" int8 NOT NULL DEFAULT nextval('"augur_data".issue_seq'::regclass),
  "repo_id" int8,
  "reporter_id" int8,
  "pull_request" int8,
  "pull_request_id" int8,
  "created_at" timestamp(0),
  "issue_title" varchar(500) COLLATE "pg_catalog"."default",
  "issue_body" text COLLATE "pg_catalog"."default",
  "cntrb_id" int8,
  "comment_count" int8,
  "updated_at" timestamp(0),
  "closed_at" timestamp(0),
  "due_on" timestamp(0),
  "repository_url" varchar(4000) COLLATE "pg_catalog"."default",
  "issue_url" varchar(4000) COLLATE "pg_catalog"."default",
  "labels_url" varchar(4000) COLLATE "pg_catalog"."default",
  "comments_url" varchar(4000) COLLATE "pg_catalog"."default",
  "events_url" varchar(4000) COLLATE "pg_catalog"."default",
  "html_url" varchar(4000) COLLATE "pg_catalog"."default",
  "issue_state" varchar(255) COLLATE "pg_catalog"."default",
  "issue_node_id" varchar COLLATE "pg_catalog"."default",
  "gh_issue_id" int8,
  "gh_user_id" int8,
  "gh_issue_number" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "issues_pkey" PRIMARY KEY ("issue_id")
);
ALTER TABLE "augur_data"."issues" OWNER TO "augur";
CREATE INDEX "issue-cntrb-dix2" ON "augur_data"."issues" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issues_ibfk_1" ON "augur_data"."issues" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issues_ibfk_2" ON "augur_data"."issues" USING btree (
  "reporter_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "issues_ibfk_4" ON "augur_data"."issues" USING btree (
  "pull_request_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."issues"."reporter_id" IS 'The ID of the person who opened the issue. ';
COMMENT ON COLUMN "augur_data"."issues"."cntrb_id" IS 'The ID of the person who closed the issue. ';

CREATE TABLE "augur_data"."libraries" (
  "library_id" int8 NOT NULL DEFAULT nextval('"augur_data".libraries_library_id_seq'::regclass),
  "repo_id" int8,
  "platform" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "created_timestamp" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "updated_timestamp" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "library_description" varchar(2000) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "keywords" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "library_homepage" varchar(1000) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "license" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "version_count" int4,
  "latest_release_timestamp" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "latest_release_number" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "package_manager_id" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "dependency_count" int4,
  "dependent_library_count" int4,
  "primary_language" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "libraries_pkey" PRIMARY KEY ("library_id")
);
ALTER TABLE "augur_data"."libraries" OWNER TO "augur";

CREATE TABLE "augur_data"."library_dependencies" (
  "lib_dependency_id" int8 NOT NULL DEFAULT nextval('"augur_data".library_dependencies_lib_dependency_id_seq'::regclass),
  "library_id" int8,
  "manifest_platform" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "manifest_filepath" varchar(1000) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "manifest_kind" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "repo_id_branch" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "library_dependencies_pkey" PRIMARY KEY ("lib_dependency_id")
);
ALTER TABLE "augur_data"."library_dependencies" OWNER TO "augur";
CREATE INDEX "REPO_DEP" ON "augur_data"."library_dependencies" USING btree (
  "library_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."library_version" (
  "library_version_id" int8 NOT NULL DEFAULT nextval('"augur_data".library_version_library_version_id_seq'::regclass),
  "library_id" int8,
  "library_platform" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "version_number" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "version_release_date" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "library_version_pkey" PRIMARY KEY ("library_version_id")
);
ALTER TABLE "augur_data"."library_version" OWNER TO "augur";

CREATE TABLE "augur_data"."lstm_anomaly_models" (
  "model_id" int8 NOT NULL DEFAULT nextval('"augur_data".lstm_anomaly_models_model_id_seq'::regclass),
  "model_name" varchar COLLATE "pg_catalog"."default",
  "model_description" varchar COLLATE "pg_catalog"."default",
  "look_back_days" int8,
  "training_days" int8,
  "batch_size" int8,
  "metric" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "lstm_anomaly_models_pkey" PRIMARY KEY ("model_id")
);
ALTER TABLE "augur_data"."lstm_anomaly_models" OWNER TO "augur";

CREATE TABLE "augur_data"."lstm_anomaly_results" (
  "result_id" int8 NOT NULL DEFAULT nextval('"augur_data".lstm_anomaly_results_result_id_seq'::regclass),
  "repo_id" int8,
  "repo_category" varchar COLLATE "pg_catalog"."default",
  "model_id" int8,
  "metric" varchar COLLATE "pg_catalog"."default",
  "contamination_factor" float8,
  "mean_absolute_error" float8,
  "remarks" varchar COLLATE "pg_catalog"."default",
  "metric_field" varchar COLLATE "pg_catalog"."default",
  "mean_absolute_actual_value" float8,
  "mean_absolute_prediction_value" float8,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "lstm_anomaly_results_pkey" PRIMARY KEY ("result_id")
);
ALTER TABLE "augur_data"."lstm_anomaly_results" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."lstm_anomaly_results"."metric_field" IS 'This is a listing of all of the endpoint fields included in the generation of the metric. Sometimes there is one, sometimes there is more than one. This will list them all. ';

CREATE TABLE "augur_data"."message" (
  "msg_id" int8 NOT NULL DEFAULT nextval('"augur_data".message_msg_id_seq'::regclass),
  "rgls_id" int8,
  "msg_text" text COLLATE "pg_catalog"."default",
  "msg_timestamp" timestamp(0),
  "msg_sender_email" varchar(255) COLLATE "pg_catalog"."default",
  "msg_header" varchar(4000) COLLATE "pg_catalog"."default",
  "pltfrm_id" int8 NOT NULL,
  "cntrb_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "message_pkey" PRIMARY KEY ("msg_id"),
  CONSTRAINT "REPOGROUPLISTER" UNIQUE ("msg_id", "rgls_id"),
  CONSTRAINT "platformer" UNIQUE ("msg_id", "pltfrm_id")
);
ALTER TABLE "augur_data"."message" OWNER TO "augur";
CREATE UNIQUE INDEX "messagegrouper" ON "augur_data"."message" USING btree (
  "msg_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "rgls_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "msg-cntrb-id-idx" ON "augur_data"."message" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "platformgrouper" ON "augur_data"."message" USING btree (
  "msg_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "pltfrm_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."message"."cntrb_id" IS 'Not populated for mailing lists. Populated for GitHub issues. ';

CREATE TABLE "augur_data"."message_analysis" (
  "msg_analysis_id" int8 NOT NULL DEFAULT nextval('"augur_data".message_analysis_msg_analysis_id_seq'::regclass),
  "msg_id" int8,
  "worker_run_id" int8,
  "sentiment_score" float8,
  "reconstruction_error" float8,
  "novelty_flag" bool,
  "feedback_flag" bool,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "message_analysis_pkey" PRIMARY KEY ("msg_analysis_id")
);
ALTER TABLE "augur_data"."message_analysis" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."message_analysis"."worker_run_id" IS 'This column is used to indicate analyses run by a worker during the same execution period, and is useful for grouping, and time series analysis.  ';
COMMENT ON COLUMN "augur_data"."message_analysis"."sentiment_score" IS 'A sentiment analysis score. Zero is neutral, negative numbers are negative sentiment, and positive numbers are positive sentiment. ';
COMMENT ON COLUMN "augur_data"."message_analysis"."reconstruction_error" IS 'Each message is converted to a 250 dimensin doc2vec vector, so the reconstruction error is the difference between what the predicted vector and the actual vector.';
COMMENT ON COLUMN "augur_data"."message_analysis"."novelty_flag" IS 'This is an analysis of the degree to which the message is novel when compared to other messages in a repository.  For example when bots are producing numerous identical messages, the novelty score is low. It would also be a low novelty score when several people are making the same coment. ';
COMMENT ON COLUMN "augur_data"."message_analysis"."feedback_flag" IS 'This exists to provide the user with an opportunity provide feedback on the resulting the sentiment scores. ';

CREATE TABLE "augur_data"."message_analysis_summary" (
  "msg_summary_id" int8 NOT NULL DEFAULT nextval('"augur_data".message_analysis_summary_msg_summary_id_seq'::regclass),
  "repo_id" int8,
  "worker_run_id" int8,
  "positive_ratio" float8,
  "negative_ratio" float8,
  "novel_count" int8,
  "period" timestamp(0),
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "message_analysis_summary_pkey" PRIMARY KEY ("msg_summary_id")
);
ALTER TABLE "augur_data"."message_analysis_summary" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."message_analysis_summary"."worker_run_id" IS 'This value should reflect the worker_run_id for the messages summarized in the table. There is not a relation between these two tables for that purpose because its not *really*, relationaly a concept unless we create a third table for "worker_run_id", which we determined was unnecessarily complex. ';
COMMENT ON COLUMN "augur_data"."message_analysis_summary"."novel_count" IS 'The number of messages identified as novel during the analyzed period';
COMMENT ON COLUMN "augur_data"."message_analysis_summary"."period" IS 'The whole timeline is divided into periods based on the definition of time period for analysis, which is user specified. Timestamp of the first period to look at, until the end of messages at the data of execution. ';
COMMENT ON TABLE "augur_data"."message_analysis_summary" IS 'In a relationally perfect world, we would have a table called “message_analysis_run” the incremented the “worker_run_id” for both message_analysis and message_analysis_summary. For now, we decided this was overkill. ';

CREATE TABLE "augur_data"."message_sentiment" (
  "msg_analysis_id" int8 NOT NULL DEFAULT nextval('"augur_data".message_sentiment_msg_analysis_id_seq'::regclass),
  "msg_id" int8,
  "worker_run_id" int8,
  "sentiment_score" float8,
  "reconstruction_error" float8,
  "novelty_flag" bool,
  "feedback_flag" bool,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "message_sentiment_pkey" PRIMARY KEY ("msg_analysis_id")
);
ALTER TABLE "augur_data"."message_sentiment" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."message_sentiment"."worker_run_id" IS 'This column is used to indicate analyses run by a worker during the same execution period, and is useful for grouping, and time series analysis.  ';
COMMENT ON COLUMN "augur_data"."message_sentiment"."sentiment_score" IS 'A sentiment analysis score. Zero is neutral, negative numbers are negative sentiment, and positive numbers are positive sentiment. ';
COMMENT ON COLUMN "augur_data"."message_sentiment"."reconstruction_error" IS 'Each message is converted to a 250 dimensin doc2vec vector, so the reconstruction error is the difference between what the predicted vector and the actual vector.';
COMMENT ON COLUMN "augur_data"."message_sentiment"."novelty_flag" IS 'This is an analysis of the degree to which the message is novel when compared to other messages in a repository.  For example when bots are producing numerous identical messages, the novelty score is low. It would also be a low novelty score when several people are making the same coment. ';
COMMENT ON COLUMN "augur_data"."message_sentiment"."feedback_flag" IS 'This exists to provide the user with an opportunity provide feedback on the resulting the sentiment scores. ';

CREATE TABLE "augur_data"."message_sentiment_summary" (
  "msg_summary_id" int8 NOT NULL DEFAULT nextval('"augur_data".message_sentiment_summary_msg_summary_id_seq'::regclass),
  "repo_id" int8,
  "worker_run_id" int8,
  "positive_ratio" float8,
  "negative_ratio" float8,
  "novel_count" int8,
  "period" timestamp(0),
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "message_sentiment_summary_pkey" PRIMARY KEY ("msg_summary_id")
);
ALTER TABLE "augur_data"."message_sentiment_summary" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."message_sentiment_summary"."worker_run_id" IS 'This value should reflect the worker_run_id for the messages summarized in the table. There is not a relation between these two tables for that purpose because its not *really*, relationaly a concept unless we create a third table for "worker_run_id", which we determined was unnecessarily complex. ';
COMMENT ON COLUMN "augur_data"."message_sentiment_summary"."novel_count" IS 'The number of messages identified as novel during the analyzed period';
COMMENT ON COLUMN "augur_data"."message_sentiment_summary"."period" IS 'The whole timeline is divided into periods based on the definition of time period for analysis, which is user specified. Timestamp of the first period to look at, until the end of messages at the data of execution. ';
COMMENT ON TABLE "augur_data"."message_sentiment_summary" IS 'In a relationally perfect world, we would have a table called “message_sentiment_run” the incremented the “worker_run_id” for both message_sentiment and message_sentiment_summary. For now, we decided this was overkill. ';

CREATE TABLE "augur_data"."platform" (
  "pltfrm_id" int8 NOT NULL DEFAULT nextval('"augur_data".platform_pltfrm_id_seq'::regclass),
  "pltfrm_name" varchar(255) COLLATE "pg_catalog"."default",
  "pltfrm_version" varchar(255) COLLATE "pg_catalog"."default",
  "pltfrm_release_date" date,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "theplat" PRIMARY KEY ("pltfrm_id")
);
ALTER TABLE "augur_data"."platform" OWNER TO "augur";
CREATE UNIQUE INDEX "plat" ON "augur_data"."platform" USING btree (
  "pltfrm_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."pull_request_analysis" (
  "pull_request_analysis_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_analysis_pull_request_analysis_id_seq'::regclass),
  "pull_request_id" int8,
  "merge_probability" numeric(256,250),
  "mechanism" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_analysis_pkey" PRIMARY KEY ("pull_request_analysis_id")
);
ALTER TABLE "augur_data"."pull_request_analysis" OWNER TO "augur";
CREATE INDEX "pr_anal_idx" ON "augur_data"."pull_request_analysis" USING btree (
  "pull_request_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "probability_idx" ON "augur_data"."pull_request_analysis" USING btree (
  "merge_probability" "pg_catalog"."numeric_ops" DESC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."pull_request_analysis"."pull_request_id" IS 'It would be better if the pull request worker is run first to fetch the latest PRs before analyzing';
COMMENT ON COLUMN "augur_data"."pull_request_analysis"."merge_probability" IS 'Indicates the probability of the PR being merged';
COMMENT ON COLUMN "augur_data"."pull_request_analysis"."mechanism" IS 'the ML model used for prediction (It is XGBoost Classifier at present)';

CREATE TABLE "augur_data"."pull_request_assignees" (
  "pr_assignee_map_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_assignees_pr_assignee_map_id_seq'::regclass),
  "pull_request_id" int8,
  "contrib_id" int8,
  "pr_assignee_src_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_assignees_pkey" PRIMARY KEY ("pr_assignee_map_id")
);
ALTER TABLE "augur_data"."pull_request_assignees" OWNER TO "augur";
CREATE INDEX "pr_meta_cntrb-idx" ON "augur_data"."pull_request_assignees" USING btree (
  "contrib_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."pull_request_commits" (
  "pr_cmt_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_commits_pr_cmt_id_seq'::regclass),
  "pull_request_id" int8,
  "pr_cmt_sha" varchar COLLATE "pg_catalog"."default",
  "pr_cmt_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_cmt_message" varchar COLLATE "pg_catalog"."default",
  "pr_cmt_comments_url" varbit,
  "pr_cmt_author_cntrb_id" int8,
  "pr_cmt_timestamp" timestamp(0),
  "pr_cmt_author_email" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_commits_pkey" PRIMARY KEY ("pr_cmt_id")
);
ALTER TABLE "augur_data"."pull_request_commits" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."pull_request_commits"."pr_cmt_sha" IS 'This is the commit SHA for a pull request commit. If the PR is not to the master branch of the main repository (or, in rare cases, from it), then you will NOT find a corresponding commit SHA in the commit table. (see table comment for further explanation). ';
COMMENT ON TABLE "augur_data"."pull_request_commits" IS 'Pull request commits are an enumeration of each commit associated with a pull request. 
Not all pull requests are from a branch or fork into master. 
The commits table intends to count only commits that end up in the master branch (i.e., part of the deployed code base for a project).
Therefore, there will be commit “SHA”’s in this table that are no associated with a commit SHA in the commits table. 
In cases where the PR is to the master branch of a project, you will find a match. In cases where the PR does not involve the master branch, you will not find a corresponding commit SHA in the commits table. This is expected. ';

CREATE TABLE "augur_data"."pull_request_events" (
  "pr_event_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_events_pr_event_id_seq'::regclass),
  "pull_request_id" int8 NOT NULL,
  "cntrb_id" int8 NOT NULL,
  "action" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "action_commit_hash" varchar COLLATE "pg_catalog"."default",
  "created_at" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "issue_event_src_id" int8,
  "node_id" varchar COLLATE "pg_catalog"."default",
  "node_url" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pr_events_pkey" PRIMARY KEY ("pr_event_id")
);
ALTER TABLE "augur_data"."pull_request_events" OWNER TO "augur";
CREATE INDEX "pr_events_ibfk_1" ON "augur_data"."pull_request_events" USING btree (
  "pull_request_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "pr_events_ibfk_2" ON "augur_data"."pull_request_events" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."pull_request_events"."issue_event_src_id" IS 'This ID comes from the source. In the case of GitHub, it is the id that is the first field returned from the issue events API';
COMMENT ON COLUMN "augur_data"."pull_request_events"."node_id" IS 'This should be renamed to issue_event_src_node_id, as its the varchar identifier in GitHub and likely common in other sources as well. However, since it was created before we came to this naming standard and workers are built around it, we have it simply named as node_id. Anywhere you see node_id in the schema, it comes from GitHubs terminology.';

CREATE TABLE "augur_data"."pull_request_files" (
  "pull_request_id" int8,
  "pr_file_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_files_pr_file_id_seq'::regclass),
  "pr_file_additions" int8,
  "pr_file_deletions" int8,
  "pr_file_path" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_files_pkey" PRIMARY KEY ("pr_file_id")
);
ALTER TABLE "augur_data"."pull_request_files" OWNER TO "augur";
COMMENT ON TABLE "augur_data"."pull_request_files" IS 'Pull request commits are an enumeration of each commit associated with a pull request. 
Not all pull requests are from a branch or fork into master. 
The commits table intends to count only commits that end up in the master branch (i.e., part of the deployed code base for a project).
Therefore, there will be commit “SHA”’s in this table that are no associated with a commit SHA in the commits table. 
In cases where the PR is to the master branch of a project, you will find a match. In cases where the PR does not involve the master branch, you will not find a corresponding commit SHA in the commits table. This is expected. ';

CREATE TABLE "augur_data"."pull_request_labels" (
  "pr_label_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_labels_pr_label_id_seq'::regclass),
  "pull_request_id" int8,
  "pr_src_id" int8,
  "pr_src_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_src_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_description" varchar COLLATE "pg_catalog"."default",
  "pr_src_color" varchar COLLATE "pg_catalog"."default",
  "pr_src_default_bool" bool,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_labels_pkey" PRIMARY KEY ("pr_label_id")
);
ALTER TABLE "augur_data"."pull_request_labels" OWNER TO "augur";

CREATE TABLE "augur_data"."pull_request_message_ref" (
  "pr_msg_ref_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_message_ref_pr_msg_ref_id_seq'::regclass),
  "pull_request_id" int8,
  "msg_id" int8,
  "pr_message_ref_src_comment_id" int8,
  "pr_message_ref_src_node_id" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_message_ref_pkey" PRIMARY KEY ("pr_msg_ref_id")
);
ALTER TABLE "augur_data"."pull_request_message_ref" OWNER TO "augur";

CREATE TABLE "augur_data"."pull_request_meta" (
  "pr_repo_meta_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_meta_pr_repo_meta_id_seq'::regclass),
  "pull_request_id" int8,
  "pr_head_or_base" varchar COLLATE "pg_catalog"."default",
  "pr_src_meta_label" varchar COLLATE "pg_catalog"."default",
  "pr_src_meta_ref" varchar COLLATE "pg_catalog"."default",
  "pr_sha" varchar COLLATE "pg_catalog"."default",
  "cntrb_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_meta_pkey" PRIMARY KEY ("pr_repo_meta_id")
);
ALTER TABLE "augur_data"."pull_request_meta" OWNER TO "augur";
CREATE INDEX "pr_meta-cntrbid-idx" ON "augur_data"."pull_request_meta" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."pull_request_meta"."pr_head_or_base" IS 'Each pull request should have one and only one head record; and one and only one base record. ';
COMMENT ON COLUMN "augur_data"."pull_request_meta"."pr_src_meta_label" IS 'This is a representation of the repo:branch information in the pull request. Head is issueing the pull request and base is taking the pull request. For example:  (We do not store all of this)

 "head": {
      "label": "chaoss:pull-request-worker",
      "ref": "pull-request-worker",
      "sha": "6b380c3d6d625616f79d702612ebab6d204614f2",
      "user": {
        "login": "chaoss",
        "id": 29740296,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",
        "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/chaoss",
        "html_url": "https://github.com/chaoss",
        "followers_url": "https://api.github.com/users/chaoss/followers",
        "following_url": "https://api.github.com/users/chaoss/following{/other_user}",
        "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",
        "organizations_url": "https://api.github.com/users/chaoss/orgs",
        "repos_url": "https://api.github.com/users/chaoss/repos",
        "events_url": "https://api.github.com/users/chaoss/events{/privacy}",
        "received_events_url": "https://api.github.com/users/chaoss/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "repo": {
        "id": 78134122,
        "node_id": "MDEwOlJlcG9zaXRvcnk3ODEzNDEyMg==",
        "name": "augur",
        "full_name": "chaoss/augur",
        "private": false,
        "owner": {
          "login": "chaoss",
          "id": 29740296,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",
          "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/chaoss",
          "html_url": "https://github.com/chaoss",
          "followers_url": "https://api.github.com/users/chaoss/followers",
          "following_url": "https://api.github.com/users/chaoss/following{/other_user}",
          "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",
          "organizations_url": "https://api.github.com/users/chaoss/orgs",
          "repos_url": "https://api.github.com/users/chaoss/repos",
          "events_url": "https://api.github.com/users/chaoss/events{/privacy}",
          "received_events_url": "https://api.github.com/users/chaoss/received_events",
          "type": "Organization",
          "site_admin": false
        },
        "html_url": "https://github.com/chaoss/augur",
        "description": "Python library and web service for Open Source Software Health and Sustainability metrics & data collection.",
        "fork": false,
        "url": "https://api.github.com/repos/chaoss/augur",
        "forks_url": "https://api.github.com/repos/chaoss/augur/forks",
        "keys_url": "https://api.github.com/repos/chaoss/augur/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/chaoss/augur/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/chaoss/augur/teams",
        "hooks_url": "https://api.github.com/repos/chaoss/augur/hooks",
        "issue_events_url": "https://api.github.com/repos/chaoss/augur/issues/events{/number}",
        "events_url": "https://api.github.com/repos/chaoss/augur/events",
        "assignees_url": "https://api.github.com/repos/chaoss/augur/assignees{/user}",
        "branches_url": "https://api.github.com/repos/chaoss/augur/branches{/branch}",
        "tags_url": "https://api.github.com/repos/chaoss/augur/tags",
        "blobs_url": "https://api.github.com/repos/chaoss/augur/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/chaoss/augur/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/chaoss/augur/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/chaoss/augur/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/chaoss/augur/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/chaoss/augur/languages",
        "stargazers_url": "https://api.github.com/repos/chaoss/augur/stargazers",
        "contributors_url": "https://api.github.com/repos/chaoss/augur/contributors",
        "subscribers_url": "https://api.github.com/repos/chaoss/augur/subscribers",
        "subscription_url": "https://api.github.com/repos/chaoss/augur/subscription",
        "commits_url": "https://api.github.com/repos/chaoss/augur/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/chaoss/augur/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/chaoss/augur/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/chaoss/augur/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/chaoss/augur/contents/{+path}",
        "compare_url": "https://api.github.com/repos/chaoss/augur/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/chaoss/augur/merges",
        "archive_url": "https://api.github.com/repos/chaoss/augur/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/chaoss/augur/downloads",
        "issues_url": "https://api.github.com/repos/chaoss/augur/issues{/number}",
        "pulls_url": "https://api.github.com/repos/chaoss/augur/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/chaoss/augur/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/chaoss/augur/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/chaoss/augur/labels{/name}",
        "releases_url": "https://api.github.com/repos/chaoss/augur/releases{/id}",
        "deployments_url": "https://api.github.com/repos/chaoss/augur/deployments",
        "created_at": "2017-01-05T17:34:54Z",
        "updated_at": "2019-11-15T00:56:12Z",
        "pushed_at": "2019-12-02T06:27:26Z",
        "git_url": "git://github.com/chaoss/augur.git",
        "ssh_url": "git@github.com:chaoss/augur.git",
        "clone_url": "https://github.com/chaoss/augur.git",
        "svn_url": "https://github.com/chaoss/augur",
        "homepage": "http://augur.osshealth.io/",
        "size": 82004,
        "stargazers_count": 153,
        "watchers_count": 153,
        "language": "Python",
        "has_issues": true,
        "has_projects": false,
        "has_downloads": true,
        "has_wiki": false,
        "has_pages": true,
        "forks_count": 205,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 14,
        "license": {
          "key": "mit",
          "name": "MIT License",
          "spdx_id": "MIT",
          "url": "https://api.github.com/licenses/mit",
          "node_id": "MDc6TGljZW5zZTEz"
        },
        "forks": 205,
        "open_issues": 14,
        "watchers": 153,
        "default_branch": "master"
      }
    },
    "base": {
      "label": "chaoss:dev",
      "ref": "dev",
      "sha": "bfd2d34b51659613dd842cf83c3873f7699c2a0e",
      "user": {
        "login": "chaoss",
        "id": 29740296,
        "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",
        "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/chaoss",
        "html_url": "https://github.com/chaoss",
        "followers_url": "https://api.github.com/users/chaoss/followers",
        "following_url": "https://api.github.com/users/chaoss/following{/other_user}",
        "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",
        "organizations_url": "https://api.github.com/users/chaoss/orgs",
        "repos_url": "https://api.github.com/users/chaoss/repos",
        "events_url": "https://api.github.com/users/chaoss/events{/privacy}",
        "received_events_url": "https://api.github.com/users/chaoss/received_events",
        "type": "Organization",
        "site_admin": false
      },
      "repo": {
        "id": 78134122,
        "node_id": "MDEwOlJlcG9zaXRvcnk3ODEzNDEyMg==",
        "name": "augur",
        "full_name": "chaoss/augur",
        "private": false,
        "owner": {
          "login": "chaoss",
          "id": 29740296,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",
          "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/chaoss",
          "html_url": "https://github.com/chaoss",
          "followers_url": "https://api.github.com/users/chaoss/followers",
          "following_url": "https://api.github.com/users/chaoss/following{/other_user}",
          "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",
          "organizations_url": "https://api.github.com/users/chaoss/orgs",
          "repos_url": "https://api.github.com/users/chaoss/repos",
          "events_url": "https://api.github.com/users/chaoss/events{/privacy}",
          "received_events_url": "https://api.github.com/users/chaoss/received_events",
          "type": "Organization",
          "site_admin": false
        },
';
COMMENT ON TABLE "augur_data"."pull_request_meta" IS 'Pull requests contain referencing metadata.  There are a few columns that are discrete. There are also head and base designations for the repo on each side of the pull request. Similar functions exist in GitLab, though the language here is based on GitHub. The JSON Being adapted to as of the development of this schema is here:      "base": {       "label": "chaoss:dev",       "ref": "dev",       "sha": "dc6c6f3947f7dc84ecba3d8bda641ef786e7027d",       "user": {         "login": "chaoss",         "id": 29740296,         "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",         "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",         "gravatar_id": "",         "url": "https://api.github.com/users/chaoss",         "html_url": "https://github.com/chaoss",         "followers_url": "https://api.github.com/users/chaoss/followers",         "following_url": "https://api.github.com/users/chaoss/following{/other_user}",         "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",         "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",         "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",         "organizations_url": "https://api.github.com/users/chaoss/orgs",         "repos_url": "https://api.github.com/users/chaoss/repos",         "events_url": "https://api.github.com/users/chaoss/events{/privacy}",         "received_events_url": "https://api.github.com/users/chaoss/received_events",         "type": "Organization",         "site_admin": false       },       "repo": {         "id": 78134122,         "node_id": "MDEwOlJlcG9zaXRvcnk3ODEzNDEyMg==",         "name": "augur",         "full_name": "chaoss/augur",         "private": false,         "owner": {           "login": "chaoss",           "id": 29740296,           "node_id": "MDEyOk9yZ2FuaXphdGlvbjI5NzQwMjk2",           "avatar_url": "https://avatars2.githubusercontent.com/u/29740296?v=4",           "gravatar_id": "",           "url": "https://api.github.com/users/chaoss",           "html_url": "https://github.com/chaoss",           "followers_url": "https://api.github.com/users/chaoss/followers",           "following_url": "https://api.github.com/users/chaoss/following{/other_user}",           "gists_url": "https://api.github.com/users/chaoss/gists{/gist_id}",           "starred_url": "https://api.github.com/users/chaoss/starred{/owner}{/repo}",           "subscriptions_url": "https://api.github.com/users/chaoss/subscriptions",           "organizations_url": "https://api.github.com/users/chaoss/orgs",           "repos_url": "https://api.github.com/users/chaoss/repos",           "events_url": "https://api.github.com/users/chaoss/events{/privacy}",           "received_events_url": "https://api.github.com/users/chaoss/received_events",           "type": "Organization",           "site_admin": false         }, ';

CREATE TABLE "augur_data"."pull_request_repo" (
  "pr_repo_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_repo_pr_repo_id_seq'::regclass),
  "pr_repo_meta_id" int8,
  "pr_repo_head_or_base" varchar COLLATE "pg_catalog"."default",
  "pr_src_repo_id" int8,
  "pr_src_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_repo_name" varchar COLLATE "pg_catalog"."default",
  "pr_repo_full_name" varchar COLLATE "pg_catalog"."default",
  "pr_repo_private_bool" bool,
  "pr_cntrb_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_repo_pkey" PRIMARY KEY ("pr_repo_id")
);
ALTER TABLE "augur_data"."pull_request_repo" OWNER TO "augur";
CREATE INDEX "pr-cntrb-idx-repo" ON "augur_data"."pull_request_repo" USING btree (
  "pr_cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."pull_request_repo"."pr_repo_head_or_base" IS 'For ease of validation checking, we should determine if the repository referenced is the head or base of the pull request. Each pull request should have one and only one of these, which is not enforcable easily in the database.';
COMMENT ON TABLE "augur_data"."pull_request_repo" IS 'This table is for storing information about forks that exist as part of a pull request. Generally we do not want to track these like ordinary repositories. ';

CREATE TABLE "augur_data"."pull_request_review_message_ref" (
  "pr_review_msg_ref_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_review_message_ref_pr_review_msg_ref_id_seq'::regclass),
  "pr_review_id" int8 NOT NULL,
  "msg_id" int8 NOT NULL,
  "pr_review_msg_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_src_id" int8,
  "pr_review_msg_src_id" int8,
  "pr_review_msg_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_diff_hunk" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_path" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_position" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_original_position" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_commit_id" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_original_commit_id" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_updated_at" timestamp(6),
  "pr_review_msg_html_url" varchar COLLATE "pg_catalog"."default",
  "pr_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_author_association" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_start_line" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_original_start_line" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_start_side" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_line" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_original_line" varchar COLLATE "pg_catalog"."default",
  "pr_review_msg_side" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pr_review_msg_ref_id" PRIMARY KEY ("pr_review_msg_ref_id")
);
ALTER TABLE "augur_data"."pull_request_review_message_ref" OWNER TO "augur";

CREATE TABLE "augur_data"."pull_request_reviewers" (
  "pr_reviewer_map_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_reviewers_pr_reviewer_map_id_seq'::regclass),
  "pull_request_id" int8,
  "cntrb_id" int8,
  "pr_reviewer_src_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_reviewers_pkey" PRIMARY KEY ("pr_reviewer_map_id")
);
ALTER TABLE "augur_data"."pull_request_reviewers" OWNER TO "augur";
CREATE INDEX "pr-reviewers-cntrb-idx1" ON "augur_data"."pull_request_reviewers" USING btree (
  "cntrb_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."pull_request_reviews" (
  "pr_review_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_reviews_pr_review_id_seq'::regclass),
  "pull_request_id" int8 NOT NULL,
  "cntrb_id" int8 NOT NULL,
  "pr_review_author_association" varchar COLLATE "pg_catalog"."default",
  "pr_review_state" varchar COLLATE "pg_catalog"."default",
  "pr_review_body" varchar COLLATE "pg_catalog"."default",
  "pr_review_submitted_at" timestamp(6),
  "pr_review_src_id" int8,
  "pr_review_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_review_html_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_pull_request_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_commit_id" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_review_id" PRIMARY KEY ("pr_review_id")
);
ALTER TABLE "augur_data"."pull_request_reviews" OWNER TO "augur";

CREATE TABLE "augur_data"."pull_request_teams" (
  "pr_team_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_request_teams_pr_team_id_seq'::regclass),
  "pull_request_id" int8,
  "pr_src_team_id" int8,
  "pr_src_team_node" varchar COLLATE "pg_catalog"."default",
  "pr_src_team_url" varchar COLLATE "pg_catalog"."default",
  "pr_team_name" varchar COLLATE "pg_catalog"."default",
  "pr_team_slug" varchar COLLATE "pg_catalog"."default",
  "pr_team_description" varchar COLLATE "pg_catalog"."default",
  "pr_team_privacy" varchar COLLATE "pg_catalog"."default",
  "pr_team_permission" varchar COLLATE "pg_catalog"."default",
  "pr_team_src_members_url" varchar COLLATE "pg_catalog"."default",
  "pr_team_src_repositories_url" varchar COLLATE "pg_catalog"."default",
  "pr_team_parent_id" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_request_teams_pkey" PRIMARY KEY ("pr_team_id")
);
ALTER TABLE "augur_data"."pull_request_teams" OWNER TO "augur";

CREATE TABLE "augur_data"."pull_requests" (
  "pull_request_id" int8 NOT NULL DEFAULT nextval('"augur_data".pull_requests_pull_request_id_seq'::regclass),
  "pr_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_id" int8,
  "pr_src_node_id" varchar COLLATE "pg_catalog"."default",
  "pr_html_url" varchar COLLATE "pg_catalog"."default",
  "pr_diff_url" varchar COLLATE "pg_catalog"."default",
  "pr_patch_url" varchar COLLATE "pg_catalog"."default",
  "pr_issue_url" varchar COLLATE "pg_catalog"."default",
  "pr_augur_issue_id" int8,
  "pr_src_number" int8,
  "pr_src_state" varchar COLLATE "pg_catalog"."default",
  "pr_src_locked" bool,
  "pr_src_title" varchar COLLATE "pg_catalog"."default",
  "pr_augur_contributor_id" int8,
  "pr_body" text COLLATE "pg_catalog"."default",
  "pr_created_at" timestamp(0),
  "pr_updated_at" timestamp(0),
  "pr_closed_at" timestamp(0),
  "pr_merged_at" timestamp(0),
  "pr_merge_commit_sha" varchar COLLATE "pg_catalog"."default",
  "pr_teams" int8,
  "pr_milestone" varchar COLLATE "pg_catalog"."default",
  "pr_commits_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_comments_url" varchar COLLATE "pg_catalog"."default",
  "pr_review_comment_url" varchar COLLATE "pg_catalog"."default",
  "pr_comments_url" varchar COLLATE "pg_catalog"."default",
  "pr_statuses_url" varchar COLLATE "pg_catalog"."default",
  "pr_meta_head_id" int8,
  "pr_meta_base_id" int8,
  "pr_src_issue_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_comments_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_review_comments_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_commits_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_statuses_url" varchar COLLATE "pg_catalog"."default",
  "pr_src_author_association" varchar COLLATE "pg_catalog"."default",
  "repo_id" int8 DEFAULT 0,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "pull_requests_pkey" PRIMARY KEY ("pull_request_id")
);
ALTER TABLE "augur_data"."pull_requests" OWNER TO "augur";
CREATE INDEX "id_node" ON "augur_data"."pull_requests" USING btree (
  "pr_src_id" "pg_catalog"."int8_ops" DESC NULLS FIRST,
  "pr_src_node_id" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" DESC NULLS LAST
);
CREATE INDEX "pull_requests_idx_repo_id_data_datex" ON "augur_data"."pull_requests" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "data_collection_date" "pg_catalog"."timestamp_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_src_id" IS 'The pr_src_id is unique across all of github.';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_augur_issue_id" IS 'This is to link to the augur stored related issue';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_src_number" IS 'The pr_src_number is unique within a repository.';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_augur_contributor_id" IS 'This is to link to the augur contributor record. ';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_teams" IS 'One to many with pull request teams. ';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_review_comment_url" IS 'This is a field with limited utility. It does expose how to access a specific comment if needed with parameters. If the source changes URL structure, it may be useful';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_meta_head_id" IS 'The metadata for the head repo that links to the pull_request_meta table. ';
COMMENT ON COLUMN "augur_data"."pull_requests"."pr_meta_base_id" IS 'The metadata for the base repo that links to the pull_request_meta table. ';

CREATE TABLE "augur_data"."releases" (
  "release_id" char(64) COLLATE "pg_catalog"."default" NOT NULL DEFAULT nextval('"augur_data".releases_release_id_seq'::regclass),
  "repo_id" int8 NOT NULL,
  "release_name" varchar(255) COLLATE "pg_catalog"."default",
  "release_description" varchar COLLATE "pg_catalog"."default",
  "release_author" varchar(255) COLLATE "pg_catalog"."default",
  "release_created_at" timestamp(6),
  "release_published_at" timestamp(6),
  "release_updated_at" timestamp(6),
  "release_is_draft" bool,
  "release_is_prerelease" bool,
  "release_tag_name" varchar(255) COLLATE "pg_catalog"."default",
  "release_url" varchar(255) COLLATE "pg_catalog"."default",
  "tag_only" bool,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "releases_pkey" PRIMARY KEY ("release_id")
);
ALTER TABLE "augur_data"."releases" OWNER TO "augur";

CREATE TABLE "augur_data"."repo" (
  "repo_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_repo_id_seq'::regclass),
  "repo_group_id" int8 NOT NULL,
  "repo_git" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "repo_path" varchar(256) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "repo_name" varchar COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "repo_added" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "repo_status" varchar(32) COLLATE "pg_catalog"."default" NOT NULL DEFAULT 'New'::character varying,
  "repo_type" varchar COLLATE "pg_catalog"."default" DEFAULT ''::character varying,
  "url" varchar(255) COLLATE "pg_catalog"."default",
  "owner_id" int4,
  "description" varchar COLLATE "pg_catalog"."default",
  "primary_language" varchar(255) COLLATE "pg_catalog"."default",
  "created_at" varchar(255) COLLATE "pg_catalog"."default",
  "forked_from" varchar COLLATE "pg_catalog"."default",
  "updated_at" timestamp(0),
  "repo_archived" int4,
  "repo_archived_date_collected" timestamptz(0),
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "repounique" PRIMARY KEY ("repo_id")
);
ALTER TABLE "augur_data"."repo" OWNER TO "augur";
CREATE INDEX "forked" ON "augur_data"."repo" USING btree (
  "forked_from" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repo_idx_repo_id_repo_namex" ON "augur_data"."repo" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "repo_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repogitindexrep" ON "augur_data"."repo" USING btree (
  "repo_git" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "reponameindex" ON "augur_data"."repo" USING hash (
  "repo_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops"
);
CREATE INDEX "reponameindexbtree" ON "augur_data"."repo" USING btree (
  "repo_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "rggrouponrepoindex" ON "augur_data"."repo" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE UNIQUE INDEX "therepo" ON "augur_data"."repo" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."repo"."repo_type" IS 'This field is intended to indicate if the repository is the "main instance" of a repository in cases where implementations choose to add the same repository to more than one repository group. In cases where the repository group is of rg_type Github Organization then this repo_type should be "primary". In other cases the repo_type should probably be "user created". We made this a varchar in order to hold open the possibility that there are additional repo_types we have not thought about. ';
COMMENT ON TABLE "augur_data"."repo" IS 'This table is a combination of the columns in Facade’s repo table and GHTorrent’s projects table. ';

CREATE TABLE "augur_data"."repo_badging" (
  "badge_collection_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_badging_badge_collection_id_seq'::regclass),
  "repo_id" int8,
  "created_at" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  "data" jsonb,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_badging_pkey" PRIMARY KEY ("badge_collection_id")
);
ALTER TABLE "augur_data"."repo_badging" OWNER TO "augur";
COMMENT ON TABLE "augur_data"."repo_badging" IS 'This will be collected from the LF’s Badging API
https://bestpractices.coreinfrastructure.org/projects.json?pq=https%3A%2F%2Fgithub.com%2Fchaoss%2Faugur
';

CREATE TABLE "augur_data"."repo_cluster_messages" (
  "msg_cluster_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_cluster_messages_msg_cluster_id_seq'::regclass),
  "repo_id" int8,
  "cluster_content" int4,
  "cluster_mechanism" int4,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_cluster_messages_pkey" PRIMARY KEY ("msg_cluster_id")
);
ALTER TABLE "augur_data"."repo_cluster_messages" OWNER TO "augur";

CREATE TABLE "augur_data"."repo_dependencies" (
  "repo_dependencies_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_dependencies_repo_dependencies_id_seq'::regclass),
  "repo_id" int8,
  "dep_name" varchar(255) COLLATE "pg_catalog"."default",
  "dep_count" int4,
  "dep_language" varchar(255) COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_dependencies_pkey" PRIMARY KEY ("repo_dependencies_id")
);
ALTER TABLE "augur_data"."repo_dependencies" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."repo_dependencies"."repo_id" IS 'Forign key for repo id. ';
COMMENT ON COLUMN "augur_data"."repo_dependencies"."dep_name" IS 'Name of the dependancy found in project. ';
COMMENT ON COLUMN "augur_data"."repo_dependencies"."dep_count" IS 'Number of times the dependancy was found. ';
COMMENT ON COLUMN "augur_data"."repo_dependencies"."dep_language" IS 'Language of the dependancy. ';
COMMENT ON TABLE "augur_data"."repo_dependencies" IS 'Contains the dependencies for a repo.';

CREATE TABLE "augur_data"."repo_deps_scorecard" (
  "repo_deps_scorecard_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_deps_scorecard_repo_deps_scorecard_id_seq1'::regclass),
  "repo_id" int8,
  "name" varchar COLLATE "pg_catalog"."default",
  "status" varchar COLLATE "pg_catalog"."default",
  "score" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_deps_scorecard_pkey1" PRIMARY KEY ("repo_deps_scorecard_id")
);
ALTER TABLE "augur_data"."repo_deps_scorecard" OWNER TO "augur";

CREATE TABLE "augur_data"."repo_group_insights" (
  "rgi_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_group_insights_rgi_id_seq'::regclass),
  "repo_group_id" int8,
  "rgi_metric" varchar COLLATE "pg_catalog"."default",
  "rgi_value" varchar COLLATE "pg_catalog"."default",
  "cms_id" int8,
  "rgi_fresh" bool,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_group_insights_pkey" PRIMARY KEY ("rgi_id")
);
ALTER TABLE "augur_data"."repo_group_insights" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."repo_group_insights"."rgi_fresh" IS 'false if the date is before the statistic that triggered the insight, true if after. This allows us to automatically display only "fresh insights" and avoid displaying "stale insights". The insight worker will populate this table. ';
COMMENT ON TABLE "augur_data"."repo_group_insights" IS 'This table is output from an analytical worker inside of Augur. It runs through the different metrics on a REPOSITORY_GROUP and identifies the five to ten most “interesting” metrics as defined by some kind of delta or other factor. The algorithm is going to evolve. 

Worker Design Notes: The idea is that the "insight worker" will scan through a bunch of active metrics or "synthetic metrics" to list the most important insights. ';

CREATE TABLE "augur_data"."repo_groups" (
  "repo_group_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_groups_repo_group_id_seq'::regclass),
  "rg_name" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "rg_description" varchar COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "rg_website" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "rg_recache" int2 DEFAULT 1,
  "rg_last_modified" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "rg_type" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "rgid" PRIMARY KEY ("repo_group_id")
);
ALTER TABLE "augur_data"."repo_groups" OWNER TO "augur";
CREATE UNIQUE INDEX "rgidm" ON "augur_data"."repo_groups" USING btree (
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);
CREATE INDEX "rgnameindex" ON "augur_data"."repo_groups" USING btree (
  "rg_name" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
COMMENT ON TABLE "augur_data"."repo_groups" IS 'rg_type is intended to be either a GitHub Organization or a User Created Repo Group. ';

CREATE TABLE "augur_data"."repo_groups_list_serve" (
  "rgls_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_groups_list_serve_rgls_id_seq'::regclass),
  "repo_group_id" int8 NOT NULL,
  "rgls_name" varchar(255) COLLATE "pg_catalog"."default",
  "rgls_description" varchar(3000) COLLATE "pg_catalog"."default",
  "rgls_sponsor" varchar(255) COLLATE "pg_catalog"."default",
  "rgls_email" varchar(255) COLLATE "pg_catalog"."default",
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "repo_groups_list_serve_pkey" PRIMARY KEY ("rgls_id"),
  CONSTRAINT "rglistserve" UNIQUE ("rgls_id", "repo_group_id")
);
ALTER TABLE "augur_data"."repo_groups_list_serve" OWNER TO "augur";
CREATE UNIQUE INDEX "lister" ON "augur_data"."repo_groups_list_serve" USING btree (
  "rgls_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "repo_group_id" "pg_catalog"."int8_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."repo_info" (
  "repo_info_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_info_repo_info_id_seq'::regclass),
  "repo_id" int8 NOT NULL,
  "last_updated" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "issues_enabled" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "open_issues" int4,
  "pull_requests_enabled" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "wiki_enabled" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "pages_enabled" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "fork_count" int4,
  "default_branch" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "watchers_count" int4,
  "UUID" int4,
  "license" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "stars_count" int4,
  "committers_count" int4,
  "issue_contributors_count" varchar(255) COLLATE "pg_catalog"."default",
  "changelog_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "contributing_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "license_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "code_of_conduct_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "security_issue_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "security_audit_file" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "status" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "keywords" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "commit_count" int8,
  "issues_count" int8,
  "issues_closed" int8,
  "pull_request_count" int8,
  "pull_requests_open" int8,
  "pull_requests_closed" int8,
  "pull_requests_merged" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_info_pkey" PRIMARY KEY ("repo_info_id")
);
ALTER TABLE "augur_data"."repo_info" OWNER TO "augur";
CREATE INDEX "repo_info_idx_repo_id_data_date_1x" ON "augur_data"."repo_info" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "data_collection_date" "pg_catalog"."timestamp_ops" ASC NULLS LAST
);
CREATE INDEX "repo_info_idx_repo_id_data_datex" ON "augur_data"."repo_info" USING btree (
  "repo_id" "pg_catalog"."int8_ops" ASC NULLS LAST,
  "data_collection_date" "pg_catalog"."timestamp_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."repo_insights" (
  "ri_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_insights_ri_id_seq'::regclass),
  "repo_id" int8,
  "ri_metric" varchar COLLATE "pg_catalog"."default",
  "ri_value" varchar(255) COLLATE "pg_catalog"."default",
  "ri_date" timestamp(0),
  "ri_fresh" bool,
  "ri_score" numeric,
  "ri_field" varchar(255) COLLATE "pg_catalog"."default",
  "ri_detection_method" varchar(255) COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_insights_pkey" PRIMARY KEY ("ri_id")
);
ALTER TABLE "augur_data"."repo_insights" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."repo_insights"."ri_fresh" IS 'false if the date is before the statistic that triggered the insight, true if after. This allows us to automatically display only "fresh insights" and avoid displaying "stale insights". The insight worker will populate this table. ';
COMMENT ON TABLE "augur_data"."repo_insights" IS 'This table is output from an analytical worker inside of Augur. It runs through the different metrics on a repository and identifies the five to ten most “interesting” metrics as defined by some kind of delta or other factor. The algorithm is going to evolve. 

Worker Design Notes: The idea is that the "insight worker" will scan through a bunch of active metrics or "synthetic metrics" to list the most important insights. ';

CREATE TABLE "augur_data"."repo_insights_records" (
  "ri_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_insights_records_ri_id_seq'::regclass),
  "repo_id" int8,
  "ri_metric" varchar COLLATE "pg_catalog"."default",
  "ri_field" varchar COLLATE "pg_catalog"."default",
  "ri_value" varchar COLLATE "pg_catalog"."default",
  "ri_date" timestamp(6),
  "ri_score" float8,
  "ri_detection_method" varchar COLLATE "pg_catalog"."default",
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(6) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_insights_records_pkey" PRIMARY KEY ("ri_id")
);
ALTER TABLE "augur_data"."repo_insights_records" OWNER TO "augur";
CREATE INDEX "dater" ON "augur_data"."repo_insights_records" USING btree (
  "ri_date" "pg_catalog"."timestamp_ops" ASC NULLS LAST
);
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_id" IS 'Primary key. ';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."repo_id" IS 'Refers to repo table primary key. Will have a foreign key';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_metric" IS 'The metric endpoint';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_field" IS 'The field in the metric endpoint';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_value" IS 'The value of the endpoint in ri_field';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_date" IS 'The date the insight is for; in other words, some anomaly occurred on this date. ';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_score" IS 'A Score, derived from the algorithm used. ';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."ri_detection_method" IS 'A confidence interval or other expression of the type of threshold and the value of a threshold met in order for it to be "an insight". Example. "95% confidence interval". ';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."tool_source" IS 'Standard Augur Metadata';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."tool_version" IS 'Standard Augur Metadata';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."data_source" IS 'Standard Augur Metadata';
COMMENT ON COLUMN "augur_data"."repo_insights_records"."data_collection_date" IS 'Standard Augur Metadata';

CREATE TABLE "augur_data"."repo_labor" (
  "repo_labor_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_labor_repo_labor_id_seq'::regclass),
  "repo_id" int8,
  "repo_clone_date" timestamp(0),
  "rl_analysis_date" timestamp(0),
  "programming_language" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "file_path" varchar(500) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "file_name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "total_lines" int4,
  "code_lines" int4,
  "comment_lines" int4,
  "blank_lines" int4,
  "code_complexity" int4,
  "repo_url" varchar(500) COLLATE "pg_catalog"."default" DEFAULT NULL::character varying,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "repo_labor_pkey" PRIMARY KEY ("repo_labor_id")
);
ALTER TABLE "augur_data"."repo_labor" OWNER TO "augur";
COMMENT ON COLUMN "augur_data"."repo_labor"."repo_url" IS 'This is a convenience column to simplify analysis against external datasets';
COMMENT ON TABLE "augur_data"."repo_labor" IS 'repo_labor is a derivative of tables used to store scc code and complexity counting statistics that are inputs to labor analysis, which are components of CHAOSS value metric calculations. ';

CREATE TABLE "augur_data"."repo_meta" (
  "repo_id" int8 NOT NULL,
  "rmeta_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_meta_rmeta_id_seq'::regclass),
  "rmeta_name" varchar(255) COLLATE "pg_catalog"."default",
  "rmeta_value" varchar(255) COLLATE "pg_catalog"."default" DEFAULT 0,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "repo_meta_pkey" PRIMARY KEY ("rmeta_id", "repo_id")
);
ALTER TABLE "augur_data"."repo_meta" OWNER TO "augur";
COMMENT ON TABLE "augur_data"."repo_meta" IS 'Project Languages';

CREATE TABLE "augur_data"."repo_sbom_scans" (
  "rsb_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_sbom_scans_rsb_id_seq'::regclass),
  "repo_id" int4,
  "sbom_scan" json,
  CONSTRAINT "repo_sbom_scans_pkey" PRIMARY KEY ("rsb_id")
);
ALTER TABLE "augur_data"."repo_sbom_scans" OWNER TO "augur";

CREATE TABLE "augur_data"."repo_stats" (
  "repo_id" int8 NOT NULL,
  "rstat_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_stats_rstat_id_seq'::regclass),
  "rstat_name" varchar(400) COLLATE "pg_catalog"."default",
  "rstat_value" int8,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0),
  CONSTRAINT "repo_stats_pkey" PRIMARY KEY ("rstat_id", "repo_id")
);
ALTER TABLE "augur_data"."repo_stats" OWNER TO "augur";
COMMENT ON TABLE "augur_data"."repo_stats" IS 'Project Watchers';

CREATE TABLE "augur_data"."repo_test_coverage" (
  "repo_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_test_coverage_repo_id_seq'::regclass),
  "repo_clone_date" timestamp(0),
  "rtc_analysis_date" timestamp(0),
  "programming_language" varchar COLLATE "pg_catalog"."default",
  "file_path" varchar COLLATE "pg_catalog"."default",
  "file_name" varchar COLLATE "pg_catalog"."default",
  "testing_tool" varchar COLLATE "pg_catalog"."default",
  "file_statement_count" int8,
  "file_subroutine_count" int8,
  "file_statements_tested" int8,
  "file_subroutines_tested" int8,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_test_coverage_pkey" PRIMARY KEY ("repo_id")
);
ALTER TABLE "augur_data"."repo_test_coverage" OWNER TO "augur";

CREATE TABLE "augur_data"."repo_topic" (
  "repo_topic_id" int8 NOT NULL DEFAULT nextval('"augur_data".repo_topic_repo_topic_id_seq'::regclass),
  "repo_id" int4,
  "topic_id" int4,
  "topic_prob" float8,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "repo_topic_pkey" PRIMARY KEY ("repo_topic_id")
);
ALTER TABLE "augur_data"."repo_topic" OWNER TO "augur";

CREATE TABLE "augur_data"."repos_fetch_log" (
  "repos_id" int4 NOT NULL,
  "status" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "date" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."repos_fetch_log" OWNER TO "augur";
CREATE INDEX "repos_id,status" ON "augur_data"."repos_fetch_log" USING btree (
  "repos_id" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "status" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
CREATE INDEX "repos_id,statusops" ON "augur_data"."repos_fetch_log" USING btree (
  "repos_id" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "status" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."settings" (
  "id" int4 NOT NULL,
  "setting" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
  "value" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "last_modified" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "settings_pkey" PRIMARY KEY ("id")
);
ALTER TABLE "augur_data"."settings" OWNER TO "augur";

CREATE TABLE "augur_data"."topic_words" (
  "topic_words_id" int8 NOT NULL DEFAULT nextval('"augur_data".topic_words_topic_words_id_seq'::regclass),
  "topic_id" int8,
  "word" varchar COLLATE "pg_catalog"."default",
  "word_prob" float8,
  "tool_source" varchar COLLATE "pg_catalog"."default",
  "tool_version" varchar COLLATE "pg_catalog"."default",
  "data_source" varchar COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "topic_words_pkey" PRIMARY KEY ("topic_words_id")
);
ALTER TABLE "augur_data"."topic_words" OWNER TO "augur";

CREATE TABLE "augur_data"."unknown_cache" (
  "type" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "repo_group_id" int4 NOT NULL,
  "email" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "domain" varchar(128) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying,
  "added" int8 NOT NULL,
  "tool_source" varchar(255) COLLATE "pg_catalog"."default",
  "tool_version" varchar(255) COLLATE "pg_catalog"."default",
  "data_source" varchar(255) COLLATE "pg_catalog"."default",
  "data_collection_date" timestamp(0) DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_data"."unknown_cache" OWNER TO "augur";
CREATE INDEX "type,projects_id" ON "augur_data"."unknown_cache" USING btree (
  "type" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST,
  "repo_group_id" "pg_catalog"."int4_ops" ASC NULLS LAST
);

CREATE TABLE "augur_data"."utility_log" (
  "id" int8 NOT NULL DEFAULT nextval('"augur_data".utility_log_id_seq1'::regclass),
  "level" varchar(8) COLLATE "pg_catalog"."default" NOT NULL,
  "status" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "attempted" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "utility_log_pkey" PRIMARY KEY ("id")
);
ALTER TABLE "augur_data"."utility_log" OWNER TO "augur";

CREATE TABLE "augur_data"."working_commits" (
  "repos_id" int4 NOT NULL,
  "working_commit" varchar(40) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying
);
ALTER TABLE "augur_data"."working_commits" OWNER TO "augur";

CREATE TABLE "augur_operations"."all" (
  "Name" varchar COLLATE "pg_catalog"."default",
  "Bytes" varchar COLLATE "pg_catalog"."default",
  "Lines" varchar COLLATE "pg_catalog"."default",
  "Code" varchar COLLATE "pg_catalog"."default",
  "Comment" varchar COLLATE "pg_catalog"."default",
  "Blank" varchar COLLATE "pg_catalog"."default",
  "Complexity" varchar COLLATE "pg_catalog"."default",
  "Count" varchar COLLATE "pg_catalog"."default",
  "WeightedComplexity" varchar COLLATE "pg_catalog"."default",
  "Files" varchar COLLATE "pg_catalog"."default"
);
ALTER TABLE "augur_operations"."all" OWNER TO "augur";

CREATE TABLE "augur_operations"."augur_settings" (
  "id" int8 NOT NULL DEFAULT nextval('"augur_operations".augur_settings_id_seq'::regclass),
  "setting" varchar COLLATE "pg_catalog"."default",
  "value" varchar COLLATE "pg_catalog"."default",
  "last_modified" timestamp(0) DEFAULT CURRENT_DATE,
  CONSTRAINT "augur_settings_pkey" PRIMARY KEY ("id")
);
ALTER TABLE "augur_operations"."augur_settings" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."augur_settings" IS 'Augur settings include the schema version, and the Augur API Key as of 10/25/2020. Future augur settings may be stored in this table, which has the basic structure of a name-value pair. ';

CREATE TABLE "augur_operations"."repos_fetch_log" (
  "repos_id" int4 NOT NULL,
  "status" varchar(128) COLLATE "pg_catalog"."default" NOT NULL,
  "date" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE "augur_operations"."repos_fetch_log" OWNER TO "augur";
CREATE INDEX "repos_id,statusops" ON "augur_operations"."repos_fetch_log" USING btree (
  "repos_id" "pg_catalog"."int4_ops" ASC NULLS LAST,
  "status" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
COMMENT ON TABLE "augur_operations"."repos_fetch_log" IS 'For future use when we move all working tables to the augur_operations schema. ';

CREATE TABLE "augur_operations"."worker_history" (
  "history_id" int8 NOT NULL DEFAULT nextval('"augur_operations".gh_worker_history_history_id_seq'::regclass),
  "repo_id" int8,
  "worker" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "job_model" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "oauth_id" int4,
  "timestamp" timestamp(0) NOT NULL,
  "status" varchar(7) COLLATE "pg_catalog"."default" NOT NULL,
  "total_results" int4,
  CONSTRAINT "history_pkey" PRIMARY KEY ("history_id")
);
ALTER TABLE "augur_operations"."worker_history" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."worker_history" IS 'This table stores the complete history of job execution, including success and failure. It is useful for troubleshooting. ';

CREATE TABLE "augur_operations"."worker_job" (
  "job_model" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "state" int4 NOT NULL DEFAULT 0,
  "zombie_head" int4,
  "since_id_str" varchar(255) COLLATE "pg_catalog"."default" NOT NULL DEFAULT '0'::character varying,
  "description" varchar(255) COLLATE "pg_catalog"."default" DEFAULT 'None'::character varying,
  "last_count" int4,
  "last_run" timestamp(0) DEFAULT NULL::timestamp without time zone,
  "analysis_state" int4 DEFAULT 0,
  "oauth_id" int4 NOT NULL,
  CONSTRAINT "job_pkey" PRIMARY KEY ("job_model")
);
ALTER TABLE "augur_operations"."worker_job" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."worker_job" IS 'This table stores the jobs workers collect data for. A job is found in the code, and in the augur.config.json under the construct of a “model”. ';

CREATE TABLE "augur_operations"."worker_oauth" (
  "oauth_id" int8 NOT NULL DEFAULT nextval('"augur_operations".worker_oauth_oauth_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "consumer_key" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "consumer_secret" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "access_token" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "access_token_secret" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "repo_directory" varchar COLLATE "pg_catalog"."default",
  "platform" varchar COLLATE "pg_catalog"."default" DEFAULT 'github'::character varying,
  CONSTRAINT "worker_oauth_pkey" PRIMARY KEY ("oauth_id")
);
ALTER TABLE "augur_operations"."worker_oauth" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."worker_oauth" IS 'This table stores credentials for retrieving data from platform API’s. Entries in this table must comply with the terms of service for each platform. ';

CREATE TABLE "augur_operations"."worker_settings_facade" (
  "id" int4 NOT NULL,
  "setting" varchar(32) COLLATE "pg_catalog"."default" NOT NULL,
  "value" varchar COLLATE "pg_catalog"."default" NOT NULL,
  "last_modified" timestamp(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT "settings_pkey" PRIMARY KEY ("id")
);
ALTER TABLE "augur_operations"."worker_settings_facade" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."worker_settings_facade" IS 'For future use when we move all working tables to the augur_operations schema. ';

CREATE TABLE "augur_operations"."working_commits" (
  "repos_id" int4 NOT NULL,
  "working_commit" varchar(40) COLLATE "pg_catalog"."default" DEFAULT 'NULL'::character varying
);
ALTER TABLE "augur_operations"."working_commits" OWNER TO "augur";
COMMENT ON TABLE "augur_operations"."working_commits" IS 'For future use when we move all working tables to the augur_operations schema. ';

CREATE TABLE "spdx"."annotation_types" (
  "annotation_type_id" int4 NOT NULL DEFAULT nextval('"spdx".annotation_types_annotation_type_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "annotation_types_pkey" PRIMARY KEY ("annotation_type_id"),
  CONSTRAINT "uc_annotation_type_name" UNIQUE ("name")
);
ALTER TABLE "spdx"."annotation_types" OWNER TO "augur";

CREATE TABLE "spdx"."annotations" (
  "annotation_id" int4 NOT NULL DEFAULT nextval('"spdx".annotations_annotation_id_seq'::regclass),
  "document_id" int4 NOT NULL,
  "annotation_type_id" int4 NOT NULL,
  "identifier_id" int4 NOT NULL,
  "creator_id" int4 NOT NULL,
  "created_ts" timestamptz(6),
  "comment" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "annotations_pkey" PRIMARY KEY ("annotation_id")
);
ALTER TABLE "spdx"."annotations" OWNER TO "augur";

CREATE TABLE "spdx"."augur_repo_map" (
  "map_id" int4 NOT NULL DEFAULT nextval('"spdx".augur_repo_map_map_id_seq'::regclass),
  "dosocs_pkg_id" int4,
  "dosocs_pkg_name" text COLLATE "pg_catalog"."default",
  "repo_id" int4,
  "repo_path" text COLLATE "pg_catalog"."default",
  CONSTRAINT "augur_repo_map_pkey" PRIMARY KEY ("map_id")
);
ALTER TABLE "spdx"."augur_repo_map" OWNER TO "augur";

CREATE TABLE "spdx"."creator_types" (
  "creator_type_id" int4 NOT NULL DEFAULT nextval('"spdx".creator_types_creator_type_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "creator_types_pkey" PRIMARY KEY ("creator_type_id")
);
ALTER TABLE "spdx"."creator_types" OWNER TO "augur";

CREATE TABLE "spdx"."creators" (
  "creator_id" int4 NOT NULL DEFAULT nextval('"spdx".creators_creator_id_seq'::regclass),
  "creator_type_id" int4 NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "email" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "creators_pkey" PRIMARY KEY ("creator_id")
);
ALTER TABLE "spdx"."creators" OWNER TO "augur";

CREATE TABLE "spdx"."document_namespaces" (
  "document_namespace_id" int4 NOT NULL DEFAULT nextval('"spdx".document_namespaces_document_namespace_id_seq'::regclass),
  "uri" varchar(500) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "document_namespaces_pkey" PRIMARY KEY ("document_namespace_id"),
  CONSTRAINT "uc_document_namespace_uri" UNIQUE ("uri")
);
ALTER TABLE "spdx"."document_namespaces" OWNER TO "augur";

CREATE TABLE "spdx"."documents" (
  "document_id" int4 NOT NULL DEFAULT nextval('"spdx".documents_document_id_seq'::regclass),
  "document_namespace_id" int4 NOT NULL,
  "data_license_id" int4 NOT NULL,
  "spdx_version" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "license_list_version" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "created_ts" timestamptz(6) NOT NULL,
  "creator_comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "document_comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "package_id" int4 NOT NULL,
  CONSTRAINT "documents_pkey" PRIMARY KEY ("document_id"),
  CONSTRAINT "uc_document_document_namespace_id" UNIQUE ("document_namespace_id")
);
ALTER TABLE "spdx"."documents" OWNER TO "augur";

CREATE TABLE "spdx"."documents_creators" (
  "document_creator_id" int4 NOT NULL DEFAULT nextval('"spdx".documents_creators_document_creator_id_seq'::regclass),
  "document_id" int4 NOT NULL,
  "creator_id" int4 NOT NULL,
  CONSTRAINT "documents_creators_pkey" PRIMARY KEY ("document_creator_id")
);
ALTER TABLE "spdx"."documents_creators" OWNER TO "augur";

CREATE TABLE "spdx"."external_refs" (
  "external_ref_id" int4 NOT NULL DEFAULT nextval('"spdx".external_refs_external_ref_id_seq'::regclass),
  "document_id" int4 NOT NULL,
  "document_namespace_id" int4 NOT NULL,
  "id_string" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "sha256" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "external_refs_pkey" PRIMARY KEY ("external_ref_id"),
  CONSTRAINT "uc_external_ref_document_id_string" UNIQUE ("document_id", "id_string")
);
ALTER TABLE "spdx"."external_refs" OWNER TO "augur";

CREATE TABLE "spdx"."file_contributors" (
  "file_contributor_id" int4 NOT NULL DEFAULT nextval('"spdx".file_contributors_file_contributor_id_seq'::regclass),
  "file_id" int4 NOT NULL,
  "contributor" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "file_contributors_pkey" PRIMARY KEY ("file_contributor_id")
);
ALTER TABLE "spdx"."file_contributors" OWNER TO "augur";

CREATE TABLE "spdx"."file_types" (
  "file_type_id" int4,
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "uc_file_type_name" PRIMARY KEY ("name")
);
ALTER TABLE "spdx"."file_types" OWNER TO "augur";

CREATE TABLE "spdx"."files" (
  "file_id" int4 NOT NULL DEFAULT nextval('"spdx".files_file_id_seq'::regclass),
  "file_type_id" int4,
  "sha256" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "copyright_text" text COLLATE "pg_catalog"."default",
  "package_id" int4,
  "comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "notice" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "files_pkey" PRIMARY KEY ("file_id"),
  CONSTRAINT "uc_file_sha256" UNIQUE ("sha256")
);
ALTER TABLE "spdx"."files" OWNER TO "augur";

CREATE TABLE "spdx"."files_licenses" (
  "file_license_id" int4 NOT NULL DEFAULT nextval('"spdx".files_licenses_file_license_id_seq'::regclass),
  "file_id" int4 NOT NULL,
  "license_id" int4 NOT NULL,
  "extracted_text" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "files_licenses_pkey" PRIMARY KEY ("file_license_id"),
  CONSTRAINT "uc_file_license" UNIQUE ("file_id", "license_id")
);
ALTER TABLE "spdx"."files_licenses" OWNER TO "augur";

CREATE TABLE "spdx"."files_scans" (
  "file_scan_id" int4 NOT NULL DEFAULT nextval('"spdx".files_scans_file_scan_id_seq'::regclass),
  "file_id" int4 NOT NULL,
  "scanner_id" int4 NOT NULL,
  CONSTRAINT "files_scans_pkey" PRIMARY KEY ("file_scan_id"),
  CONSTRAINT "uc_file_scanner_id" UNIQUE ("file_id", "scanner_id")
);
ALTER TABLE "spdx"."files_scans" OWNER TO "augur";

CREATE TABLE "spdx"."identifiers" (
  "identifier_id" int4 NOT NULL DEFAULT nextval('"spdx".identifiers_identifier_id_seq'::regclass),
  "document_namespace_id" int4 NOT NULL,
  "id_string" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "document_id" int4,
  "package_id" int4,
  "package_file_id" int4,
  CONSTRAINT "identifiers_pkey" PRIMARY KEY ("identifier_id"),
  CONSTRAINT "uc_identifier_document_namespace_id" UNIQUE ("document_namespace_id", "id_string"),
  CONSTRAINT "uc_identifier_namespace_document_id" UNIQUE ("document_namespace_id", "document_id"),
  CONSTRAINT "uc_identifier_namespace_package_file_id" UNIQUE ("document_namespace_id", "package_file_id"),
  CONSTRAINT "uc_identifier_namespace_package_id" UNIQUE ("document_namespace_id", "package_id"),
  CONSTRAINT "ck_identifier_exactly_one" CHECK (((document_id IS NOT NULL)::integer + (package_id IS NOT NULL)::integer + (package_file_id IS NOT NULL)::integer) = 1)
);
ALTER TABLE "spdx"."identifiers" OWNER TO "augur";

CREATE TABLE "spdx"."licenses" (
  "license_id" int4 NOT NULL DEFAULT nextval('"spdx".licenses_license_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default",
  "short_name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "cross_reference" text COLLATE "pg_catalog"."default" NOT NULL,
  "comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "is_spdx_official" bool NOT NULL,
  CONSTRAINT "licenses_pkey" PRIMARY KEY ("license_id"),
  CONSTRAINT "uc_license_short_name" UNIQUE ("short_name")
);
ALTER TABLE "spdx"."licenses" OWNER TO "augur";

CREATE TABLE "spdx"."packages" (
  "package_id" int4 NOT NULL DEFAULT nextval('"spdx".packages_package_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "version" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  "file_name" text COLLATE "pg_catalog"."default" NOT NULL,
  "supplier_id" int4,
  "originator_id" int4,
  "download_location" text COLLATE "pg_catalog"."default",
  "verification_code" varchar(64) COLLATE "pg_catalog"."default" NOT NULL,
  "ver_code_excluded_file_id" int4,
  "sha256" varchar(64) COLLATE "pg_catalog"."default",
  "home_page" text COLLATE "pg_catalog"."default",
  "source_info" text COLLATE "pg_catalog"."default" NOT NULL,
  "concluded_license_id" int4,
  "declared_license_id" int4,
  "license_comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "copyright_text" text COLLATE "pg_catalog"."default",
  "summary" text COLLATE "pg_catalog"."default" NOT NULL,
  "description" text COLLATE "pg_catalog"."default" NOT NULL,
  "comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "dosocs2_dir_code" varchar(64) COLLATE "pg_catalog"."default",
  CONSTRAINT "packages_pkey" PRIMARY KEY ("package_id"),
  CONSTRAINT "uc_dir_code_ver_code" UNIQUE ("verification_code", "dosocs2_dir_code"),
  CONSTRAINT "uc_package_sha256" UNIQUE ("sha256"),
  CONSTRAINT "uc_sha256_ds2_dir_code_exactly_one" CHECK (((sha256 IS NOT NULL)::integer + (dosocs2_dir_code IS NOT NULL)::integer) = 1)
);
ALTER TABLE "spdx"."packages" OWNER TO "augur";

CREATE TABLE "spdx"."packages_files" (
  "package_file_id" int4 NOT NULL DEFAULT nextval('"spdx".packages_files_package_file_id_seq'::regclass),
  "package_id" int4 NOT NULL,
  "file_id" int4 NOT NULL,
  "concluded_license_id" int4,
  "license_comment" text COLLATE "pg_catalog"."default" NOT NULL,
  "file_name" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "packages_files_pkey" PRIMARY KEY ("package_file_id"),
  CONSTRAINT "uc_package_id_file_name" UNIQUE ("package_id", "file_name")
);
ALTER TABLE "spdx"."packages_files" OWNER TO "augur";

CREATE TABLE "spdx"."packages_scans" (
  "package_scan_id" int4 NOT NULL DEFAULT nextval('"spdx".packages_scans_package_scan_id_seq'::regclass),
  "package_id" int4 NOT NULL,
  "scanner_id" int4 NOT NULL,
  CONSTRAINT "packages_scans_pkey" PRIMARY KEY ("package_scan_id"),
  CONSTRAINT "uc_package_scanner_id" UNIQUE ("package_id", "scanner_id")
);
ALTER TABLE "spdx"."packages_scans" OWNER TO "augur";

CREATE TABLE "spdx"."projects" (
  "package_id" int4 NOT NULL DEFAULT nextval('"spdx".projects_package_id_seq'::regclass),
  "name" text COLLATE "pg_catalog"."default" NOT NULL,
  "homepage" text COLLATE "pg_catalog"."default" NOT NULL,
  "uri" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "projects_pkey" PRIMARY KEY ("package_id")
);
ALTER TABLE "spdx"."projects" OWNER TO "augur";

CREATE TABLE "spdx"."relationship_types" (
  "relationship_type_id" int4 NOT NULL DEFAULT nextval('"spdx".relationship_types_relationship_type_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "relationship_types_pkey" PRIMARY KEY ("relationship_type_id"),
  CONSTRAINT "uc_relationship_type_name" UNIQUE ("name")
);
ALTER TABLE "spdx"."relationship_types" OWNER TO "augur";

CREATE TABLE "spdx"."relationships" (
  "relationship_id" int4 NOT NULL DEFAULT nextval('"spdx".relationships_relationship_id_seq'::regclass),
  "left_identifier_id" int4 NOT NULL,
  "right_identifier_id" int4 NOT NULL,
  "relationship_type_id" int4 NOT NULL,
  "relationship_comment" text COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "relationships_pkey" PRIMARY KEY ("relationship_id"),
  CONSTRAINT "uc_left_right_relationship_type" UNIQUE ("left_identifier_id", "right_identifier_id", "relationship_type_id")
);
ALTER TABLE "spdx"."relationships" OWNER TO "augur";

CREATE TABLE "spdx"."sbom_scans" (
  "repo_id" int4,
  "sbom_scan" json
);
ALTER TABLE "spdx"."sbom_scans" OWNER TO "augur";

CREATE TABLE "spdx"."scanners" (
  "scanner_id" int4 NOT NULL DEFAULT nextval('"spdx".scanners_scanner_id_seq'::regclass),
  "name" varchar(255) COLLATE "pg_catalog"."default" NOT NULL,
  CONSTRAINT "scanners_pkey" PRIMARY KEY ("scanner_id"),
  CONSTRAINT "uc_scanner_name" UNIQUE ("name")
);
ALTER TABLE "spdx"."scanners" OWNER TO "augur";

ALTER TABLE "augur_data"."commit_comment_ref" ADD CONSTRAINT "fk_commit_comment_ref_commits_1" FOREIGN KEY ("cmt_id") REFERENCES "augur_data"."commits" ("cmt_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."commit_comment_ref" ADD CONSTRAINT "fk_commit_comment_ref_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."commit_parents" ADD CONSTRAINT "fk_commit_parents_commits_1" FOREIGN KEY ("cmt_id") REFERENCES "augur_data"."commits" ("cmt_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."commit_parents" ADD CONSTRAINT "fk_commit_parents_commits_2" FOREIGN KEY ("parent_id") REFERENCES "augur_data"."commits" ("cmt_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."commits" ADD CONSTRAINT "fk_commits_contributors_1" FOREIGN KEY ("cmt_ght_author_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE;
ALTER TABLE "augur_data"."commits" ADD CONSTRAINT "fk_commits_contributors_2" FOREIGN KEY ("cmt_ght_committer_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE;
ALTER TABLE "augur_data"."commits" ADD CONSTRAINT "fk_commits_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."contributor_repo" ADD CONSTRAINT "fk_contributor_repo_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE;
ALTER TABLE "augur_data"."contributors_aliases" ADD CONSTRAINT "fk_alias_id" FOREIGN KEY ("cntrb_a_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."contributors_aliases" ADD CONSTRAINT "fk_contributors_aliases_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE CASCADE ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."contributors_history" ADD CONSTRAINT "fk_contributors_history_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."discourse_insights" ADD CONSTRAINT "fk_discourse_insights_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."issue_assignees" ADD CONSTRAINT "fk_issue_assignees_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issue_assignees" ADD CONSTRAINT "fk_issue_assignees_issues_1" FOREIGN KEY ("issue_id") REFERENCES "augur_data"."issues" ("issue_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issue_events" ADD CONSTRAINT "fk_issue_events_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issue_events" ADD CONSTRAINT "fk_issue_events_issues_1" FOREIGN KEY ("issue_id") REFERENCES "augur_data"."issues" ("issue_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issue_labels" ADD CONSTRAINT "fk_issue_labels_issues_1" FOREIGN KEY ("issue_id") REFERENCES "augur_data"."issues" ("issue_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."issue_message_ref" ADD CONSTRAINT "fk_issue_message_ref_issues_1" FOREIGN KEY ("issue_id") REFERENCES "augur_data"."issues" ("issue_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."issue_message_ref" ADD CONSTRAINT "fk_issue_message_ref_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."issues" ADD CONSTRAINT "fk_issues_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issues" ADD CONSTRAINT "fk_issues_contributors_2" FOREIGN KEY ("reporter_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."issues" ADD CONSTRAINT "fk_issues_repo" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."libraries" ADD CONSTRAINT "fk_libraries_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."library_dependencies" ADD CONSTRAINT "fk_library_dependencies_libraries_1" FOREIGN KEY ("library_id") REFERENCES "augur_data"."libraries" ("library_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."library_version" ADD CONSTRAINT "fk_library_version_libraries_1" FOREIGN KEY ("library_id") REFERENCES "augur_data"."libraries" ("library_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."lstm_anomaly_results" ADD CONSTRAINT "fk_lstm_anomaly_results_lstm_anomaly_models_1" FOREIGN KEY ("model_id") REFERENCES "augur_data"."lstm_anomaly_models" ("model_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."lstm_anomaly_results" ADD CONSTRAINT "fk_lstm_anomaly_results_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."message" ADD CONSTRAINT "fk_message_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."message" ADD CONSTRAINT "fk_message_platform_1" FOREIGN KEY ("pltfrm_id") REFERENCES "augur_data"."platform" ("pltfrm_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."message" ADD CONSTRAINT "fk_message_repo_groups_list_serve_1" FOREIGN KEY ("rgls_id") REFERENCES "augur_data"."repo_groups_list_serve" ("rgls_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."message_analysis" ADD CONSTRAINT "fk_message_analysis_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."message_analysis_summary" ADD CONSTRAINT "fk_message_analysis_summary_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."message_sentiment" ADD CONSTRAINT "fk_message_sentiment_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."message_sentiment_summary" ADD CONSTRAINT "fk_message_sentiment_summary_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."pull_request_analysis" ADD CONSTRAINT "fk_pull_request_analysis_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_assignees" ADD CONSTRAINT "fk_pull_request_assignees_contributors_1" FOREIGN KEY ("contrib_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_assignees" ADD CONSTRAINT "fk_pull_request_assignees_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_commits" ADD CONSTRAINT "fk_pr_commit_cntrb_id" FOREIGN KEY ("pr_cmt_author_cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE NO ACTION ON UPDATE NO ACTION DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_commits" ADD CONSTRAINT "fk_pull_request_commits_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_events" ADD CONSTRAINT "fk_pull_request_events_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_events" ADD CONSTRAINT "fk_pull_request_events_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_files" ADD CONSTRAINT "fk_pull_request_commits_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_labels" ADD CONSTRAINT "fk_pull_request_labels_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_message_ref" ADD CONSTRAINT "fk_pull_request_message_ref_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_message_ref" ADD CONSTRAINT "fk_pull_request_message_ref_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_meta" ADD CONSTRAINT "fk_pull_request_meta_contributors_2" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_meta" ADD CONSTRAINT "fk_pull_request_meta_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_repo" ADD CONSTRAINT "fk_pull_request_repo_contributors_1" FOREIGN KEY ("pr_cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_repo" ADD CONSTRAINT "fk_pull_request_repo_pull_request_meta_1" FOREIGN KEY ("pr_repo_meta_id") REFERENCES "augur_data"."pull_request_meta" ("pr_repo_meta_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_review_message_ref" ADD CONSTRAINT "fk_pull_request_review_message_ref_message_1" FOREIGN KEY ("msg_id") REFERENCES "augur_data"."message" ("msg_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."pull_request_review_message_ref" ADD CONSTRAINT "fk_pull_request_review_message_ref_pull_request_reviews_1" FOREIGN KEY ("pr_review_id") REFERENCES "augur_data"."pull_request_reviews" ("pr_review_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_request_reviewers" ADD CONSTRAINT "fk_pull_request_reviewers_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_reviewers" ADD CONSTRAINT "fk_pull_request_reviewers_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_reviews" ADD CONSTRAINT "fk_pull_request_reviews_contributors_1" FOREIGN KEY ("cntrb_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_reviews" ADD CONSTRAINT "fk_pull_request_reviews_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_request_teams" ADD CONSTRAINT "fk_pull_request_teams_pull_requests_1" FOREIGN KEY ("pull_request_id") REFERENCES "augur_data"."pull_requests" ("pull_request_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."pull_requests" ADD CONSTRAINT "fk_pr_contribs" FOREIGN KEY ("pr_augur_contributor_id") REFERENCES "augur_data"."contributors" ("cntrb_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."pull_requests" ADD CONSTRAINT "fk_pull_requests_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE RESTRICT ON UPDATE CASCADE DEFERRABLE;
ALTER TABLE "augur_data"."releases" ADD CONSTRAINT "fk_releases_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo" ADD CONSTRAINT "fk_repo_repo_groups_1" FOREIGN KEY ("repo_group_id") REFERENCES "augur_data"."repo_groups" ("repo_group_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMENT ON CONSTRAINT "fk_repo_repo_groups_1" ON "augur_data"."repo" IS 'Repo_groups cardinality set to one and only one because, although in theory there could be more than one repo group for a repo, this might create dependencies in hosted situation that we do not want to live with. ';
ALTER TABLE "augur_data"."repo_badging" ADD CONSTRAINT "fk_repo_badging_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_cluster_messages" ADD CONSTRAINT "fk_repo_cluster_messages_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_dependencies" ADD CONSTRAINT "repo_id" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_deps_scorecard" ADD CONSTRAINT "repo_id" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_group_insights" ADD CONSTRAINT "fk_repo_group_insights_repo_groups_1" FOREIGN KEY ("repo_group_id") REFERENCES "augur_data"."repo_groups" ("repo_group_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_groups_list_serve" ADD CONSTRAINT "fk_repo_groups_list_serve_repo_groups_1" FOREIGN KEY ("repo_group_id") REFERENCES "augur_data"."repo_groups" ("repo_group_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_info" ADD CONSTRAINT "fk_repo_info_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_insights" ADD CONSTRAINT "fk_repo_insights_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_insights_records" ADD CONSTRAINT "repo_id_ref" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE SET NULL ON UPDATE CASCADE;
ALTER TABLE "augur_data"."repo_labor" ADD CONSTRAINT "fk_repo_labor_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_meta" ADD CONSTRAINT "fk_repo_meta_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_sbom_scans" ADD CONSTRAINT "repo_linker_sbom" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "augur_data"."repo_stats" ADD CONSTRAINT "fk_repo_stats_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_test_coverage" ADD CONSTRAINT "fk_repo_test_coverage_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "augur_data"."repo_topic" ADD CONSTRAINT "fk_repo_topic_repo_1" FOREIGN KEY ("repo_id") REFERENCES "augur_data"."repo" ("repo_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."annotations" ADD CONSTRAINT "annotations_annotation_type_id_fkey" FOREIGN KEY ("annotation_type_id") REFERENCES "spdx"."annotation_types" ("annotation_type_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."annotations" ADD CONSTRAINT "annotations_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "spdx"."creators" ("creator_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."annotations" ADD CONSTRAINT "annotations_document_id_fkey" FOREIGN KEY ("document_id") REFERENCES "spdx"."documents" ("document_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."annotations" ADD CONSTRAINT "annotations_identifier_id_fkey" FOREIGN KEY ("identifier_id") REFERENCES "spdx"."identifiers" ("identifier_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."creators" ADD CONSTRAINT "creators_creator_type_id_fkey" FOREIGN KEY ("creator_type_id") REFERENCES "spdx"."creator_types" ("creator_type_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."documents" ADD CONSTRAINT "documents_data_license_id_fkey" FOREIGN KEY ("data_license_id") REFERENCES "spdx"."licenses" ("license_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."documents" ADD CONSTRAINT "documents_document_namespace_id_fkey" FOREIGN KEY ("document_namespace_id") REFERENCES "spdx"."document_namespaces" ("document_namespace_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."documents" ADD CONSTRAINT "documents_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "spdx"."packages" ("package_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."documents_creators" ADD CONSTRAINT "documents_creators_creator_id_fkey" FOREIGN KEY ("creator_id") REFERENCES "spdx"."creators" ("creator_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."documents_creators" ADD CONSTRAINT "documents_creators_document_id_fkey" FOREIGN KEY ("document_id") REFERENCES "spdx"."documents" ("document_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."external_refs" ADD CONSTRAINT "external_refs_document_id_fkey" FOREIGN KEY ("document_id") REFERENCES "spdx"."documents" ("document_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."external_refs" ADD CONSTRAINT "external_refs_document_namespace_id_fkey" FOREIGN KEY ("document_namespace_id") REFERENCES "spdx"."document_namespaces" ("document_namespace_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."file_contributors" ADD CONSTRAINT "file_contributors_file_id_fkey" FOREIGN KEY ("file_id") REFERENCES "spdx"."files" ("file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."files_licenses" ADD CONSTRAINT "files_licenses_file_id_fkey" FOREIGN KEY ("file_id") REFERENCES "spdx"."files" ("file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."files_licenses" ADD CONSTRAINT "files_licenses_license_id_fkey" FOREIGN KEY ("license_id") REFERENCES "spdx"."licenses" ("license_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."files_scans" ADD CONSTRAINT "files_scans_file_id_fkey" FOREIGN KEY ("file_id") REFERENCES "spdx"."files" ("file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."files_scans" ADD CONSTRAINT "files_scans_scanner_id_fkey" FOREIGN KEY ("scanner_id") REFERENCES "spdx"."scanners" ("scanner_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."identifiers" ADD CONSTRAINT "identifiers_document_id_fkey" FOREIGN KEY ("document_id") REFERENCES "spdx"."documents" ("document_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."identifiers" ADD CONSTRAINT "identifiers_document_namespace_id_fkey" FOREIGN KEY ("document_namespace_id") REFERENCES "spdx"."document_namespaces" ("document_namespace_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."identifiers" ADD CONSTRAINT "identifiers_package_file_id_fkey" FOREIGN KEY ("package_file_id") REFERENCES "spdx"."packages_files" ("package_file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."identifiers" ADD CONSTRAINT "identifiers_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "spdx"."packages" ("package_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages" ADD CONSTRAINT "fk_package_packages_files" FOREIGN KEY ("ver_code_excluded_file_id") REFERENCES "spdx"."packages_files" ("package_file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages" ADD CONSTRAINT "packages_concluded_license_id_fkey" FOREIGN KEY ("concluded_license_id") REFERENCES "spdx"."licenses" ("license_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages" ADD CONSTRAINT "packages_declared_license_id_fkey" FOREIGN KEY ("declared_license_id") REFERENCES "spdx"."licenses" ("license_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages" ADD CONSTRAINT "packages_originator_id_fkey" FOREIGN KEY ("originator_id") REFERENCES "spdx"."creators" ("creator_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages" ADD CONSTRAINT "packages_supplier_id_fkey" FOREIGN KEY ("supplier_id") REFERENCES "spdx"."creators" ("creator_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages_files" ADD CONSTRAINT "fk_package_files_packages" FOREIGN KEY ("package_id") REFERENCES "spdx"."packages" ("package_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages_files" ADD CONSTRAINT "packages_files_concluded_license_id_fkey" FOREIGN KEY ("concluded_license_id") REFERENCES "spdx"."licenses" ("license_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages_files" ADD CONSTRAINT "packages_files_file_id_fkey" FOREIGN KEY ("file_id") REFERENCES "spdx"."files" ("file_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages_scans" ADD CONSTRAINT "packages_scans_package_id_fkey" FOREIGN KEY ("package_id") REFERENCES "spdx"."packages" ("package_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."packages_scans" ADD CONSTRAINT "packages_scans_scanner_id_fkey" FOREIGN KEY ("scanner_id") REFERENCES "spdx"."scanners" ("scanner_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."relationships" ADD CONSTRAINT "relationships_left_identifier_id_fkey" FOREIGN KEY ("left_identifier_id") REFERENCES "spdx"."identifiers" ("identifier_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."relationships" ADD CONSTRAINT "relationships_relationship_type_id_fkey" FOREIGN KEY ("relationship_type_id") REFERENCES "spdx"."relationship_types" ("relationship_type_id") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "spdx"."relationships" ADD CONSTRAINT "relationships_right_identifier_id_fkey" FOREIGN KEY ("right_identifier_id") REFERENCES "spdx"."identifiers" ("identifier_id") ON DELETE NO ACTION ON UPDATE NO ACTION;




-- #SPDX-License-Identifier: MIT
BEGIN;
INSERT INTO "augur_data"."platform" VALUES (25150, 'GitHub', '3', '2019-06-05', 'Manual Entry', 'Sean Goggins', 'GitHub', '2019-06-05 17:23:42');
INSERT INTO "augur_data"."platform" VALUES (25151, 'GitLab', '3', '2019-06-05', 'Manual Entry', 'Sean Goggins', 'GitHub', '2019-06-05 17:23:42');

COMMIT;

BEGIN; 
INSERT INTO "augur_data"."contributors"("cntrb_id", "cntrb_login", "cntrb_email", "cntrb_company", "cntrb_created_at", "cntrb_type", "cntrb_fake", "cntrb_deleted", "cntrb_long", "cntrb_lat", "cntrb_country_code", "cntrb_state", "cntrb_city", "cntrb_location", "cntrb_canonical", "gh_user_id", "gh_login", "gh_url", "gh_html_url", "gh_node_id", "gh_avatar_url", "gh_gravatar_id", "gh_followers_url", "gh_following_url", "gh_gists_url", "gh_starred_url", "gh_subscriptions_url", "gh_organizations_url", "gh_repos_url", "gh_events_url", "gh_received_events_url", "gh_type", "gh_site_admin", "tool_source", "tool_version", "data_source", "data_collection_date") VALUES (1, 'not-provided', NULL, NULL, '2019-06-13 11:33:39', NULL, 0, 0, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, 'nobody', 'http://fake.me', 'http://fake.me', 'x', 'http://fake.me', NULL, 'http://fake.me', 'http://fake.me', 'http://fake.me', 'http://fake.me', 'http://fake.me', 'http://fake.me', 'http://fake.me', 'http://fake.me', NULL, NULL, NULL, NULL, NULL, NULL, '2019-06-13 16:35:25');

INSERT INTO "augur_data"."repo_groups"("repo_group_id", "rg_name", "rg_description", "rg_website", "rg_recache", "rg_last_modified", "rg_type", "tool_source", "tool_version", "data_source", "data_collection_date") VALUES (1, 'Default Repo Group', 'The default repo group created by the schema generation script', '', 0, '2019-06-03 15:55:20', 'GitHub Organization', 'load', 'one', 'git', '2019-06-05 13:36:25');
INSERT INTO "augur_data"."repo"("repo_id", "repo_group_id", "repo_git", "repo_path", "repo_name", "repo_added", "repo_status", "repo_type", "url", "owner_id", "description", "primary_language", "created_at", "forked_from", "updated_at", "tool_source", "tool_version", "data_source", "data_collection_date") VALUES (1, 1, 'https://github.com/chaoss/augur.git', 'github.com/chaoss/', 'augur', '2019-05-31 14:28:44', 'New', '', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'data load', 'one', 'git', '2019-06-05 18:41:14');

INSERT INTO "augur_operations"."augur_settings"("id", "setting", "value", "last_modified") VALUES (1, 'augur_data_version', '60', '2021-07-12 18:41:00');

COMMIT; 

-- ----------------------------
-- Records of settings
-- ----------------------------
BEGIN;
INSERT INTO "augur_data"."settings" VALUES (5, 'report_date', 'committer', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (6, 'report_attribution', 'author', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (10, 'google_analytics', 'disabled', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (11, 'update_frequency', '24', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (12, 'database_version', '7', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (13, 'results_visibility', 'show', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (1, 'start_date', '2001-01-01', '1900-01-22 20:34:51');
INSERT INTO "augur_data"."settings" VALUES (4, 'log_level', 'Debug', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (2, 'repo_directory', '/augur/repos/', '2019-05-07 12:47:26');
INSERT INTO "augur_data"."settings" VALUES (8, 'affiliations_processed', '2001-08-26 10:03:29.815013+00', '1900-01-22 20:36:27');
INSERT INTO "augur_data"."settings" VALUES (9, 'aliases_processed', '2001-08-26 10:03:29.815013+00', '1900-01-22 20:36:27');
INSERT INTO "augur_data"."settings" VALUES (7, 'working_author', 'done', '1900-01-22 20:23:43');
INSERT INTO "augur_data"."settings" VALUES (3, 'utility_status', 'Idle', '1900-01-22 20:38:07');

COMMIT;



-- ----------------------------
-- Records of chaoss_metric_status
-- ----------------------------
BEGIN;
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (2, 'growth-maturity-decline', 'githubapi', 'timeseries', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/timeseries/githubapi/issues', NULL, 'Open Issues', 'growth-maturity-decline', '"open-issues"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:41:41', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (3, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/issues', NULL, 'Open Issues', 'growth-maturity-decline', '"open-issues"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:42:15', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (4, 'growth-maturity-decline', 'githubapi', 'timeseries', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/timeseries/githubapi/issues/closed', NULL, 'Closed Issues', 'growth-maturity-decline', '"closed-issues"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:45:53', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (5, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/issues/closed', NULL, 'Closed Issues', 'growth-maturity-decline', '"closed-issues"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:26', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (6, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/issues/response_time', NULL, 'First Response To Issue Duration', 'growth-maturity-decline', '"first-response-to-issue-duration"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:27', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (7, 'growth-maturity-decline', 'githubapi', 'timeseries', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/timeseries/githubapi/commits', NULL, 'Code Commits', 'growth-maturity-decline', '"code-commits"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:49:29', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (8, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/commits', NULL, 'Code Commits', 'growth-maturity-decline', '"code-commits"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:30', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (9, 'growth-maturity-decline', 'githubapi', 'metric', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/lines_changed', NULL, 'Lines Of Code Changed', 'growth-maturity-decline', '"lines-of-code-changed"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:49:32', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (10, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/pulls/maintainer_response_time', NULL, 'Maintainer Response To Merge Request Duration', 'growth-maturity-decline', '"maintainer-response-to-merge-request-duration"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:33', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (11, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/code_review_iteration', NULL, 'Code Review Iteration', 'growth-maturity-decline', '"code-review-iteration"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:35', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (12, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/forks', NULL, 'Forks', 'growth-maturity-decline', '"forks"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:36', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (13, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/pulls', NULL, 'Pull Requests Open', 'growth-maturity-decline', '"pull-requests-open"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:38', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (14, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/pulls/closed', NULL, 'Pull Requests Closed', 'growth-maturity-decline', '"pull-requests-closed"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:39', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (15, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/pulls/response_time', NULL, 'Pull Request Comment Duration', 'growth-maturity-decline', '"pull-request-comment-duration"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:41', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (16, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/pulls/comments', NULL, 'Pull Request Comments', 'growth-maturity-decline', '"pull-request-comments"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:42', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (17, 'growth-maturity-decline', 'augur_db', 'metric', 'implemented', 'unimplemented', 't', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/contributors', NULL, 'Contributors', 'growth-maturity-decline', '"contributors"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:44', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (18, 'growth-maturity-decline', 'githubapi', 'metric', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/githubapi/contributors', NULL, 'Contributors', 'growth-maturity-decline', '"contributors"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:49:45', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (19, 'growth-maturity-decline', 'ghtorrent', 'metric', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/contributors', NULL, 'Contributors', 'growth-maturity-decline', '"contributors"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:47', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (20, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/community_engagement', NULL, 'Community Engagement', 'growth-maturity-decline', '"community-engagement"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:48', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (21, 'growth-maturity-decline', 'augur_db', 'metric', 'implemented', 'unimplemented', 't', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/sub-projects', NULL, 'Sub Projects', 'growth-maturity-decline', '"sub-projects"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:50', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (22, 'growth-maturity-decline', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/contribution_acceptance', NULL, 'Contribution Acceptance', 'growth-maturity-decline', '"contribution-acceptance"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:49:51', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (23, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/code-changes', NULL, 'Code Changes', 'experimental', '"code-changes"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:53', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (24, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/pull-requests-merge-contributor-new', NULL, 'Pull Requests Merge Contributor New', 'experimental', '"pull-requests-merge-contributor-new"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:55', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (25, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-first-time-opened', NULL, 'Issues First Time Opened', 'experimental', '"issues-first-time-opened"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:56', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (26, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-first-time-closed', NULL, 'Issues First Time Closed', 'experimental', '"issues-first-time-closed"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:58', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (27, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/contributors-new', NULL, 'Contributors New', 'experimental', '"contributors-new"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:49:59', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (28, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/code-changes-lines', NULL, 'Code Changes Lines', 'experimental', '"code-changes-lines"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:01', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (29, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-new', NULL, 'Issues New', 'experimental', '"issues-new"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:02', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (30, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-closed', NULL, 'Issues Closed', 'experimental', '"issues-closed"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:04', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (31, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Issue Duration', 'experimental', '"issue-duration"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:05', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (32, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issue-backlog', NULL, 'Issue Backlog', 'experimental', '"issue-backlog"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:07', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (33, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-open-age', NULL, 'Issues Open Age', 'experimental', '"issues-open-age"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:08', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (34, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/issues-closed-resolution-duration', NULL, 'Issues Closed Resolution Duration', 'experimental', '"issues-closed-resolution-duration"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:10', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (35, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Lines Changed By Author', 'experimental', '"lines-changed-by-author"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:11', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (36, 'experimental', 'augur_db', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups', NULL, 'Repo Groups', 'experimental', '"repo-groups"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:13', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (37, 'experimental', 'augur_db', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/repos', NULL, 'Downloaded Repos', 'experimental', '"downloaded-repos"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:15', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (38, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/open-issues-count', NULL, 'Open Issues Count', 'experimental', '"closed-issues-count"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:16', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (39, 'experimental', 'augur_db', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/repo-groups/<repo_group_id>/repos/<repo_id>/closed-issues-count', NULL, 'Closed Issues Count', 'experimental', '"closed-issues-count"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:18', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (40, 'experimental', 'augur_db', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/repos/<owner>/<repo>', NULL, 'Get Repo', 'experimental', '"get-repo"', 'Insight Worker', '0.0.1', 'augur_db', '2019-06-20 22:50:19', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (41, 'experimental', 'downloads', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/downloads', NULL, 'Downloads', 'experimental', '"downloads"', 'Insight Worker', '0.0.1', 'downloads', '2019-06-20 22:50:21', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (42, 'experimental', 'githubapi', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/githubapi/pull_requests_closed', NULL, 'Pull Requests Closed', 'experimental', '"pull_requests_closed"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:22', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (43, 'experimental', 'githubapi', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/githubapi/pull_requests_merged', NULL, 'Pull Requests Merged', 'experimental', '"pull_requests_merged"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:24', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (44, 'experimental', 'githubapi', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/githubapi/pull_requests_open', NULL, 'Pull Requests Open', 'experimental', '"pull_requests_open"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:25', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (45, 'experimental', 'githubapi', 'metric', 'implemented', 'unimplemented', 't', '/api/unstable/<owner>/<repo>/githubapi/repository_size', NULL, 'Repository Size', 'experimental', '"repository-size"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:27', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (46, 'experimental', 'githubapi', 'metric', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/bus_factor', NULL, 'Bus Factor', 'experimental', '"bus-factor"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:28', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (47, 'experimental', 'githubapi', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/tags/major', NULL, 'Major Tags', 'experimental', '"major-tags"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:30', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (48, 'experimental', 'githubapi', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/tags', NULL, 'Tags', 'experimental', '"tags"', 'Insight Worker', '0.0.1', 'githubapi', '2019-06-20 22:50:31', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (49, 'experimental', 'facade', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/git/repos', NULL, 'Downloaded Repos', 'experimental', '"downloaded-repos"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:33', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (50, 'experimental', 'facade', 'git', 'implemented', 'implemented', 'f', '/api/unstable/git/changes_by_author', NULL, 'Lines Changed By Author', 'experimental', '"lines-changed-by-author"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:35', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (51, 'experimental', 'facade', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/git/lines_changed_by_week', NULL, 'Lines Changed By Week', 'experimental', '"lines-changed-by-week"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:36', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (52, 'experimental', 'facade', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/git/lines_changed_by_month', NULL, 'Lines Changed By Month', 'experimental', '"lines-changed-by-month"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:38', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (53, 'experimental', 'facade', 'git', 'implemented', 'unimplemented', 'f', '/api/unstable/git/commits_by_week', NULL, 'Commits By Week', 'experimental', '"commits-by-week"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:40', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (54, 'experimental', 'facade', 'git', 'implemented', 'implemented', 'f', '/api/unstable/git/facade_project', NULL, 'Facade Project', 'experimental', '"facade-project"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:41', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (55, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Annual Commit Count Ranked By New Repo In Repo Group', 'experimental', '"annual-commit-count-ranked-by-new-repo-in-repo-group"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:43', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (56, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Annual Lines Of Code Count Ranked By New Repo In Repo Group', 'experimental', '"annual-lines-of-code-count-ranked-by-new-repo-in-repo-group"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:44', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (57, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Annual Commit Count Ranked By Repo In Repo Group', 'experimental', '"annual-commit-count-ranked-by-repo-in-repo-group"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:46', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (58, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Annual Lines Of Code Count Ranked By Repo In Repo Group', 'experimental', '"annual-lines-of-code-count-ranked-by-repo-in-repo-group"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:48', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (59, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Lines Of Code Commit Counts By Calendar Year Grouped', 'experimental', '"lines-of-code-commit-counts-by-calendar-year-grouped"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:49', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (60, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Unaffiliated Contributors Lines Of Code Commit Counts By Calendar Year Grouped', 'experimental', '"unaffiliated-contributors-lines-of-code-commit-counts-by-calendar-year-grouped"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:51', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (61, 'experimental', 'facade', 'metric', 'implemented', 'unimplemented', 'f', 'none', NULL, 'Repo Group Lines Of Code Commit Counts Calendar Year Grouped', 'experimental', '"repo-group-lines-of-code-commit-counts-calendar-year-grouped"', 'Insight Worker', '0.0.1', 'facade', '2019-06-20 22:50:52', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (62, 'experimental', 'ghtorrent', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/contributing_github_organizations', NULL, 'Contributing Github Organizations', 'experimental', '"contributing-github-organizations"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:50:54', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (63, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/new_contributing_github_organizations', NULL, 'New Contributing Github Organizations', 'experimental', '"new-contributing-github-organizations"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:50:56', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (64, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/issue_comments', NULL, 'Issue Comments', 'experimental', '"issue-comments"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:50:57', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (65, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/pulls/made_closed', NULL, 'Pull Requests Made Closed', 'experimental', '"pull-requests-made-closed"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:50:59', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (66, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 't', '/api/unstable/<owner>/<repo>/timeseries/watchers', NULL, 'Watchers', 'experimental', '"watchers"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:00', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (67, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/commits100', NULL, 'Commits100', 'experimental', '"commits100"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:02', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (68, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/commits/comments', NULL, 'Commit Comments', 'experimental', '"commit-comments"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:03', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (69, 'experimental', 'ghtorrent', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/committer_locations', NULL, 'Committer Locations', 'experimental', '"committer-locations"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:05', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (70, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/total_committers', NULL, 'Total Committers', 'experimental', '"total-committers"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:07', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (71, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/issues/activity', NULL, 'Issue Activity', 'experimental', '"issue-activity"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:08', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (72, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/pulls/acceptance_rate', NULL, 'Pull Request Acceptance Rate', 'experimental', '"pull-request-acceptance-rate"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:10', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (73, 'experimental', 'ghtorrent', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/community_age', NULL, 'Community Age', 'experimental', '"community-age"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:11', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (74, 'experimental', 'ghtorrent', 'metric', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/contributions', NULL, 'Contributions', 'experimental', '"contributions"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:13', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (75, 'experimental', 'ghtorrent', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/project_age', NULL, 'Project Age', 'experimental', '"project-age"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:14', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (76, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/fakes', NULL, 'Fakes', 'experimental', '"fakes"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:16', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (77, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'unimplemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/total_watchers', NULL, 'Total Watchers', 'experimental', '"total-watchers"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:18', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (78, 'experimental', 'ghtorrent', 'timeseries', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/timeseries/new_watchers', NULL, 'New Watchers', 'experimental', '"new-watchers"', 'Insight Worker', '0.0.1', 'ghtorrent', '2019-06-20 22:51:19', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (79, 'experimental', 'librariesio', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/dependencies', NULL, 'Dependencies', 'experimental', '"dependencies"', 'Insight Worker', '0.0.1', 'librariesio', '2019-06-20 22:51:21', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (80, 'experimental', 'librariesio', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/dependency_stats', NULL, 'Dependency Stats', 'experimental', '"dependency-stats"', 'Insight Worker', '0.0.1', 'librariesio', '2019-06-20 22:51:23', NULL);
INSERT INTO "augur_data"."chaoss_metric_status" VALUES (81, 'experimental', 'librariesio', 'metric', 'implemented', 'implemented', 'f', '/api/unstable/<owner>/<repo>/dependents', NULL, 'Dependents', 'experimental', '"dependents"', 'Insight Worker', '0.0.1', 'librariesio', '2019-06-20 22:51:25', NULL);
COMMIT;

-- SPDX Schema Required Metadata 


-- ----------------------------
-- Records of relationship_types
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."relationship_types" VALUES (1, 'DESCRIBES');
INSERT INTO "spdx"."relationship_types" VALUES (2, 'DESCRIBED_BY');
INSERT INTO "spdx"."relationship_types" VALUES (3, 'CONTAINS');
INSERT INTO "spdx"."relationship_types" VALUES (4, 'CONTAINED_BY');
INSERT INTO "spdx"."relationship_types" VALUES (5, 'GENERATES');
INSERT INTO "spdx"."relationship_types" VALUES (6, 'GENERATED_FROM');
INSERT INTO "spdx"."relationship_types" VALUES (7, 'ANCESTOR_OF');
INSERT INTO "spdx"."relationship_types" VALUES (8, 'DESCENDANT_OF');
INSERT INTO "spdx"."relationship_types" VALUES (9, 'VARIANT_OF');
INSERT INTO "spdx"."relationship_types" VALUES (10, 'DISTRIBUTION_ARTIFACT');
INSERT INTO "spdx"."relationship_types" VALUES (11, 'PATCH_FOR');
INSERT INTO "spdx"."relationship_types" VALUES (12, 'PATCH_APPLIED');
INSERT INTO "spdx"."relationship_types" VALUES (13, 'COPY_OF');
INSERT INTO "spdx"."relationship_types" VALUES (14, 'FILE_ADDED');
INSERT INTO "spdx"."relationship_types" VALUES (15, 'FILE_DELETED');
INSERT INTO "spdx"."relationship_types" VALUES (16, 'FILE_MODIFIED');
INSERT INTO "spdx"."relationship_types" VALUES (17, 'EXPANDED_FROM_ARCHIVE');
INSERT INTO "spdx"."relationship_types" VALUES (18, 'DYNAMIC_LINK');
INSERT INTO "spdx"."relationship_types" VALUES (19, 'STATIC_LINK');
INSERT INTO "spdx"."relationship_types" VALUES (20, 'DATA_FILE_OF');
INSERT INTO "spdx"."relationship_types" VALUES (21, 'TEST_CASE_OF');
INSERT INTO "spdx"."relationship_types" VALUES (22, 'BUILD_TOOL_OF');
INSERT INTO "spdx"."relationship_types" VALUES (23, 'DOCUMENTATION_OF');
INSERT INTO "spdx"."relationship_types" VALUES (24, 'OPTIONAL_COMPONENT_OF');
INSERT INTO "spdx"."relationship_types" VALUES (25, 'METAFILE_OF');
INSERT INTO "spdx"."relationship_types" VALUES (26, 'PACKAGE_OF');
INSERT INTO "spdx"."relationship_types" VALUES (27, 'AMENDS');
INSERT INTO "spdx"."relationship_types" VALUES (28, 'PREREQUISITE_FOR');
INSERT INTO "spdx"."relationship_types" VALUES (29, 'HAS_PREREQUISITE');
INSERT INTO "spdx"."relationship_types" VALUES (30, 'OTHER');
COMMIT;



-- ----------------------------
-- Records of licenses
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."licenses" VALUES (1, '3dfx Glide License', 'Glide', 'http://spdx.org/licenses/Glide.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (2, 'Abstyles License', 'Abstyles', 'http://spdx.org/licenses/Abstyles.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (3, 'Academic Free License v1.1', 'AFL-1.1', 'http://spdx.org/licenses/AFL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (4, 'Academic Free License v1.2', 'AFL-1.2', 'http://spdx.org/licenses/AFL-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (5, 'Academic Free License v2.0', 'AFL-2.0', 'http://spdx.org/licenses/AFL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (6, 'Academic Free License v2.1', 'AFL-2.1', 'http://spdx.org/licenses/AFL-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (7, 'Academic Free License v3.0', 'AFL-3.0', 'http://spdx.org/licenses/AFL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (8, 'Academy of Motion Picture Arts and Sciences BSD', 'AMPAS', 'http://spdx.org/licenses/AMPAS.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (9, 'Adaptive Public License 1.0', 'APL-1.0', 'http://spdx.org/licenses/APL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (10, 'Adobe Glyph List License', 'Adobe-Glyph', 'http://spdx.org/licenses/Adobe-Glyph.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (11, 'Adobe Postscript AFM License', 'APAFML', 'http://spdx.org/licenses/APAFML.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (12, 'Adobe Systems Incorporated Source Code License Agreement', 'Adobe-2006', 'http://spdx.org/licenses/Adobe-2006.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (13, 'Affero General Public License v1.0', 'AGPL-1.0', 'http://spdx.org/licenses/AGPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (14, 'Afmparse License', 'Afmparse', 'http://spdx.org/licenses/Afmparse.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (15, 'Aladdin Free Public License', 'Aladdin', 'http://spdx.org/licenses/Aladdin.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (16, 'Amazon Digital Services License', 'ADSL', 'http://spdx.org/licenses/ADSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (17, 'AMD''s plpa_map.c License', 'AMDPLPA', 'http://spdx.org/licenses/AMDPLPA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (18, 'ANTLR Software Rights Notice', 'ANTLR-PD', 'http://spdx.org/licenses/ANTLR-PD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (19, 'Apache License 1.0', 'Apache-1.0', 'http://spdx.org/licenses/Apache-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (20, 'Apache License 1.1', 'Apache-1.1', 'http://spdx.org/licenses/Apache-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (21, 'Apache License 2.0', 'Apache-2.0', 'http://spdx.org/licenses/Apache-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (22, 'Apple MIT License', 'AML', 'http://spdx.org/licenses/AML.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (23, 'Apple Public Source License 1.0', 'APSL-1.0', 'http://spdx.org/licenses/APSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (24, 'Apple Public Source License 1.1', 'APSL-1.1', 'http://spdx.org/licenses/APSL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (25, 'Apple Public Source License 1.2', 'APSL-1.2', 'http://spdx.org/licenses/APSL-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (26, 'Apple Public Source License 2.0', 'APSL-2.0', 'http://spdx.org/licenses/APSL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (27, 'Artistic License 1.0', 'Artistic-1.0', 'http://spdx.org/licenses/Artistic-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (28, 'Artistic License 1.0 (Perl)', 'Artistic-1.0-Perl', 'http://spdx.org/licenses/Artistic-1.0-Perl.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (29, 'Artistic License 1.0 w/clause 8', 'Artistic-1.0-cl8', 'http://spdx.org/licenses/Artistic-1.0-cl8.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (30, 'Artistic License 2.0', 'Artistic-2.0', 'http://spdx.org/licenses/Artistic-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (31, 'Attribution Assurance License', 'AAL', 'http://spdx.org/licenses/AAL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (32, 'Bahyph License', 'Bahyph', 'http://spdx.org/licenses/Bahyph.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (33, 'Barr License', 'Barr', 'http://spdx.org/licenses/Barr.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (34, 'Beerware License', 'Beerware', 'http://spdx.org/licenses/Beerware.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (35, 'BitTorrent Open Source License v1.0', 'BitTorrent-1.0', 'http://spdx.org/licenses/BitTorrent-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (36, 'BitTorrent Open Source License v1.1', 'BitTorrent-1.1', 'http://spdx.org/licenses/BitTorrent-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (37, 'Boost Software License 1.0', 'BSL-1.0', 'http://spdx.org/licenses/BSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (38, 'Borceux license', 'Borceux', 'http://spdx.org/licenses/Borceux.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (39, 'BSD 2-clause "Simplified" License', 'BSD-2-Clause', 'http://spdx.org/licenses/BSD-2-Clause.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (40, 'BSD 2-clause FreeBSD License', 'BSD-2-Clause-FreeBSD', 'http://spdx.org/licenses/BSD-2-Clause-FreeBSD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (41, 'BSD 2-clause NetBSD License', 'BSD-2-Clause-NetBSD', 'http://spdx.org/licenses/BSD-2-Clause-NetBSD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (42, 'BSD 3-clause "New" or "Revised" License', 'BSD-3-Clause', 'http://spdx.org/licenses/BSD-3-Clause.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (43, 'BSD 3-clause Clear License', 'BSD-3-Clause-Clear', 'http://spdx.org/licenses/BSD-3-Clause-Clear.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (44, 'BSD 4-clause "Original" or "Old" License', 'BSD-4-Clause', 'http://spdx.org/licenses/BSD-4-Clause.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (45, 'BSD Protection License', 'BSD-Protection', 'http://spdx.org/licenses/BSD-Protection.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (46, 'BSD with attribution', 'BSD-3-Clause-Attribution', 'http://spdx.org/licenses/BSD-3-Clause-Attribution.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (47, 'BSD Zero Clause License', '0BSD', 'http://spdx.org/licenses/0BSD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (48, 'BSD-4-Clause (University of California-Specific)', 'BSD-4-Clause-UC', 'http://spdx.org/licenses/BSD-4-Clause-UC.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (49, 'bzip2 and libbzip2 License v1.0.5', 'bzip2-1.0.5', 'http://spdx.org/licenses/bzip2-1.0.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (50, 'bzip2 and libbzip2 License v1.0.6', 'bzip2-1.0.6', 'http://spdx.org/licenses/bzip2-1.0.6.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (51, 'Caldera License', 'Caldera', 'http://spdx.org/licenses/Caldera.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (52, 'CeCILL Free Software License Agreement v1.0', 'CECILL-1.0', 'http://spdx.org/licenses/CECILL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (53, 'CeCILL Free Software License Agreement v1.1', 'CECILL-1.1', 'http://spdx.org/licenses/CECILL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (54, 'CeCILL Free Software License Agreement v2.0', 'CECILL-2.0', 'http://spdx.org/licenses/CECILL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (55, 'CeCILL Free Software License Agreement v2.1', 'CECILL-2.1', 'http://spdx.org/licenses/CECILL-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (56, 'CeCILL-B Free Software License Agreement', 'CECILL-B', 'http://spdx.org/licenses/CECILL-B.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (57, 'CeCILL-C Free Software License Agreement', 'CECILL-C', 'http://spdx.org/licenses/CECILL-C.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (58, 'Clarified Artistic License', 'ClArtistic', 'http://spdx.org/licenses/ClArtistic.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (59, 'CMU License', 'MIT-CMU', 'http://spdx.org/licenses/MIT-CMU.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (60, 'CNRI Jython License', 'CNRI-Jython', 'http://spdx.org/licenses/CNRI-Jython.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (61, 'CNRI Python License', 'CNRI-Python', 'http://spdx.org/licenses/CNRI-Python.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (62, 'CNRI Python Open Source GPL Compatible License Agreement', 'CNRI-Python-GPL-Compatible', 'http://spdx.org/licenses/CNRI-Python-GPL-Compatible.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (63, 'Code Project Open License 1.02', 'CPOL-1.02', 'http://spdx.org/licenses/CPOL-1.02.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (64, 'Common Development and Distribution License 1.0', 'CDDL-1.0', 'http://spdx.org/licenses/CDDL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (65, 'Common Development and Distribution License 1.1', 'CDDL-1.1', 'http://spdx.org/licenses/CDDL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (66, 'Common Public Attribution License 1.0', 'CPAL-1.0', 'http://spdx.org/licenses/CPAL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (67, 'Common Public License 1.0', 'CPL-1.0', 'http://spdx.org/licenses/CPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (68, 'Computer Associates Trusted Open Source License 1.1', 'CATOSL-1.1', 'http://spdx.org/licenses/CATOSL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (69, 'Condor Public License v1.1', 'Condor-1.1', 'http://spdx.org/licenses/Condor-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (70, 'Creative Commons Attribution 1.0', 'CC-BY-1.0', 'http://spdx.org/licenses/CC-BY-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (71, 'Creative Commons Attribution 2.0', 'CC-BY-2.0', 'http://spdx.org/licenses/CC-BY-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (72, 'Creative Commons Attribution 2.5', 'CC-BY-2.5', 'http://spdx.org/licenses/CC-BY-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (73, 'Creative Commons Attribution 3.0', 'CC-BY-3.0', 'http://spdx.org/licenses/CC-BY-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (74, 'Creative Commons Attribution 4.0', 'CC-BY-4.0', 'http://spdx.org/licenses/CC-BY-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (75, 'Creative Commons Attribution No Derivatives 1.0', 'CC-BY-ND-1.0', 'http://spdx.org/licenses/CC-BY-ND-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (76, 'Creative Commons Attribution No Derivatives 2.0', 'CC-BY-ND-2.0', 'http://spdx.org/licenses/CC-BY-ND-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (77, 'Creative Commons Attribution No Derivatives 2.5', 'CC-BY-ND-2.5', 'http://spdx.org/licenses/CC-BY-ND-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (78, 'Creative Commons Attribution No Derivatives 3.0', 'CC-BY-ND-3.0', 'http://spdx.org/licenses/CC-BY-ND-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (79, 'Creative Commons Attribution No Derivatives 4.0', 'CC-BY-ND-4.0', 'http://spdx.org/licenses/CC-BY-ND-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (80, 'Creative Commons Attribution Non Commercial 1.0', 'CC-BY-NC-1.0', 'http://spdx.org/licenses/CC-BY-NC-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (81, 'Creative Commons Attribution Non Commercial 2.0', 'CC-BY-NC-2.0', 'http://spdx.org/licenses/CC-BY-NC-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (82, 'Creative Commons Attribution Non Commercial 2.5', 'CC-BY-NC-2.5', 'http://spdx.org/licenses/CC-BY-NC-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (83, 'Creative Commons Attribution Non Commercial 3.0', 'CC-BY-NC-3.0', 'http://spdx.org/licenses/CC-BY-NC-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (84, 'Creative Commons Attribution Non Commercial 4.0', 'CC-BY-NC-4.0', 'http://spdx.org/licenses/CC-BY-NC-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (85, 'Creative Commons Attribution Non Commercial No Derivatives 1.0', 'CC-BY-NC-ND-1.0', 'http://spdx.org/licenses/CC-BY-NC-ND-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (86, 'Creative Commons Attribution Non Commercial No Derivatives 2.0', 'CC-BY-NC-ND-2.0', 'http://spdx.org/licenses/CC-BY-NC-ND-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (87, 'Creative Commons Attribution Non Commercial No Derivatives 2.5', 'CC-BY-NC-ND-2.5', 'http://spdx.org/licenses/CC-BY-NC-ND-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (88, 'Creative Commons Attribution Non Commercial No Derivatives 3.0', 'CC-BY-NC-ND-3.0', 'http://spdx.org/licenses/CC-BY-NC-ND-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (89, 'Creative Commons Attribution Non Commercial No Derivatives 4.0', 'CC-BY-NC-ND-4.0', 'http://spdx.org/licenses/CC-BY-NC-ND-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (90, 'Creative Commons Attribution Non Commercial Share Alike 1.0', 'CC-BY-NC-SA-1.0', 'http://spdx.org/licenses/CC-BY-NC-SA-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (91, 'Creative Commons Attribution Non Commercial Share Alike 2.0', 'CC-BY-NC-SA-2.0', 'http://spdx.org/licenses/CC-BY-NC-SA-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (92, 'Creative Commons Attribution Non Commercial Share Alike 2.5', 'CC-BY-NC-SA-2.5', 'http://spdx.org/licenses/CC-BY-NC-SA-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (93, 'Creative Commons Attribution Non Commercial Share Alike 3.0', 'CC-BY-NC-SA-3.0', 'http://spdx.org/licenses/CC-BY-NC-SA-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (94, 'Creative Commons Attribution Non Commercial Share Alike 4.0', 'CC-BY-NC-SA-4.0', 'http://spdx.org/licenses/CC-BY-NC-SA-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (95, 'Creative Commons Attribution Share Alike 1.0', 'CC-BY-SA-1.0', 'http://spdx.org/licenses/CC-BY-SA-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (96, 'Creative Commons Attribution Share Alike 2.0', 'CC-BY-SA-2.0', 'http://spdx.org/licenses/CC-BY-SA-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (97, 'Creative Commons Attribution Share Alike 2.5', 'CC-BY-SA-2.5', 'http://spdx.org/licenses/CC-BY-SA-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (98, 'Creative Commons Attribution Share Alike 3.0', 'CC-BY-SA-3.0', 'http://spdx.org/licenses/CC-BY-SA-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (99, 'Creative Commons Attribution Share Alike 4.0', 'CC-BY-SA-4.0', 'http://spdx.org/licenses/CC-BY-SA-4.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (100, 'Creative Commons Zero v1.0 Universal', 'CC0-1.0', 'http://spdx.org/licenses/CC0-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (101, 'Crossword License', 'Crossword', 'http://spdx.org/licenses/Crossword.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (102, 'CrystalStacker License', 'CrystalStacker', 'http://spdx.org/licenses/CrystalStacker.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (103, 'CUA Office Public License v1.0', 'CUA-OPL-1.0', 'http://spdx.org/licenses/CUA-OPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (104, 'Cube License', 'Cube', 'http://spdx.org/licenses/Cube.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (105, 'Deutsche Freie Software Lizenz', 'D-FSL-1.0', 'http://spdx.org/licenses/D-FSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (106, 'diffmark license', 'diffmark', 'http://spdx.org/licenses/diffmark.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (107, 'Do What The F*ck You Want To Public License', 'WTFPL', 'http://spdx.org/licenses/WTFPL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (108, 'DOC License', 'DOC', 'http://spdx.org/licenses/DOC.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (109, 'Dotseqn License', 'Dotseqn', 'http://spdx.org/licenses/Dotseqn.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (110, 'DSDP License', 'DSDP', 'http://spdx.org/licenses/DSDP.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (111, 'dvipdfm License', 'dvipdfm', 'http://spdx.org/licenses/dvipdfm.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (112, 'Eclipse Public License 1.0', 'EPL-1.0', 'http://spdx.org/licenses/EPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (113, 'Educational Community License v1.0', 'ECL-1.0', 'http://spdx.org/licenses/ECL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (114, 'Educational Community License v2.0', 'ECL-2.0', 'http://spdx.org/licenses/ECL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (115, 'eGenix.com Public License 1.1.0', 'eGenix', 'http://spdx.org/licenses/eGenix.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (116, 'Eiffel Forum License v1.0', 'EFL-1.0', 'http://spdx.org/licenses/EFL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (117, 'Eiffel Forum License v2.0', 'EFL-2.0', 'http://spdx.org/licenses/EFL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (118, 'Enlightenment License (e16)', 'MIT-advertising', 'http://spdx.org/licenses/MIT-advertising.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (119, 'enna License', 'MIT-enna', 'http://spdx.org/licenses/MIT-enna.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (120, 'Entessa Public License v1.0', 'Entessa', 'http://spdx.org/licenses/Entessa.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (121, 'Erlang Public License v1.1', 'ErlPL-1.1', 'http://spdx.org/licenses/ErlPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (122, 'EU DataGrid Software License', 'EUDatagrid', 'http://spdx.org/licenses/EUDatagrid.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (123, 'European Union Public License 1.0', 'EUPL-1.0', 'http://spdx.org/licenses/EUPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (124, 'European Union Public License 1.1', 'EUPL-1.1', 'http://spdx.org/licenses/EUPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (125, 'Eurosym License', 'Eurosym', 'http://spdx.org/licenses/Eurosym.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (126, 'Fair License', 'Fair', 'http://spdx.org/licenses/Fair.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (127, 'feh License', 'MIT-feh', 'http://spdx.org/licenses/MIT-feh.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (128, 'Frameworx Open License 1.0', 'Frameworx-1.0', 'http://spdx.org/licenses/Frameworx-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (129, 'FreeImage Public License v1.0', 'FreeImage', 'http://spdx.org/licenses/FreeImage.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (130, 'Freetype Project License', 'FTL', 'http://spdx.org/licenses/FTL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (131, 'FSF Unlimited License', 'FSFUL', 'http://spdx.org/licenses/FSFUL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (132, 'FSF Unlimited License (with License Retention)', 'FSFULLR', 'http://spdx.org/licenses/FSFULLR.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (133, 'Giftware License', 'Giftware', 'http://spdx.org/licenses/Giftware.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (134, 'GL2PS License', 'GL2PS', 'http://spdx.org/licenses/GL2PS.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (135, 'Glulxe License', 'Glulxe', 'http://spdx.org/licenses/Glulxe.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (136, 'GNU Affero General Public License v3.0', 'AGPL-3.0', 'http://spdx.org/licenses/AGPL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (137, 'GNU Free Documentation License v1.1', 'GFDL-1.1', 'http://spdx.org/licenses/GFDL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (138, 'GNU Free Documentation License v1.2', 'GFDL-1.2', 'http://spdx.org/licenses/GFDL-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (139, 'GNU Free Documentation License v1.3', 'GFDL-1.3', 'http://spdx.org/licenses/GFDL-1.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (140, 'GNU General Public License v1.0 only', 'GPL-1.0', 'http://spdx.org/licenses/GPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (141, 'GNU General Public License v2.0 only', 'GPL-2.0', 'http://spdx.org/licenses/GPL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (142, 'GNU General Public License v3.0 only', 'GPL-3.0', 'http://spdx.org/licenses/GPL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (143, 'GNU Lesser General Public License v2.1 only', 'LGPL-2.1', 'http://spdx.org/licenses/LGPL-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (144, 'GNU Lesser General Public License v3.0 only', 'LGPL-3.0', 'http://spdx.org/licenses/LGPL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (145, 'GNU Library General Public License v2 only', 'LGPL-2.0', 'http://spdx.org/licenses/LGPL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (146, 'gnuplot License', 'gnuplot', 'http://spdx.org/licenses/gnuplot.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (147, 'gSOAP Public License v1.3b', 'gSOAP-1.3b', 'http://spdx.org/licenses/gSOAP-1.3b.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (148, 'Haskell Language Report License', 'HaskellReport', 'http://spdx.org/licenses/HaskellReport.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (149, 'Historic Permission Notice and Disclaimer', 'HPND', 'http://spdx.org/licenses/HPND.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (150, 'IBM PowerPC Initialization and Boot Software', 'IBM-pibs', 'http://spdx.org/licenses/IBM-pibs.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (151, 'IBM Public License v1.0', 'IPL-1.0', 'http://spdx.org/licenses/IPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (152, 'ICU License', 'ICU', 'http://spdx.org/licenses/ICU.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (153, 'ImageMagick License', 'ImageMagick', 'http://spdx.org/licenses/ImageMagick.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (154, 'iMatix Standard Function Library Agreement', 'iMatix', 'http://spdx.org/licenses/iMatix.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (155, 'Imlib2 License', 'Imlib2', 'http://spdx.org/licenses/Imlib2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (156, 'Independent JPEG Group License', 'IJG', 'http://spdx.org/licenses/IJG.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (157, 'Intel ACPI Software License Agreement', 'Intel-ACPI', 'http://spdx.org/licenses/Intel-ACPI.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (158, 'Intel Open Source License', 'Intel', 'http://spdx.org/licenses/Intel.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (159, 'Interbase Public License v1.0', 'Interbase-1.0', 'http://spdx.org/licenses/Interbase-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (160, 'IPA Font License', 'IPA', 'http://spdx.org/licenses/IPA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (161, 'ISC License', 'ISC', 'http://spdx.org/licenses/ISC.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (162, 'JasPer License', 'JasPer-2.0', 'http://spdx.org/licenses/JasPer-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (163, 'JSON License', 'JSON', 'http://spdx.org/licenses/JSON.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (164, 'LaTeX Project Public License 1.3a', 'LPPL-1.3a', 'http://spdx.org/licenses/LPPL-1.3a.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (165, 'LaTeX Project Public License v1.0', 'LPPL-1.0', 'http://spdx.org/licenses/LPPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (166, 'LaTeX Project Public License v1.1', 'LPPL-1.1', 'http://spdx.org/licenses/LPPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (167, 'LaTeX Project Public License v1.2', 'LPPL-1.2', 'http://spdx.org/licenses/LPPL-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (168, 'LaTeX Project Public License v1.3c', 'LPPL-1.3c', 'http://spdx.org/licenses/LPPL-1.3c.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (169, 'Latex2e License', 'Latex2e', 'http://spdx.org/licenses/Latex2e.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (170, 'Lawrence Berkeley National Labs BSD variant license', 'BSD-3-Clause-LBNL', 'http://spdx.org/licenses/BSD-3-Clause-LBNL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (171, 'Leptonica License', 'Leptonica', 'http://spdx.org/licenses/Leptonica.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (172, 'Lesser General Public License For Linguistic Resources', 'LGPLLR', 'http://spdx.org/licenses/LGPLLR.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (173, 'libpng License', 'Libpng', 'http://spdx.org/licenses/Libpng.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (174, 'libtiff License', 'libtiff', 'http://spdx.org/licenses/libtiff.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (175, 'Lucent Public License v1.02', 'LPL-1.02', 'http://spdx.org/licenses/LPL-1.02.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (176, 'Lucent Public License Version 1.0', 'LPL-1.0', 'http://spdx.org/licenses/LPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (177, 'MakeIndex License', 'MakeIndex', 'http://spdx.org/licenses/MakeIndex.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (178, 'Matrix Template Library License', 'MTLL', 'http://spdx.org/licenses/MTLL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (179, 'Microsoft Public License', 'MS-PL', 'http://spdx.org/licenses/MS-PL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (180, 'Microsoft Reciprocal License', 'MS-RL', 'http://spdx.org/licenses/MS-RL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (181, 'MirOS Licence', 'MirOS', 'http://spdx.org/licenses/MirOS.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (182, 'MIT +no-false-attribs license', 'MITNFA', 'http://spdx.org/licenses/MITNFA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (183, 'MIT License', 'MIT', 'http://spdx.org/licenses/MIT.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (184, 'Motosoto License', 'Motosoto', 'http://spdx.org/licenses/Motosoto.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (185, 'Mozilla Public License 1.0', 'MPL-1.0', 'http://spdx.org/licenses/MPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (186, 'Mozilla Public License 1.1', 'MPL-1.1', 'http://spdx.org/licenses/MPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (187, 'Mozilla Public License 2.0', 'MPL-2.0', 'http://spdx.org/licenses/MPL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (188, 'Mozilla Public License 2.0 (no copyleft exception)', 'MPL-2.0-no-copyleft-exception', 'http://spdx.org/licenses/MPL-2.0-no-copyleft-exception.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (189, 'mpich2 License', 'mpich2', 'http://spdx.org/licenses/mpich2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (190, 'Multics License', 'Multics', 'http://spdx.org/licenses/Multics.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (191, 'Mup License', 'Mup', 'http://spdx.org/licenses/Mup.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (192, 'NASA Open Source Agreement 1.3', 'NASA-1.3', 'http://spdx.org/licenses/NASA-1.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (193, 'Naumen Public License', 'Naumen', 'http://spdx.org/licenses/Naumen.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (194, 'Net Boolean Public License v1', 'NBPL-1.0', 'http://spdx.org/licenses/NBPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (195, 'NetCDF license', 'NetCDF', 'http://spdx.org/licenses/NetCDF.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (196, 'Nethack General Public License', 'NGPL', 'http://spdx.org/licenses/NGPL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (197, 'Netizen Open Source License', 'NOSL', 'http://spdx.org/licenses/NOSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (198, 'Netscape Public License v1.0', 'NPL-1.0', 'http://spdx.org/licenses/NPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (199, 'Netscape Public License v1.1', 'NPL-1.1', 'http://spdx.org/licenses/NPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (200, 'Newsletr License', 'Newsletr', 'http://spdx.org/licenses/Newsletr.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (201, 'No Limit Public License', 'NLPL', 'http://spdx.org/licenses/NLPL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (202, 'Nokia Open Source License', 'Nokia', 'http://spdx.org/licenses/Nokia.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (203, 'Non-Profit Open Software License 3.0', 'NPOSL-3.0', 'http://spdx.org/licenses/NPOSL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (204, 'Noweb License', 'Noweb', 'http://spdx.org/licenses/Noweb.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (205, 'NRL License', 'NRL', 'http://spdx.org/licenses/NRL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (206, 'NTP License', 'NTP', 'http://spdx.org/licenses/NTP.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (207, 'Nunit License', 'Nunit', 'http://spdx.org/licenses/Nunit.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (208, 'OCLC Research Public License 2.0', 'OCLC-2.0', 'http://spdx.org/licenses/OCLC-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (209, 'ODC Open Database License v1.0', 'ODbL-1.0', 'http://spdx.org/licenses/ODbL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (210, 'ODC Public Domain Dedication &amp; License 1.0', 'PDDL-1.0', 'http://spdx.org/licenses/PDDL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (211, 'Open Group Test Suite License', 'OGTSL', 'http://spdx.org/licenses/OGTSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (212, 'Open LDAP Public License  2.2.2', 'OLDAP-2.2.2', 'http://spdx.org/licenses/OLDAP-2.2.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (213, 'Open LDAP Public License v1.1', 'OLDAP-1.1', 'http://spdx.org/licenses/OLDAP-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (214, 'Open LDAP Public License v1.2', 'OLDAP-1.2', 'http://spdx.org/licenses/OLDAP-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (215, 'Open LDAP Public License v1.3', 'OLDAP-1.3', 'http://spdx.org/licenses/OLDAP-1.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (216, 'Open LDAP Public License v1.4', 'OLDAP-1.4', 'http://spdx.org/licenses/OLDAP-1.4.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (217, 'Open LDAP Public License v2.0 (or possibly 2.0A and 2.0B)', 'OLDAP-2.0', 'http://spdx.org/licenses/OLDAP-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (218, 'Open LDAP Public License v2.0.1', 'OLDAP-2.0.1', 'http://spdx.org/licenses/OLDAP-2.0.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (219, 'Open LDAP Public License v2.1', 'OLDAP-2.1', 'http://spdx.org/licenses/OLDAP-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (220, 'Open LDAP Public License v2.2', 'OLDAP-2.2', 'http://spdx.org/licenses/OLDAP-2.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (221, 'Open LDAP Public License v2.2.1', 'OLDAP-2.2.1', 'http://spdx.org/licenses/OLDAP-2.2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (222, 'Open LDAP Public License v2.3', 'OLDAP-2.3', 'http://spdx.org/licenses/OLDAP-2.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (223, 'Open LDAP Public License v2.4', 'OLDAP-2.4', 'http://spdx.org/licenses/OLDAP-2.4.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (224, 'Open LDAP Public License v2.5', 'OLDAP-2.5', 'http://spdx.org/licenses/OLDAP-2.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (225, 'Open LDAP Public License v2.6', 'OLDAP-2.6', 'http://spdx.org/licenses/OLDAP-2.6.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (226, 'Open LDAP Public License v2.7', 'OLDAP-2.7', 'http://spdx.org/licenses/OLDAP-2.7.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (227, 'Open LDAP Public License v2.8', 'OLDAP-2.8', 'http://spdx.org/licenses/OLDAP-2.8.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (228, 'Open Market License', 'OML', 'http://spdx.org/licenses/OML.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (229, 'Open Public License v1.0', 'OPL-1.0', 'http://spdx.org/licenses/OPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (230, 'Open Software License 1.0', 'OSL-1.0', 'http://spdx.org/licenses/OSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (231, 'Open Software License 1.1', 'OSL-1.1', 'http://spdx.org/licenses/OSL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (232, 'Open Software License 2.0', 'OSL-2.0', 'http://spdx.org/licenses/OSL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (233, 'Open Software License 2.1', 'OSL-2.1', 'http://spdx.org/licenses/OSL-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (234, 'Open Software License 3.0', 'OSL-3.0', 'http://spdx.org/licenses/OSL-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (235, 'OpenSSL License', 'OpenSSL', 'http://spdx.org/licenses/OpenSSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (236, 'PHP License v3.0', 'PHP-3.0', 'http://spdx.org/licenses/PHP-3.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (237, 'PHP License v3.01', 'PHP-3.01', 'http://spdx.org/licenses/PHP-3.01.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (238, 'Plexus Classworlds License', 'Plexus', 'http://spdx.org/licenses/Plexus.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (239, 'PostgreSQL License', 'PostgreSQL', 'http://spdx.org/licenses/PostgreSQL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (240, 'psfrag License', 'psfrag', 'http://spdx.org/licenses/psfrag.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (241, 'psutils License', 'psutils', 'http://spdx.org/licenses/psutils.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (242, 'Python License 2.0', 'Python-2.0', 'http://spdx.org/licenses/Python-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (243, 'Q Public License 1.0', 'QPL-1.0', 'http://spdx.org/licenses/QPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (244, 'Qhull License', 'Qhull', 'http://spdx.org/licenses/Qhull.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (245, 'Rdisc License', 'Rdisc', 'http://spdx.org/licenses/Rdisc.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (246, 'RealNetworks Public Source License v1.0', 'RPSL-1.0', 'http://spdx.org/licenses/RPSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (247, 'Reciprocal Public License 1.1', 'RPL-1.1', 'http://spdx.org/licenses/RPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (248, 'Reciprocal Public License 1.5', 'RPL-1.5', 'http://spdx.org/licenses/RPL-1.5.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (249, 'Red Hat eCos Public License v1.1', 'RHeCos-1.1', 'http://spdx.org/licenses/RHeCos-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (250, 'Ricoh Source Code Public License', 'RSCPL', 'http://spdx.org/licenses/RSCPL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (251, 'RSA Message-Digest License ', 'RSA-MD', 'http://spdx.org/licenses/RSA-MD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (252, 'Ruby License', 'Ruby', 'http://spdx.org/licenses/Ruby.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (253, 'Sax Public Domain Notice', 'SAX-PD', 'http://spdx.org/licenses/SAX-PD.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (254, 'Saxpath License', 'Saxpath', 'http://spdx.org/licenses/Saxpath.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (255, 'SCEA Shared Source License', 'SCEA', 'http://spdx.org/licenses/SCEA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (256, 'Scheme Widget Library (SWL) Software License Agreement', 'SWL', 'http://spdx.org/licenses/SWL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (257, 'Sendmail License', 'Sendmail', 'http://spdx.org/licenses/Sendmail.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (258, 'SGI Free Software License B v1.0', 'SGI-B-1.0', 'http://spdx.org/licenses/SGI-B-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (259, 'SGI Free Software License B v1.1', 'SGI-B-1.1', 'http://spdx.org/licenses/SGI-B-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (260, 'SGI Free Software License B v2.0', 'SGI-B-2.0', 'http://spdx.org/licenses/SGI-B-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (261, 'SIL Open Font License 1.0', 'OFL-1.0', 'http://spdx.org/licenses/OFL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (262, 'SIL Open Font License 1.1', 'OFL-1.1', 'http://spdx.org/licenses/OFL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (263, 'Simple Public License 2.0', 'SimPL-2.0', 'http://spdx.org/licenses/SimPL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (264, 'Sleepycat License', 'Sleepycat', 'http://spdx.org/licenses/Sleepycat.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (265, 'SNIA Public License 1.1', 'SNIA', 'http://spdx.org/licenses/SNIA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (266, 'Spencer License 86', 'Spencer-86', 'http://spdx.org/licenses/Spencer-86.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (267, 'Spencer License 94', 'Spencer-94', 'http://spdx.org/licenses/Spencer-94.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (268, 'Spencer License 99', 'Spencer-99', 'http://spdx.org/licenses/Spencer-99.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (269, 'Standard ML of New Jersey License', 'SMLNJ', 'http://spdx.org/licenses/SMLNJ.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (270, 'SugarCRM Public License v1.1.3', 'SugarCRM-1.1.3', 'http://spdx.org/licenses/SugarCRM-1.1.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (271, 'Sun Industry Standards Source License v1.1', 'SISSL', 'http://spdx.org/licenses/SISSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (272, 'Sun Industry Standards Source License v1.2', 'SISSL-1.2', 'http://spdx.org/licenses/SISSL-1.2.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (273, 'Sun Public License v1.0', 'SPL-1.0', 'http://spdx.org/licenses/SPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (274, 'Sybase Open Watcom Public License 1.0', 'Watcom-1.0', 'http://spdx.org/licenses/Watcom-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (275, 'TCL/TK License', 'TCL', 'http://spdx.org/licenses/TCL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (276, 'The Unlicense', 'Unlicense', 'http://spdx.org/licenses/Unlicense.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (277, 'TMate Open Source License', 'TMate', 'http://spdx.org/licenses/TMate.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (278, 'TORQUE v2.5+ Software License v1.1', 'TORQUE-1.1', 'http://spdx.org/licenses/TORQUE-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (279, 'Trusster Open Source License', 'TOSL', 'http://spdx.org/licenses/TOSL.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (280, 'Unicode Terms of Use', 'Unicode-TOU', 'http://spdx.org/licenses/Unicode-TOU.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (281, 'Universal Permissive License v1.0', 'UPL-1.0', 'http://spdx.org/licenses/UPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (282, 'University of Illinois/NCSA Open Source License', 'NCSA', 'http://spdx.org/licenses/NCSA.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (283, 'Vim License', 'Vim', 'http://spdx.org/licenses/Vim.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (284, 'VOSTROM Public License for Open Source', 'VOSTROM', 'http://spdx.org/licenses/VOSTROM.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (285, 'Vovida Software License v1.0', 'VSL-1.0', 'http://spdx.org/licenses/VSL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (286, 'W3C Software Notice and License (1998-07-20)', 'W3C-19980720', 'http://spdx.org/licenses/W3C-19980720.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (287, 'W3C Software Notice and License (2002-12-31)', 'W3C', 'http://spdx.org/licenses/W3C.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (288, 'Wsuipa License', 'Wsuipa', 'http://spdx.org/licenses/Wsuipa.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (289, 'X.Net License', 'Xnet', 'http://spdx.org/licenses/Xnet.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (290, 'X11 License', 'X11', 'http://spdx.org/licenses/X11.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (291, 'Xerox License', 'Xerox', 'http://spdx.org/licenses/Xerox.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (292, 'XFree86 License 1.1', 'XFree86-1.1', 'http://spdx.org/licenses/XFree86-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (293, 'xinetd License', 'xinetd', 'http://spdx.org/licenses/xinetd.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (294, 'XPP License', 'xpp', 'http://spdx.org/licenses/xpp.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (295, 'XSkat License', 'XSkat', 'http://spdx.org/licenses/XSkat.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (296, 'Yahoo! Public License v1.0', 'YPL-1.0', 'http://spdx.org/licenses/YPL-1.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (297, 'Yahoo! Public License v1.1', 'YPL-1.1', 'http://spdx.org/licenses/YPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (298, 'Zed License', 'Zed', 'http://spdx.org/licenses/Zed.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (299, 'Zend License v2.0', 'Zend-2.0', 'http://spdx.org/licenses/Zend-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (300, 'Zimbra Public License v1.3', 'Zimbra-1.3', 'http://spdx.org/licenses/Zimbra-1.3.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (301, 'Zimbra Public License v1.4', 'Zimbra-1.4', 'http://spdx.org/licenses/Zimbra-1.4.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (302, 'zlib License', 'Zlib', 'http://spdx.org/licenses/Zlib.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (303, 'zlib/libpng License with Acknowledgement', 'zlib-acknowledgement', 'http://spdx.org/licenses/zlib-acknowledgement.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (304, 'Zope Public License 1.1', 'ZPL-1.1', 'http://spdx.org/licenses/ZPL-1.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (305, 'Zope Public License 2.0', 'ZPL-2.0', 'http://spdx.org/licenses/ZPL-2.0.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (306, 'Zope Public License 2.1', 'ZPL-2.1', 'http://spdx.org/licenses/ZPL-2.1.html', '', 't');
INSERT INTO "spdx"."licenses" VALUES (307, 'eCos license version 2.0', 'eCos-2.0', 'http://spdx.org/licenses/eCos-2.0', '', 't');
INSERT INTO "spdx"."licenses" VALUES (308, 'GNU General Public License v1.0 or later', 'GPL-1.0+', 'http://spdx.org/licenses/GPL-1.0+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (309, 'GNU General Public License v2.0 or later', 'GPL-2.0+', 'http://spdx.org/licenses/GPL-2.0+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (310, 'GNU General Public License v2.0 w/Autoconf exception', 'GPL-2.0-with-autoconf-exception', 'http://spdx.org/licenses/GPL-2.0-with-autoconf-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (311, 'GNU General Public License v2.0 w/Bison exception', 'GPL-2.0-with-bison-exception', 'http://spdx.org/licenses/GPL-2.0-with-bison-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (312, 'GNU General Public License v2.0 w/Classpath exception', 'GPL-2.0-with-classpath-exception', 'http://spdx.org/licenses/GPL-2.0-with-classpath-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (313, 'GNU General Public License v2.0 w/Font exception', 'GPL-2.0-with-font-exception', 'http://spdx.org/licenses/GPL-2.0-with-font-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (314, 'GNU General Public License v2.0 w/GCC Runtime Library exception', 'GPL-2.0-with-GCC-exception', 'http://spdx.org/licenses/GPL-2.0-with-GCC-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (315, 'GNU General Public License v3.0 or later', 'GPL-3.0+', 'http://spdx.org/licenses/GPL-3.0+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (316, 'GNU General Public License v3.0 w/Autoconf exception', 'GPL-3.0-with-autoconf-exception', 'http://spdx.org/licenses/GPL-3.0-with-autoconf-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (317, 'GNU General Public License v3.0 w/GCC Runtime Library exception', 'GPL-3.0-with-GCC-exception', 'http://spdx.org/licenses/GPL-3.0-with-GCC-exception', '', 't');
INSERT INTO "spdx"."licenses" VALUES (318, 'GNU Lesser General Public License v2.1 or later', 'LGPL-2.1+', 'http://spdx.org/licenses/LGPL-2.1+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (319, 'GNU Lesser General Public License v3.0 or later', 'LGPL-3.0+', 'http://spdx.org/licenses/LGPL-3.0+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (320, 'GNU Library General Public License v2 or later', 'LGPL-2.0+', 'http://spdx.org/licenses/LGPL-2.0+', '', 't');
INSERT INTO "spdx"."licenses" VALUES (321, 'Standard ML of New Jersey License', 'StandardML-NJ', 'http://spdx.org/licenses/StandardML-NJ', '', 't');
INSERT INTO "spdx"."licenses" VALUES (322, 'wxWindows Library License', 'WXwindows', 'http://spdx.org/licenses/WXwindows', '', 't');
COMMIT;



-- ----------------------------
-- Records of file_types
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."file_types" VALUES (4, 'APPLICATION');
INSERT INTO "spdx"."file_types" VALUES (3, 'ARCHIVE');
INSERT INTO "spdx"."file_types" VALUES (5, 'AUDIO');
INSERT INTO "spdx"."file_types" VALUES (2, 'BINARY');
INSERT INTO "spdx"."file_types" VALUES (9, 'DOCUMENTATION');
INSERT INTO "spdx"."file_types" VALUES (6, 'IMAGE');
INSERT INTO "spdx"."file_types" VALUES (11, 'OTHER');
INSERT INTO "spdx"."file_types" VALUES (1, 'SOURCE');
INSERT INTO "spdx"."file_types" VALUES (10, 'SPDX');
INSERT INTO "spdx"."file_types" VALUES (7, 'TEXT');
INSERT INTO "spdx"."file_types" VALUES (8, 'VIDEO');
COMMIT;







-- ----------------------------
-- Records of creator_types
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."creator_types" VALUES (1, 'Person');
INSERT INTO "spdx"."creator_types" VALUES (2, 'Organization');
INSERT INTO "spdx"."creator_types" VALUES (3, 'Tool');
COMMIT;


-- ----------------------------
-- Records of annotation_types
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."annotation_types" VALUES (1, 'REVIEW');
INSERT INTO "spdx"."annotation_types" VALUES (2, 'OTHER');
COMMIT;


-- ----------------------------
-- Records of creators
-- ----------------------------
BEGIN;
INSERT INTO "spdx"."creators" VALUES (1, 3, 'dosocs2-0.16.1', '');
COMMIT;

BEGIN; 


INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25222, 'venuvardhanreddytekula8@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:14:35', '2021-02-06 15:14:35', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25221, 'nichols.keanu9@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:14:11', '2021-02-06 15:14:11', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25220, 'ubuntu@ip-172-31-2-14.us-west-2.compute.internal', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:13:50', '2021-02-06 15:13:50', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25219, 'kmlumbard@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:13:21', '2021-02-06 15:13:21', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25218, 'jonah.zukosky@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:12:50', '2021-02-06 15:12:50', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25217, 'pogayo17@alustudent.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:12:14', '2021-02-06 15:12:14', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25216, 'mishrapratik356@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:11:23', '2021-02-06 15:11:23', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25215, 'andrewbrain2019@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:10:42', '2021-02-06 15:10:42', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25214, 'root@bing0ne.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:10:15', '2021-02-06 15:10:15', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25213, 'gordonli@me.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:09:46', '2021-02-06 15:09:46', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25212, 'ac.be', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:09:20', '2021-02-06 15:09:20', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25211, 'shohanduttaroy99@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:08:56', '2021-02-06 15:08:56', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25210, 'missouri.edu', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:08:27', '2021-02-06 15:08:27', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25209, 'akarajgi0@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:07:11', '2021-02-06 15:07:11', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25208, 'jacobeharding@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:06:45', '2021-02-06 15:06:45', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25207, 'hacksmath@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:06:19', '2021-02-06 15:06:19', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25206, 'benjaminparish628@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:05:48', '2021-02-06 15:05:48', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25205, 'msnell@unomaha.edu', '1970-01-01', NULL, NULL, NULL, '2021-02-06 15:04:05', '2021-02-06 15:04:05', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25204, 'aksharap.181it132@nitk.edu.in', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:10:03', '2021-02-06 14:10:03', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25203, 'iyovcheva@vmware.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:09:36', '2021-02-06 14:09:36', 'VMWare', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25202, 'maximumbalk@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:09:15', '2021-02-06 14:09:15', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25201, '43684300+pratikmishra356@users.noreply.github.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:08:34', '2021-02-06 14:08:34', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25200, 'abhinavbajpai2012@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:08:01', '2021-02-06 14:08:01', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25188, 'ortonpaul18@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:05:58', '2021-02-06 14:05:58', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25187, 'linkgeorg@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:05:29', '2021-02-06 14:05:29', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25186, 'parth261297@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:05:02', '2021-02-06 14:05:02', 'Google Summer of Code', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25185, 'users.noreply.github.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:04:39', '2021-02-06 14:04:39', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25184, 'foundjem@users.noreply.github.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:04:12', '2021-02-06 14:04:12', 'CHAOSS Community', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25183, 'gsyc.es', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:03:39', '2021-02-06 14:03:39', 'Bitergia', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25182, 'harshalmittal4@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:03:21', '2021-02-06 14:03:21', 'Bitergia', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25181, '31676518+tretrue@users.noreply.github.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:02:57', '2021-02-06 14:02:57', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25180, 'klumbard@unomaha.edu', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:02:28', '2021-02-06 14:02:28', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25179, 'gabe.heim@yahoo.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:01:55', '2021-02-06 14:01:55', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25178, 'ccarterlandis@pm.me', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:01:34', '2021-02-06 14:01:34', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25177, 'ccarterlandis@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:01:13', '2021-02-06 14:01:13', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25176, 'abuhman@users.noreply.github.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:00:32', '2021-02-06 14:00:32', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25175, 'gogginss@missouri.edu', '1970-01-01', NULL, NULL, NULL, '2021-02-06 14:00:06', '2021-02-06 14:00:06', 'University of Missouri', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25174, 'spencerrrobinson@unomaha.edu', '1970-01-01', NULL, NULL, NULL, '2021-02-06 13:59:19', '2021-02-06 13:59:19', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25173, 'germonprez@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 13:58:48', '2021-02-06 13:58:48', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25172, 'derek@howderek.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 13:57:56', '2021-02-06 13:57:56', 'Lawrence Livermore National Lab', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25171, 'doombreakr@gmail.com', '1970-01-01', NULL, NULL, NULL, '2021-02-06 13:57:20', '2021-02-06 13:57:20', 'Lawrence Livermore National Lab', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "ca_start_date", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_affiliation", "ca_active") VALUES (25170, 'cmehil.warn@gmail.com', '2016-05-06', 'load', '1.0', 'load', '2021-02-06 13:55:16', '2021-02-06 13:56:46', 'University of Nebraska-Omaha', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24189, 'jschnake@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24190, 'schnake.john@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24191, 'bmcerlean@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24192, 'bridget@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24193, 'ashish.amarnath@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24194, 'ashisham@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24195, 'gus@inodes.org', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24196, 'felipe.alfaro@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24197, 'sameer@damagehead.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24198, 'sameer@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24199, 'sameersbn@Sameers-MacBook-Pro.local', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24200, 'adnan@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24201, 'adnan@prydoni.us', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24202, 'adnan@adnan-bitnami.local', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24203, 'apulido@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24204, 'ara@ubuntu.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24205, 'bridgetmcerlean@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24206, 'migmartri@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24207, 'miguel@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24208, 'dbarranco@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24209, 'jbianquetti@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24210, 'jbianquetti-nami@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24211, 'andres.mgotor@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24212, 'andres@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24213, 'juanjosec@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24214, 'containers@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24215, 'bors\[bot\]@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24216, 'matt.goodall@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24217, 'j-fuentes@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24218, 'jfuentes@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24219, 'mnelson@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24220, 'mkm@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24221, 'mmikulicic@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24222, 'james@jameswestby.net', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24223, 'stephen.stewart@carisenda.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24224, 'daniel.lopez@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24225, 'nomisbeme@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24226, 'marcos@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24227, 'marcosbc@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24228, 'juan@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24229, 'juan_ariza_cordoba@hotmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24230, 'jota@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24231, 'jotamartos@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24232, 'alejandro@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24233, 'alexrwave@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24234, 'jotadrilo@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24235, 'jsalmeron@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24236, 'tomas@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24237, 'vikram@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24238, 'vikram-bitnami@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24239, 'crhernandez@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24240, 'carrodher1179@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24241, 'juanjo@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24242, 'juanjo@bitrock.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24243, 'beltran@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24244, 'angel@bitnami.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24245, 'Angelmmiguel@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24246, 'rcampuzano82@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24247, 'andy@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24248, 'andy.goldstein@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24249, 'goldsteina@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24250, 'nolan@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (27291, 'brubakern@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24252, 'nolan@nbrubaker.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24253, 'stevek@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24254, 'steve@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24255, 'stephen.kriss@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24256, 'krisss@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24257, 'carlisia@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24258, 'carlisia@grokkingtech.io', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24259, 'carlisiac@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24260, 'carlisia@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24261, 'wayne@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24262, 'wayne@riotousliving.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24263, 'wwitzel3@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24264, 'jennifer@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24265, 'jrondeau@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24266, 'Bradamant3@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24267, 'aadnan@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24268, 'dave@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24269, 'dave@cheney.net', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24270, 'steves@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24271, 'steve@stevesloka.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24272, 'slokas@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24273, 'ynick@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24274, 'inocuo@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24275, 'ynick@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24276, 'jpeach@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24277, 'ross@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24278, 'ross@kukulinski.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24279, 'ralph@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24280, 'ralph.l.bankston@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24281, 'alex_brand@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24282, 'alexbrand09@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24283, 'joe@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24284, 'joe.github@bedafamily.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24285, 'vince@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24286, 'vince@vincepri.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24287, 'chuck@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24288, 'ha.chuck@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24289, 'jason@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24290, 'detiber@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24291, 'detiberusj@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24292, 'liz@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24293, '.*liztio@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24294, 'naadir@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24295, 'naadir@randomvariable.co.uk', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24296, 'randomvariable@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24297, 'ruben@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24298, 'rubenoz@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (24299, 'rdodev@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25300, 'tstclair@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25301, 'timothysc@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25302, 'craigtracey@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25303, 'luohui925@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25304, 'davanum@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25305, 'amy@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25306, 'bryanliles@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25307, 'bryan@Bryans-MacBook-Pro.local', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25308, 'lilesb@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25309, 'sfoohei@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25310, 'foos@vmware.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25311, 'mlandaverde@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25312, 'mdaverde@users.noreply.github.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25313, 'shomron@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25314, 'derek@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25315, 'jderekwilson@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25316, 'eric@heptio.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25317, 'kate.kuchin@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25318, 'suraci.alex@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25319, 'asuraci@pivotal.io', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25320, 'alex@localhost.localdomain', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25321, 'julian.zucker@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25322, 'sahil.muthoo@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25323, 'fali@pivotal.io', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25324, 'fai28683@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25325, 'dgarnier@pivotal.io', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25326, 'git@garnier.wf', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25327, 'matthew.heidemann@gmail.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25328, 'me@lurraca.com', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;
INSERT INTO "augur_data"."contributor_affiliations"("ca_id", "ca_domain", "tool_source", "tool_version", "data_source", "data_collection_date", "ca_last_used", "ca_start_date", "ca_affiliation", "ca_active") VALUES (25329, 'lurraca@pivotal.io', 'Helper Script', NULL, 'Dawn''s vmware_mapping JSON', '2020-04-28 18:52:49', '2020-04-28 18:52:49', '1970-01-01', 'VMware', 1) ON CONFLICT DO NOTHING;

COMMIT; 

