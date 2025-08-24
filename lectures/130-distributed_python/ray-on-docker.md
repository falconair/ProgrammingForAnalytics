# Set up ray via docker

docker network create ray-network

# Ray dashboard: 8265, GCS: 6379, Jupyter: 8888, Ray Client Server: 10001
docker run -it --name ray-head --network ray-network -p 8265:8265 -p 6379:6379 rayproject/ray:latest
ray start --head --dashboard-host=0.0.0.0 --dashboard-port=8265
# ray stop|status
# docker run -d --name ray-head --network ray-network -p 8265:8265 -p 6379:6379 rayproject/ray:latest ray start --head --dashboard-host=0.0.0.0 --dashboard-port=8265


# http://localhost:8265/#/cluster will show connected nodes

docker run -it --name ray1 --network ray-network rayproject/ray:latest
ray start --address='ray-head:6379'
# docker run -d --name ray1 --network ray-network rayproject/ray:latest ray start --address='ray-head:6379' 



docker run -it --name ray2 --network ray-network rayproject/ray:latest
ray start --address='ray-head:6379'

RAY_ADDRESS='http://172.18.0.2:8265' ray job submit --working-dir . -- python my_script.py
ray job submit --address http://localhost:8265 --working-dir . -- python job_script.py
# docker run -d --name ray2 --network ray-network rayproject/ray:latest ray start --address='ray-head:6379' 

# See "Jobs" tab in the dashboard


TODO:
- Add Jupyter notebook support
- Test Ray serve
- Test ML related features