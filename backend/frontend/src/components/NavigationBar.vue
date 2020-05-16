<template>
  <nav class="bd-navbar navbar is-spaced" :class="{'navbar--hidden': !showNavbar}">
    <div class="container">
      <div class="navbar-brand">
        <figure class="navbar-item" id="navbar-logo">
          <img src="../assets/img/logo.png" alt />
        </figure>

        <!-- <a class="navbar-item" id="navbar-logo" href="#" style="font-weight:bold;">Graditude</a> -->
        <span class="navbar-burger burger" data-target="navMenu">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
      <div id="navMenu" class="navbar-menu">
        <div class="navbar-start">
          <a href="#" class="navbar-item bd-navbar-item">About</a>
          <a href="#" class="navbar-item bd-navbar-item" v-scroll-to="'#JobsTable'">Careers</a>
        </div>
        <div class="navbar-end">
          <a
            class="button is-info navbar-item bd-navbar-item"
            @click="isComponentModalActive = true"
          >Sign In</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
document.addEventListener("DOMContentLoaded", function() {
  // Get all "navbar-burger" elements
  var $navbarBurgers = Array.prototype.slice.call(
    document.querySelectorAll(".navbar-burger"),
    0
  );

  // Check if there are any nav burgers
  if ($navbarBurgers.length > 0) {
    // Add a click event on each of them
    $navbarBurgers.forEach(function($el) {
      $el.addEventListener("click", function() {
        // Get the target from the "data-target" attribute
        var target = $el.dataset.target;
        var $target = document.getElementById(target);

        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle("is-active");
        $target.classList.toggle("is-active");
      });
    });
  }
});

export default {
  name: "NavigationBar",
  components: {},
  data() {
    return {
      showNavbar: true,
      lastScrollPosition: 0
    };
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
  },
  beforeDestroy() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    onScroll() {
      const currentScrollPos =
        window.pageYOffset || document.documentElement.scrollTop;

      if (currentScrollPos < 0) {
        return;
      }
      // Stop executing this function if the difference between
      // current scroll position and last scroll position is less than some offset
      const OFFSET = 60;
      if (Math.abs(currentScrollPos - this.lastScrollPosition) < OFFSET) {
        return;
      }
      this.showNavbar = currentScrollPos < this.lastScrollPosition;
      this.lastScrollPosition = currentScrollPos;
    }
  }
};
</script>

<style>
.navbar {
  position: fixed;
  transform: translate3d(0, 0, 0);
  transition: 0.3s all ease-out;
}

.navbar > .container {
  max-width: 1100px;
}

.navbar.navbar--hidden {
  box-shadow: none;
  transform: translate3d(0, -100%, 0);
}

</style>