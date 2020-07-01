# coding: utf-8

"""
    edu-sharing Repository REST API

    The public restful API of the edu-sharing repository.  # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PersonDeleteOptions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'cleanup_metadata': 'bool',
        'home_folder': 'HomeFolderOptions',
        'shared_folders': 'SharedFolderOptions',
        'collections': 'CollectionOptions',
        'ratings': 'DeleteOption',
        'comments': 'DeleteOption',
        'collection_feedback': 'DeleteOption',
        'statistics': 'DeleteOption',
        'stream': 'DeleteOption',
        'receiver': 'str',
        'receiver_group': 'str'
    }

    attribute_map = {
        'cleanup_metadata': 'cleanupMetadata',
        'home_folder': 'homeFolder',
        'shared_folders': 'sharedFolders',
        'collections': 'collections',
        'ratings': 'ratings',
        'comments': 'comments',
        'collection_feedback': 'collectionFeedback',
        'statistics': 'statistics',
        'stream': 'stream',
        'receiver': 'receiver',
        'receiver_group': 'receiverGroup'
    }

    def __init__(self, cleanup_metadata=False, home_folder=None, shared_folders=None, collections=None, ratings=None, comments=None, collection_feedback=None, statistics=None, stream=None, receiver=None, receiver_group=None):  # noqa: E501
        """PersonDeleteOptions - a model defined in Swagger"""  # noqa: E501

        self._cleanup_metadata = None
        self._home_folder = None
        self._shared_folders = None
        self._collections = None
        self._ratings = None
        self._comments = None
        self._collection_feedback = None
        self._statistics = None
        self._stream = None
        self._receiver = None
        self._receiver_group = None
        self.discriminator = None

        if cleanup_metadata is not None:
            self.cleanup_metadata = cleanup_metadata
        if home_folder is not None:
            self.home_folder = home_folder
        if shared_folders is not None:
            self.shared_folders = shared_folders
        if collections is not None:
            self.collections = collections
        if ratings is not None:
            self.ratings = ratings
        if comments is not None:
            self.comments = comments
        if collection_feedback is not None:
            self.collection_feedback = collection_feedback
        if statistics is not None:
            self.statistics = statistics
        if stream is not None:
            self.stream = stream
        if receiver is not None:
            self.receiver = receiver
        if receiver_group is not None:
            self.receiver_group = receiver_group

    @property
    def cleanup_metadata(self):
        """Gets the cleanup_metadata of this PersonDeleteOptions.  # noqa: E501


        :return: The cleanup_metadata of this PersonDeleteOptions.  # noqa: E501
        :rtype: bool
        """
        return self._cleanup_metadata

    @cleanup_metadata.setter
    def cleanup_metadata(self, cleanup_metadata):
        """Sets the cleanup_metadata of this PersonDeleteOptions.


        :param cleanup_metadata: The cleanup_metadata of this PersonDeleteOptions.  # noqa: E501
        :type: bool
        """

        self._cleanup_metadata = cleanup_metadata

    @property
    def home_folder(self):
        """Gets the home_folder of this PersonDeleteOptions.  # noqa: E501


        :return: The home_folder of this PersonDeleteOptions.  # noqa: E501
        :rtype: HomeFolderOptions
        """
        return self._home_folder

    @home_folder.setter
    def home_folder(self, home_folder):
        """Sets the home_folder of this PersonDeleteOptions.


        :param home_folder: The home_folder of this PersonDeleteOptions.  # noqa: E501
        :type: HomeFolderOptions
        """

        self._home_folder = home_folder

    @property
    def shared_folders(self):
        """Gets the shared_folders of this PersonDeleteOptions.  # noqa: E501


        :return: The shared_folders of this PersonDeleteOptions.  # noqa: E501
        :rtype: SharedFolderOptions
        """
        return self._shared_folders

    @shared_folders.setter
    def shared_folders(self, shared_folders):
        """Sets the shared_folders of this PersonDeleteOptions.


        :param shared_folders: The shared_folders of this PersonDeleteOptions.  # noqa: E501
        :type: SharedFolderOptions
        """

        self._shared_folders = shared_folders

    @property
    def collections(self):
        """Gets the collections of this PersonDeleteOptions.  # noqa: E501


        :return: The collections of this PersonDeleteOptions.  # noqa: E501
        :rtype: CollectionOptions
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this PersonDeleteOptions.


        :param collections: The collections of this PersonDeleteOptions.  # noqa: E501
        :type: CollectionOptions
        """

        self._collections = collections

    @property
    def ratings(self):
        """Gets the ratings of this PersonDeleteOptions.  # noqa: E501


        :return: The ratings of this PersonDeleteOptions.  # noqa: E501
        :rtype: DeleteOption
        """
        return self._ratings

    @ratings.setter
    def ratings(self, ratings):
        """Sets the ratings of this PersonDeleteOptions.


        :param ratings: The ratings of this PersonDeleteOptions.  # noqa: E501
        :type: DeleteOption
        """

        self._ratings = ratings

    @property
    def comments(self):
        """Gets the comments of this PersonDeleteOptions.  # noqa: E501


        :return: The comments of this PersonDeleteOptions.  # noqa: E501
        :rtype: DeleteOption
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this PersonDeleteOptions.


        :param comments: The comments of this PersonDeleteOptions.  # noqa: E501
        :type: DeleteOption
        """

        self._comments = comments

    @property
    def collection_feedback(self):
        """Gets the collection_feedback of this PersonDeleteOptions.  # noqa: E501


        :return: The collection_feedback of this PersonDeleteOptions.  # noqa: E501
        :rtype: DeleteOption
        """
        return self._collection_feedback

    @collection_feedback.setter
    def collection_feedback(self, collection_feedback):
        """Sets the collection_feedback of this PersonDeleteOptions.


        :param collection_feedback: The collection_feedback of this PersonDeleteOptions.  # noqa: E501
        :type: DeleteOption
        """

        self._collection_feedback = collection_feedback

    @property
    def statistics(self):
        """Gets the statistics of this PersonDeleteOptions.  # noqa: E501


        :return: The statistics of this PersonDeleteOptions.  # noqa: E501
        :rtype: DeleteOption
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this PersonDeleteOptions.


        :param statistics: The statistics of this PersonDeleteOptions.  # noqa: E501
        :type: DeleteOption
        """

        self._statistics = statistics

    @property
    def stream(self):
        """Gets the stream of this PersonDeleteOptions.  # noqa: E501


        :return: The stream of this PersonDeleteOptions.  # noqa: E501
        :rtype: DeleteOption
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this PersonDeleteOptions.


        :param stream: The stream of this PersonDeleteOptions.  # noqa: E501
        :type: DeleteOption
        """

        self._stream = stream

    @property
    def receiver(self):
        """Gets the receiver of this PersonDeleteOptions.  # noqa: E501


        :return: The receiver of this PersonDeleteOptions.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this PersonDeleteOptions.


        :param receiver: The receiver of this PersonDeleteOptions.  # noqa: E501
        :type: str
        """

        self._receiver = receiver

    @property
    def receiver_group(self):
        """Gets the receiver_group of this PersonDeleteOptions.  # noqa: E501


        :return: The receiver_group of this PersonDeleteOptions.  # noqa: E501
        :rtype: str
        """
        return self._receiver_group

    @receiver_group.setter
    def receiver_group(self, receiver_group):
        """Sets the receiver_group of this PersonDeleteOptions.


        :param receiver_group: The receiver_group of this PersonDeleteOptions.  # noqa: E501
        :type: str
        """

        self._receiver_group = receiver_group

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PersonDeleteOptions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersonDeleteOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
