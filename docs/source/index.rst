Augur Documentation
==================================

:doc:`Welcome! <getting-started/Welcome>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   getting-started/Welcome
   quick-start
   deployment/toc
   getting-started/toc
   development-guide/toc
   rest-api/api
   docker/toc
   schema/toc
   login
   procedures/toc
.. 

..
  deployment/toc
..
  schema/toc

.. image:: development-guide/images/augur-architecture-2.png
  :width: 700
  :alt: Development guide image overview of augur


What is Augur?
~~~~~~~~~~~~~~~~

Augur is a software suite for collecting and measuring structured data about free and open-source software (FOSS) communities.

Augur's main focus is to measure the overall health and sustainability of open source projects, as these types of projects are system critical for nearly every software organization or company. We do this by gathering data about project repositories and normalizing that into our data model to provide useful metrics about your project's health. For example, one of our metrics is Burstiness. Burstiness - how are short timeframes of intense activity, followed by a corresponding return to a typical pattern of activity, observed in a project? This can paint a picture of a project's focus and gain insight into the potential stability of a project and how its typical cycle of updates occurs. There are many more useful metrics, and you can find a full list of them `here <https://chaoss.community/metrics/>`__.

Augur gathers trace data for a group of repositories, normalize it into our data model, and provide a variety of metrics about that data.

This software is developed as part of the CHAOSS (Community Health Analytics Open Source Software) project. Many of our metrics are implementations of the metrics defined by our community. You can find more information about how to get involved on the `CHAOSS website <https://chaoss.community>`_.

If you want to see augur in action, you can view CHAOSS's augur instance `here <https://ai.chaoss.io/>`_.

Contributors & Maintainers
---------------------------
You can find the complete list of:

- Current maintainers
- Former maintainainers
- Founding maintainers
- Contributors
- Google Summer of Code participants

here:
`Contributors & Participants (CONTRIBUTORS.md) <https://github.com/chaoss/augur/blob/main/CONTRIBUTORS.md>`_
