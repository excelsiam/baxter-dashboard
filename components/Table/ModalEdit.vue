<template>
  <modal :show.sync="active" footerClasses="justify-content-center" type="notice">
    <form class="form-horizontal basicinfo-form">
      <card>
        <h4 slot="header" class="card-title">Edit Record#{{ form.id }}: {{ form.name }}</h4>
        <div>
          <div class="row">
            <label class="col-sm-4 col-form-label">Name</label>
            <div class="col-sm-8">
              <base-input name="name" v-validate="modelValidations.name" v-model="form.name" :error="getError('name')"> </base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">ID</label>
            <div class="col-sm-8">
              <base-input name="code_id" v-validate="modelValidations.id" v-model="form.code_id" :error="getError('code_id')"> </base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Hospital</label>
            <div class="col-sm-8">
              <base-input name="hospital" v-model="form.hospital"> </base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Gender</label>
            <div class="col-sm-8">
              <base-input name="gender" v-model="form.gender"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Birth Date</label>
            <div class="col-sm-8">
              <base-input name="birth_date" v-model="form.birth_date"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Education</label>
            <div class="col-sm-8">
              <base-input name="education" v-model="form.education"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Payment</label>
            <div class="col-sm-8">
              <base-input name="payment" v-model="form.payment"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Primary Kidney Disease</label>
            <div class="col-sm-8">
              <base-input name="primary_kidney_disease" v-model="form.primary_kidney_disease"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">DM Status</label>
            <div class="col-sm-8">
              <div class="form-check">
                <label class="form-check-label" style="vertical-align: top;">
                  <input type="checkbox" class="form-check-input" v-model="form.dm_status" />
                  <span class="form-check-sign"></span>
                </label>
              </div>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">PD Initiation Date</label>
            <div class="col-sm-8">
              <base-input name="pd_initiation_date" v-model="form.pd_initiation_date"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Dropout Date</label>
            <div class="col-sm-8">
              <base-input name="dropout_date" v-model="form.dropout_date"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Dropout Category</label>
            <div class="col-sm-8">
              <base-input name="dropout_category" v-model="form.dropout_category"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Dropout Cause</label>
            <div class="col-sm-8">
              <base-input name="dropout_cause" v-model="form.dropout_cause"></base-input>
            </div>
          </div>

          <div class="row">
            <label class="col-sm-4 col-form-label">Remarks</label>
            <div class="col-sm-8">
              <base-input name="remarks" v-model="form.remarks"></base-input>
            </div>
          </div>
        </div>
      </card>
    </form>
    <div slot="footer" class="justify-content-center">
      <base-button type="info" round @click.native="submit()">Sounds good! </base-button>
    </div>
  </modal>
</template>
<script>
import { Modal } from '@/components'
export default {
  components: {
    Modal
  },
  data() {
    return {
      active: false,
      form: {},
      modelValidations: {
        name: {
          required: true
        },
        id: {
          required: true
        }
      }
    }
  },
  methods: {
    getError(fieldName) {
      return this.errors.first(fieldName)
    },
    async submit() {
      let isValid = await this.$validator.validateAll()
      if (!isValid) return

      let response = await this.$axios.$post(`http://localhost:8000/basics_update/${this.form.id}`, this.form)
      if (!response.success) {
        alert('error')
        return
      }
      this.active = false
      this.$notify({
        message: 'Updated',
        timeout: 3000,
        icon: 'tim-icons icon-check-2',
        horizontalAlign: 'right',
        verticalAlign: 'top',
        type: 'success'
      })
      this.$emit('updateRow', this.form)
    }
  }
}
</script>

<style lang="scss">
.modal.show .modal-dialog {
  transform: unset;
}
.basicinfo-form .form-group {
  margin-bottom: 0;
}
.basicinfo-form .row {
  margin-bottom: 10px;
}
</style>
