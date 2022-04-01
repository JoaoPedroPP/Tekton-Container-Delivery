import os
a = [
    "pipeline-run-5lcmq-build-pod",
"pipeline-run-5lcmq-clone-pod",
"pipeline-run-bst7s-build-pod",
"pipeline-run-bst7s-clone-pod",
"pipeline-run-fqh82-build-pod",
"pipeline-run-fqh82-clone-pod",
"pipeline-run-mzlgz-build-pod",
"pipeline-run-mzlgz-clone-pod"
]

for i in a:
    os.system('kubectl delete pod {}'.format(i))