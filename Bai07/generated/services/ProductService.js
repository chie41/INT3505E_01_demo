/* eslint-disable no-unused-vars */
const Service = require('./Service');
let products = [
  { id: '1', name: 'iPhone 17', price: 999, description: 'Flagship Apple phone' },
  { id: '2', name: 'Galaxy S25', price: 899, description: 'Samsung flagship phone' },
];

/**
* Create a new product
*
* product Product 
* no response value expected for this operation
* */
const createProduct = ({ product }) => new Promise(
  async (resolve, reject) => {
    try {
      const newProduct = {
        id: (products.length + 1).toString(),
        name: product.name,
        price: product.price,
        description: product.description,
      };
      products.push(newProduct);
      resolve(Service.successResponse({
        product,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Delete product
*
* id String 
* no response value expected for this operation
* */
const deleteProduct = ({ id }) => new Promise(
  async (resolve, reject) => {
    const index = products.findIndex(p => p.id === id);
    if (index === -1) {
      reject(Service.rejectResponse('Product not found', 404));
      return;
    }
    products.splice(index, 1);
    try {
      resolve(Service.successResponse({
        id,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get product by ID
*
* id String 
* no response value expected for this operation
* */
const getProductById = ({ id }) => new Promise(
  async (resolve, reject) => {
    try {
      const product = products.find(p => p.id === id);
      if (!product) {
        reject(Service.rejectResponse('Product not found', 404));
        return;
      }
      resolve(Service.successResponse({
        id,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Get all products
*
* no response value expected for this operation
* */
const getProducts = () => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Update product
*
* id String 
* product Product 
* no response value expected for this operation
* */
const updateProduct = ({ id, product }) => new Promise(
  async (resolve, reject) => {
    try {
      const index = products.findIndex(p => p.id === id);
      if (index === -1) {
        reject(Service.rejectResponse('Product not found', 404));
        return;
      }

      products[index] = { ...products[index], ...product };
      resolve(Service.successResponse({
        id,
        product,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

module.exports = {
  createProduct,
  deleteProduct,
  getProductById,
  getProducts,
  updateProduct,
};
