<template>
  <div class="content">
    <div class="col-md-8 ml-auto mr-auto">
      <h2 class="text-center">Basic Information</h2>
    </div>
    <BasicWizard />
    <div class="row mt-5">
      <div class="col-12">
        <card card-body-classes="table-full-width">
          <h4 slot="header" class="card-title">Basic Information</h4>
          <div>
            <div class="col-12 d-flex justify-content-center justify-content-sm-between flex-wrap">
              <el-select class="select-primary mb-3 pagination-select" v-model="pagination.perPage" placeholder="Per page">
                <el-option class="select-primary" v-for="item in pagination.perPageOptions" :key="item" :label="item" :value="item"> </el-option>
              </el-select>
              <base-input>
                <el-input
                  type="search"
                  class="mb-3 search-input"
                  clearable
                  prefix-icon="el-icon-search"
                  placeholder="Search records"
                  v-model="searchQuery"
                  aria-controls="datatables"
                >
                </el-input>
              </base-input>
            </div>
            <el-table :data="queriedData">
              <el-table-column v-for="column in tableColumns" :key="column.label" :min-width="column.minWidth" :prop="column.prop" :label="column.label">
              </el-table-column>
              <el-table-column :min-width="180" align="right" label="Actions">
                <div slot-scope="props">
                  <base-button @click.native="handleView(props.$index, props.row)" class="btn-link" type="info" size="sm" icon>
                    <i class="tim-icons icon-zoom-split"></i>
                  </base-button>
                  <base-button @click.native="handleEdit(props.$index, props.row)" class="edit btn-link" type="warning" size="sm" icon>
                    <i class="tim-icons icon-pencil"></i>
                  </base-button>
                  <base-button @click.native="handleDelete(props.$index, props.row)" class="remove btn-link" type="danger" size="sm" icon>
                    <i class="tim-icons icon-simple-remove"></i>
                  </base-button>
                </div>
              </el-table-column>
            </el-table>
          </div>
          <div slot="footer" class="col-12 d-flex justify-content-center justify-content-sm-between flex-wrap">
            <div class="">
              <p class="card-category">Showing {{ from + 1 }} to {{ to }} of {{ total }} entries</p>
            </div>
            <base-pagination class="pagination-no-border" v-model="pagination.currentPage" :per-page="pagination.perPage" :total="total"> </base-pagination>
          </div>
        </card>
      </div>
    </div>
    <ModalView ref="modal-view" />
    <ModalEdit ref="modal-edit" @updateRow="updateRow" />
  </div>
</template>
<script>
import { Table, TableColumn, Select, Option } from 'element-ui'
import ModalEdit from '@/components/Table/ModalEdit'
import ModalView from '@/components/Table/ModalView'
import BasicWizard from '@/components/Table/BasicWizard'
import { BasePagination } from '@/components'
import Fuse from 'fuse.js'
import swal from 'sweetalert2'

export default {
  name: 'paginated',
  components: {
    BasePagination,
    [Select.name]: Select,
    [Option.name]: Option,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn,
    ModalView,
    ModalEdit,
    BasicWizard
  },
  data() {
    return {
      pagination: {
        perPage: 5,
        currentPage: 1,
        perPageOptions: [5, 10, 25, 50],
        total: 0
      },
      searchQuery: '',
      tableColumns: [
        {
          prop: 'name',
          label: 'name',
          minWidth: 250
        },
        {
          prop: 'code_id',
          label: 'id',
          minWidth: 250
        },
        {
          prop: 'hospital',
          label: 'hospital',
          minWidth: 250
        }
      ],
      tableData: [],
      searchedData: [],
      fuseSearch: null
    }
  },
  computed: {
    queriedData() {
      let result = this.tableData
      if (this.searchedData.length > 0) {
        result = this.searchedData
      }
      return result.slice(this.from, this.to)
    },
    to() {
      let highBound = this.from + this.pagination.perPage
      if (this.total < highBound) {
        highBound = this.total
      }
      return highBound
    },
    from() {
      return this.pagination.perPage * (this.pagination.currentPage - 1)
    },
    total() {
      return this.searchedData.length > 0 ? this.searchedData.length : this.tableData.length
    }
  },
  methods: {
    handleView(index, row) {
      this.$refs['modal-view'].active = true
      this.$refs['modal-view'].data = row
    },
    handleEdit(index, row) {
      this.$refs['modal-edit'].active = true
      this.$refs['modal-edit'].data = row
      this.$refs['modal-edit'].form = Object.assign({}, row)
    },
    handleDelete(index, row) {
      swal
        .fire({
          title: 'Are you sure?',
          icon: 'warning',
          text: `You won't be able to revert this!`,
          showCancelButton: true,
          confirmButtonText: 'Yes, delete it!'
        })
        .then(result => {
          if (result.value) {
            this.deleteRow(row)
            this.$notify({
              message: 'Deleted',
              timeout: 3000,
              icon: 'tim-icons icon-check-2',
              horizontalAlign: 'right',
              verticalAlign: 'top',
              type: 'success'
            })
          }
        })
    },
    updateRow(row) {
      var index = this.tableData.findIndex(x => x.id === row.id)
      this.tableData[index] = row
      this.$set(this.tableData, index, row)
    },
    deleteRow(row) {
      this.tableData = this.tableData.filter(x => x.id !== row.id)
      this.$axios.$post(`http://localhost:8000/basics_delete/${row.id}`)
    }
  },
  created() {
    this.$axios.$get('http://localhost:8000/basics').then(response => {
      this.tableData = response
    })
  },
  mounted() {
    // Fuse search initialization.
    this.fuseSearch = new Fuse(this.tableData, {
      keys: ['name', 'id'],
      threshold: 0.3
    })
  },
  watch: {
    searchQuery(value) {
      let result = this.tableData
      if (value !== '') {
        result = this.fuseSearch.search(this.searchQuery)
        console.log(result)
      }
      this.searchedData = result
    }
  }
}
</script>
<style>
.pagination-select,
.search-input {
  width: 200px;
}
</style>
