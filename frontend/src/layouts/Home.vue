<!-- #SPDX-License-Identifier: MIT -->
<template>
    <d-container fluid>
      <h1>Welcome to <span>Augur</span></h1>
        <div id="img">
            <img src="../assets/logo.png" alt="logo">
        </div>
        <div id="button">
            <a href="/home">Get Started</a>
        </div>
    </d-container>
</template>

<script>
export default {
  name: 'home',
  components: {
  },
  data() {
    return {
    };
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@500&family=Ubuntu:wght@700&display=swap');
span{
    color: #1E90FF;
    font-family: 'Rubik', sans-serif;
}
h1, a{
    margin-top: 200px;
    text-align: center;
    font-family: 'Rubik', sans-serif;
}

img{
    width: 100%;
    height: 100%;
}

#img{
    width: 500px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 30px;
}

a{
    text-decoration: none;
    color: white;
}

a:hover{
    text-decoration: none;
    color: white;
}

#button{
    border: 2px solid #1E90FF;
    width: 120px;
    background-color: #1E90FF;
    border-radius: 10px;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
}



</style>