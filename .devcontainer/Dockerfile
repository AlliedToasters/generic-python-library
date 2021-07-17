FROM docker pull nvcr.io/nvidia/pytorch:21.06-py3

RUN apt-get update
RUN apt-get install -y gcc gfortran make wget libpng-dev libopenblas-dev curl git  python3-dev

RUN ln -s /usr/include/locale.h /usr/include/xlocale.hs

RUN pip3 install  "awscli>=1.16,<2" \
  databricks-cli==0.8.6 \
  twine \
  wheel

RUN curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64 && \
  chmod +x ./kops && \
  mv ./kops /usr/local/bin/

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
  chmod +x ./kubectl && \
  mv ./kubectl /usr/local/bin/kubectl

RUN addgroup --gid 639 brewmaster
RUN adduser --disabled-password --gecos "brewmaster" --gid 639 --uid 639 brewmaster
USER brewmaster
RUN pip3 install --no-warn-script-location scikit-learn
