from dulwich import client
from dulwich import index
from dulwich.repo import Repo

url = "https://gitee.com/sdf321/ascend-deployer"
local_repo = Repo.init('ad', mkdir=True)
remote_repo = client.HttpGitClient(url, pool_manager=None)
remote_refs = remote_repo.fetch(url, local_repo)
local_repo[b"HEAD"] = remote_refs[b"refs/heads/support_msinstaller"]
index_file = local_repo.index_path()
tree = local_repo[b"HEAD"].tree
index.build_index_from_tree(local_repo.path, index_file,
                            local_repo.object_store, tree)
