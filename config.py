# encoding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import os

# Authentication for user filing issue (must have read/write access to repository to add issue to)
USERNAME = 'Huangxiaowen47'
TOKEN = os.environ.get('G_T') 

# The repository to add this issue to
REPO_OWNER = 'Huangxiaowen47'
REPO_NAME = 'DailyPapers'

# Set new submission url of subject
NEW_SUB_URL = 'https://arxiv.org/list/cs/new'

# Keywords to search
KEYWORD_LIST = [
    "Super-Resolution", "SISR", 
    "Video Anomaly Detection", "VAD", "Abnormal Event",
    "Token Compression", "Token Pruning", "Token Merging", "Efficient Transformer"
]

OPENAI_API_KEYS = [os.environ.get('DS_KEY'), ] 
LANGUAGE = "zh"  # zh | en
