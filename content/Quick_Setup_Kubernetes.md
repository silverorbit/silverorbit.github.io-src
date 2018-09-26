Title: Easily and Quickly Setup Kubernetes using LXD. 
Date: 2018-09-19 03:18
Category: Tools
Tags: aws, lxd, microservices

Running Kubernetes in 5 easy steps.


```
$ sudo snap install conjure-up --classic --edge
$ sudo snap install lxd
$ /snap/bin/lxd init
$ sudo usermod -a -G lxd $USER
$ conjure-up kubernetes
```

![Yay] (/images/k8/juju-status.jpg)

Setup the dashboard yet: [https://github.com/kubernetes/dashboard](https://github.com/kubernetes/dashboard)


Or we can create user for admin here: 
[https://github.com/kubernetes/dashboard/wiki/Creating-sample-user](https://github.com/kubernetes/dashboard/wiki/Creating-sample-user)

```
tmux 
kubectl proxy
```

Now perform the forwarding so we can access the dashboard locally using the command on local machine:  
`ssh ubuntu@<remoteip> -L 8001:127.0.0.1:8001 -N`

And hitting our local browser on port 8001, we see the following Dashboard.

![Yay] (/images/k8/view_dashboard.jpg)


We can also try to ssh back to the host machine and execute a sample application.

```
kubectl run hello-world --replicas=2 --labels="run=load-balancer-example" --image=gcr.io/google-samples/node-hello:1.0 --port=8080
```


![Yay](/images/k8/view-hello.jpg)


It's fast and easy to get Kubernetes for any demo purposes.




