export function get(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', url);
    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        reject(`Request failed.  Returned status of ${xhr.status}`);
      }
    };
    xhr.send(null);
  });
}

export function post(url, params = null) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', url);
    xhr.onload = () => {
      if (xhr.status === 200) {
        if (xhr.getResponseHeader('Content-Type').toLocaleLowerCase() === 'application/json') {
          resolve(JSON.parse(xhr.responseText));
        } else {
          resolve(xhr.responseText);
        }
      } else {
        reject(`Request failed.  Returned status of ${xhr.status}`);
      }
    };
    if (params) {
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.send(JSON.stringify(params));
    } else {
      xhr.send(null);
    }
  });
}
