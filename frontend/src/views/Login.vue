<template>
    <BlogHeader/>
    <div id="grid">
        <div id="signup">
            <h3>注册账号</h3>
            <form>
                <div class="form-elem">
                    <span>账号：</span>
                    <input v-model="signupName" type="text" placeholder="输入用户名">
                </div>
                <div class="form-elem">
                    <span>密码1：</span>
                    <input v-model="signupPwd1" type="password" placeholder="输入密码">
                </div>
                <div class="form-elem">
                    <span>密码2：</span>
                    <input v-model="signupPwd2" type="password" placeholder="输入密码">
                </div>
                <div class="form-elem">
                    <button v-on:click.prevent="Signup">提交</button>
                </div>
            </form>
        </div>

        <div id="signin">
            <h3>登录账号</h3>
            <form>
                <div class="form-elem">
                    <span>账号：</span>
                    <input v-model="signinName" type="text" placeholder="输入用户名">
                </div>

                <div class="form-elem">
                    <span>密码：</span>
                    <input v-model="signinPwd" type="password" placeholder="输入密码">
                </div>

                <div class="form-elem">
                    <button v-on:click.prevent="Signin">登录</button>
                </div>
            </form>
        </div>
    </div>
    <BlogFooter/>
</template>

<script>
    import BlogHeader from "../components/BlogHeader";
    import BlogFooter from "../components/BlogFooter";
    import axios from "axios";

    export default {
        name: "Login",
        components: {BlogFooter, BlogHeader},
        data: function () {
            return {
                signupName: '',
                signupPwd1: '',
                signupPwd2: '',
                signinName: '',
                signinPwd: '',
                signupResponse: null,
            }
        },
        methods: {
            Signup() {
                if (this.signupPwd1 === this.signupPwd2) {
                    const that = this;
                    axios
                        .post('/api/user/', {
                            username: this.signupName,
                            password: this.signupPwd1,
                        })
                        .then(function (response) {
                            that.signupResponse = response.data;
                            alert('用户注册成功，快去登录吧！');
                        })
                        .catch(function (error) {
                            alert(error.message);
                            // Handling Error here...
                            // https://github.com/axios/axios#handling-errors
                        })
                } else {
                    alert('两次输入密码不一样，请重试');
                }
            },
            Signin() {
                const that = this;
                axios
                    .post('/api/token/', {
                        username: that.signinName,
                        password: that.signinPwd,
                    })  //获取token
                    .then(function (response) {
                        const storage = localStorage;
                        // Date.parse(...) 返回1970年1月1日UTC以来的毫秒数
                        // Token 被设置为1分钟，因此这里加上60000毫秒
                        const expiredTime = Date.parse(response.headers.date) + 60000;
                        // 设置 localStorage
                        storage.setItem('access.myblog', response.data.access);
                        storage.setItem('refresh.myblog', response.data.refresh);
                        storage.setItem('expiredTime.myblog', expiredTime);
                        storage.setItem('username.myblog', that.signinName);  //令牌、过期时间和用户名一并保存
                        // 是否为管理员
                        axios
                            .get('/api/user/' + that.signinName + '/')
                            .then(function (response) {
                                storage.setItem('isSuperuser.myblog', response.data.is_superuser);
                                // 路由跳转修改到这里
                                that.$router.push({name: 'Home'});   // 登录成功后回到博客首页
                            })
                            .catch(function () {
                                alert("只有管理员能够发文章...");
                            })
                    })
                    .catch(function () {
                        alert("账号或密码错误...");
                    })
            },
        }
    }
</script>

<style scoped>
    #grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
    #signup {
        text-align: center;
    }
    .form-elem {
        padding: 10px;
    }
    input {
        height: 25px;
        padding-left: 10px;
    }
    button {
        height: 35px;
        cursor: pointer;
        border: none;
        outline: none;
        background: gray;
        color: whitesmoke;
        border-radius: 5px;
        width: 60px;
    }
</style>