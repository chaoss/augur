Schema Change Process
============

1. All database changes will be approved via pull request by Sean Goggins, following these basic principles:
        - Avoid redundant data collection
        - Ensure consistent naming
        - Ensure logical and consistent breakdown of tables versus columns in a table
        - Ensure foreign key and other rules are implemented
        - Ensure the four pieces of Augur metadata are added

2. Production Deployment involves the following steps
        - Sean makes the changes to the reference schema
        - Sean adds the "update script" to the Augur Build
        - Carter verifies that the update works

3. Development deployment will involve Sean making the changes to the instance of the Augur schema is developing on with all due speed. **It is critical that our intention to tightly control changes to the database does not impede developer velocity or momentum**.

