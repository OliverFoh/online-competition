const ipcRenderer = require('electron').ipcRenderer;
const session = require('electron').remote.session;
let login = () => {
  let name = document.getElementById('name');
  let password = document.getElementById('password');
};
/**
 * 保存用户名和密码
 */
let savePassword = () => {
  let name = document.getElementById('name').value;
  let password = document.getElementById('password').value;
  setCookie('name', name);
  setCookie('password', password);
};
/**
 * 获得
 */
let getCookies = () => {
  session.defaultSession.cookies.get({ url: "http://www.github.com" }, function (error, cookies) {
    console.log(cookies);
    if (cookies.length > 0) {
      let name = document.getElementById('name');
      name.value = cookies[0].value;
      let password = document.getElementById('password');
      password.value = cookies[1].value;
    }
  });
};
/**
 * 清空缓存
 */
let clearCookies = () => {
  session.defaultSession.clearStorageData({
    origin: "http://www.github.com",
    storages: ['cookies']
  }, function (error) {
    if (error) console.error(error);
  })
};

/**
 * 保存cookie
 * @param name  cookie名称
 * @param value cookie值
 */
let setCookie = (name, value) => {
  let Days = 30;
  let exp = new Date();
  let date = Math.round(exp.getTime() / 1000) + Days * 24 * 60 * 60;
  const cookie = {
    url: "http://www.github.com",
    name: name,
    value: value,
    expirationDate: date
  };
  session.defaultSession.cookies.set(cookie, (error) => {
    if (error) console.error(error);
  });
};

getCookies();
