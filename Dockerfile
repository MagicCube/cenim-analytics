FROM node:boron

MAINTAINER Henry Li <henry1943@163.com>

# Use Alibaba's NPM mirror
RUN npm set registry https://registry.npm.taobao.org/

# creat workdir
RUN mkdir -p /usr/projects/cenim-analytics
WORKDIR /usr/projects/cenim-analytics

# Install dependencies
COPY package.json /usr/projects/cenim-analytics
RUN npm install --production

# copy other codes and resources
COPY . /usr/projects/cenim-analytics

EXPOSE 3000
# ENTRYPOINT diff CMD CDM can be overrided
CMD [ "npm", "start" ]
