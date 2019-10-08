# Changelog for Thoth's Template GitHub Project

## [0.2.0] - 2019-Oct-05 - goern

### Added

Added methods to create a topic and to send to a topic. These need some love, error handling is basically none!

## [0.1.0] - 2019-Sep-11 - goern

### Added

all the things that you see...

## Release 0.2.1 (2019-10-08T08:08:16)
* :pushpin: Automatic update of dependency pytest-cov from 2.7.1 to 2.8.1
* :pushpin: Automatic update of dependency pytest from 5.1.3 to 5.2.1
* :pushpin: Automatic update of dependency faust from 1.7.4 to 1.8.0
* :pushpin: Automatic update of dependency thoth-common from 0.9.10 to 0.9.12
* Update .zuul.yaml
* :green_heart: removed the pytest jobs from all pipelines
* :green_heart: started adding tests
* :green_heart: added the tests/ directory
* :green_heart: remove the writing of test coverage data (for now)
* oh, left over stuff we dont need was removed
* added a release pipeline job to push to pypi
* :sparkles: added create_topic, publish_to_topic
* added the required requirements files
* note required
* added an explicite serializer
* this is the basic set of files, updated ...
