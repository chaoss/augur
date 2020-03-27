<template>
<div class="login">
  <img alt="augur logo" src="@/assets/logo.png"  class="center">
       <div class="container">
         
  <div class="form">
    <div class="row">
      <div class="col"></div>
     <div class="col"> <h4 style="text-align:center">Login</h4></div>
      
      </div>
      <div class="row">
      <div class="col">
        <a href="#" class="fb btn" v-on:click="login()">
          <i class="fa fa-twitter fa-fw"></i> Login with Facebook
        </a>  
              
        <a href="#" class="twitter btn">
          <i class="fa fa-twitter fa-fw"></i> Login with Twitter
        </a>
        <a href="#" class="google btn">
          <i class="fa fa-google fa-fw"></i> Login with Google+
        </a>
      </div>

      <div class="col">
        <div class="hide-md-lg">
          <p>Or sign in manually:</p>
        </div>

        
        <input type="text" name="username" v-model="input.username" placeholder="Username" required />
        <input type="password" name="password" v-model="input.password" placeholder="Password" required />
        <input type="submit" v-on:click="normalLogin()" value="Login">
       
      </div>

    </div>
  </div>
</div>


  </div>
   
</template>

<script async defer src="https://connect.facebook.net/en_US/sdk.js"></script>
<script>


    export default {
        name: 'Login',
        data() {
            return {
                input: {
                    username: "",
                    password: ""
                },
                isConnected: false,
                 FB: {},
                 message: ''
            }
        },
        mounted () {
            window.checkLoginState=this.checkLoginState
            let _this = this
            this.$nextTick(() => {
            window.fbAsyncInit = function () {
                FB.init({
                appId: '579783109556137',
                xfbml: true,
                version: 'v2.6'
                })
                FB.AppEvents.logPageView()
                _this.FB = FB
                console.log('FB SDK was initialized as mixin')
            };
            (function (d, s, id) {
                let js, fjs = d.getElementsByTagName(s)[0]
                if (d.getElementById(id)) { return }
                js = d.createElement(s); js.id = id
                js.src = '//connect.facebook.net/en_US/sdk.js'
                fjs.parentNode.insertBefore(js, fjs)
            }(document, 'script', 'facebook-jssdk'))
            })
  },
        methods: {
            normalLogin() {
                if(this.input.username != "" && this.input.password != "") {
                    if(this.input.username == "nayan" && this.input.password == "nayan") {
                        
                        this.$router.replace({ name: "secure" });
                    } else {
                        console.log("The username and / or password is incorrect");
                    }
                } else {
                    console.log("A username and password must be present");
                }
            },
            
            login() {
                
                FB.login(function(response) {
                if (response.status === 'connected') {

                checkLoginState();

                        
                }  else {
                 // Login failed 
                 console.log("Login failed");
         }
        });},
            checkLoginState : function() {
                FB.getLoginStatus(function (response) {
                    console.log("Login Successfull");
                
                });
            //this.$emit("authenticated", true);
            this.$router.replace({ name: "secure" });
}
        
            },
           
        }
    
</script>

<style scoped>
   
    h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

* {box-sizing: border-box}

/* style the container */
.container {
  position: relative;
  border-radius: 15px;
  background-color: #f2f2f2;
  padding: 10px 0 30px 0;
  margin: auto;
  width: 60%;
}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
  
}
/* style inputs and link buttons */
input,
.btn {
  width: 100%;
  padding: 12px;
  border: none;
  border-radius: 4px;
  margin: 5px 0;
  opacity: 0.85;
  display: inline-block;
  font-size: 17px;
  line-height: 20px;
  text-decoration: none; /* remove underline from anchors */
}

input:hover,
.btn:hover {
  opacity: 1;
}


.fb {
  background-color: #3B5998;
  color: white;
}

.twitter {
  background-color: #55ACEE;
  color: white;
}

.google {
  background-color: #dd4b39;
  color: white;
}

/* style the submit button */
input[type=submit] {
  background-color: #4CAF50;
  color: white;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

/* Two-column layout */
.col {
  float: left;
  width: 50%;
  margin: auto;
  padding: 0 50px;
  margin-top: 6px;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* vertical line */
.vl {
  position: absolute;
  left: 50%;
  transform: translate(-50%);
  border: 2px solid #ddd;
  height: 175px;
}

.inner {
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  background-color: #f1f1f1;
  border: 1px solid #ccc;
  border-radius: 50%;
  padding: 8px 10px;
}


.hide-md-lg {
  display: none;
}

.bottom-container {
  text-align: center;
  background-color: #666;
  border-radius: 0px 0px 4px 4px;
}

@media screen and (max-width: 650px) {
  .col {
    width: 100%;
    margin-top: 0;
  }
  /* hide the vertical line */
  .vl {
    display: none;
  }
  /* show the hidden text on small screens */
  .hide-md-lg {
    display: block;
    text-align: center;
  }
}

.login {
  
  margin: auto;
}


.button {
  margin: auto;
}
</style>