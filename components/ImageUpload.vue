<template>
  <div class="fileinput text-center">
    <div class="fileinput-new thumbnail" :class="{ 'img-circle': type === 'avatar' }">
      <img :src="image" alt="preview" />
    </div>
    <div>
      <span class="btn btn-primary btn-simple btn-file">
        <span class="fileinput-new">{{ fileExists ? changeText : selectText }}</span>
        <input type="hidden" value="" name="" />
        <input accept="image/*" @change="handlePreview" type="file" name="..." class="valid" :multiple="false" aria-invalid="false" />
      </span>
      <base-button v-if="fileExists" @click="removeFile" round type="danger"> <i class="fas fa-times"></i> {{ removeText }} </base-button>
    </div>
  </div>
</template>
<script>
export default {
  name: 'image-upload',
  props: {
    type: {
      type: String,
      default: '',
      description: 'Image upload type (""|avatar)'
    },
    src: {
      type: String,
      default: '',
      description: 'Initial image to display'
    },
    selectText: {
      type: String,
      default: 'Select image'
    },
    changeText: {
      type: String,
      default: 'Change'
    },
    removeText: {
      type: String,
      default: 'Remove'
    }
  },
  data() {
    let avatarPlaceholder =
      'https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1397750781/2c423ac427445275b4346a31289d13e8.png'
    let imgPlaceholder =
      'https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco/v1397750781/2c423ac427445275b4346a31289d13e8.png'
    return {
      placeholder: this.type === 'avatar' ? avatarPlaceholder : imgPlaceholder,
      imagePreview: null
    }
  },
  computed: {
    fileExists() {
      return this.imagePreview !== null
    },
    image() {
      return this.imagePreview || this.src || this.placeholder
    }
  },
  methods: {
    handlePreview(event) {
      let file = event.target.files[0]
      this.imagePreview = URL.createObjectURL(file)
      this.$emit('change', file)
    },
    removeFile() {
      this.imagePreview = null
      this.$emit('change', null)
    }
  }
}
</script>
<style></style>
