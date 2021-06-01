<template>
  <div class="wrapper" :class="{ 'nav-open': $sidebar.showSidebar }">
    <notifications></notifications>
    <sidebar-fixed-toggle-button />
    <side-bar :background-color="sidebarBackground" :short-title="$t('sidebar.shortTitle')" :title="$t('sidebar.title')">
      <template slot="links">
        <sidebar-item :link="{ name: $t('sidebar.dashboard'), icon: 'tim-icons icon-chart-pie-36', path: '/' }"> </sidebar-item>
        <sidebar-item :link="{ name: $t('sidebar.forms'), icon: 'tim-icons icon-notes' }">
          <sidebar-item :link="{ name: $t('sidebar.regularForms'), path: '/forms/regular' }"></sidebar-item>
          <sidebar-item :link="{ name: $t('sidebar.extendedForms'), path: '/forms/extended' }"></sidebar-item>
          <sidebar-item :link="{ name: $t('sidebar.validationForms'), path: '/forms/validation' }"></sidebar-item>
          <sidebar-item :link="{ name: $t('sidebar.wizard'), path: '/forms/wizard' }"></sidebar-item>
        </sidebar-item>
        <sidebar-item :link="{ name: $t('sidebar.tables'), icon: 'tim-icons icon-puzzle-10', path: '/table-list/paginated' }"></sidebar-item>
        <sidebar-item :link="{ name: $t('sidebar.charts'), icon: 'tim-icons icon-chart-bar-32', path: '/charts' }"></sidebar-item>
      </template>
    </side-bar>
    <div class="main-panel" :data="sidebarBackground">
      <dashboard-navbar></dashboard-navbar>
      <router-view name="header"></router-view>
      <div :class="{ content: true }" @click="toggleSidebar">
        <zoom-center-transition :duration="200" mode="out-in">
          <nuxt />
        </zoom-center-transition>
      </div>
      <content-footer></content-footer>
    </div>
  </div>
</template>
<script>
/* eslint-disable no-new */
import PerfectScrollbar from 'perfect-scrollbar'
import 'perfect-scrollbar/css/perfect-scrollbar.css'
import SidebarShare from '@/components/Layout/SidebarSharePlugin'
function hasElement(className) {
  return document.getElementsByClassName(className).length > 0
}

function initScrollbar(className) {
  if (hasElement(className)) {
    new PerfectScrollbar(`.${className}`)
  } else {
    // try to init it later in case this component is loaded async
    setTimeout(() => {
      initScrollbar(className)
    }, 100)
  }
}

import DashboardNavbar from '@/components/Layout/DashboardNavbar.vue'
import ContentFooter from '@/components/Layout/ContentFooter.vue'
import DashboardContent from '@/components/Layout/Content.vue'
import SidebarFixedToggleButton from '@/components/Layout/SidebarFixedToggleButton.vue'
import { SlideYDownTransition, ZoomCenterTransition } from 'vue2-transitions'

export default {
  components: {
    DashboardNavbar,
    ContentFooter,
    SidebarFixedToggleButton,
    DashboardContent,
    SlideYDownTransition,
    ZoomCenterTransition,
    SidebarShare
  },
  data() {
    return {
      sidebarBackground: 'vue' //vue|blue|orange|green|red|primary
    }
  },
  methods: {
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false)
      }
    },
    initScrollbar() {
      let docClasses = document.body.classList
      let isWindows = navigator.platform.startsWith('Win')
      if (isWindows) {
        // if we are on windows OS we activate the perfectScrollbar function
        initScrollbar('sidebar')
        initScrollbar('main-panel')
        initScrollbar('sidebar-wrapper')

        docClasses.add('perfect-scrollbar-on')
      } else {
        docClasses.add('perfect-scrollbar-off')
      }
    }
  },
  mounted() {
    this.initScrollbar()
  }
}
</script>
<style lang="scss">
$scaleSize: 0.95;
@keyframes zoomIn95 {
  from {
    opacity: 0;
    transform: scale3d($scaleSize, $scaleSize, $scaleSize);
  }
  to {
    opacity: 1;
  }
}

.main-panel .zoomIn {
  animation-name: zoomIn95;
}

@keyframes zoomOut95 {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
    transform: scale3d($scaleSize, $scaleSize, $scaleSize);
  }
}

.main-panel .zoomOut {
  animation-name: zoomOut95;
}
</style>
