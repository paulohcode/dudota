/* ===== Dudota Doces – Carrinho de Compras ===== */

const PRODUCTS = [
  { id: 'canudo-bandeja',    name: 'Canudo Frito Recheado',              price: 45, image: 'assets/canudo_bandeja.jpeg',        category: 'destaque' },
  { id: 'pacoca-caseira',    name: 'Paçoca Caseira',                     price: 30, image: 'assets/pacoca_caseira.jpeg',        category: 'tradicionais' },
  { id: 'pe-moleque',        name: 'Pé de Moleque',                      price: 30, image: 'assets/pe_moleque.jpeg',            category: 'tradicionais' },
  { id: 'canudo-8',          name: 'Canudo Frito',                       price: 8,  image: 'assets/canudo_8.jpeg',              category: 'destaque' },
  { id: 'geleia-frutas',     name: 'Geleia de Frutas',                   price: 27, image: 'assets/geleia_frutas.jpeg',         category: 'sortidos' },
  { id: 'bananitas',         name: 'Bananitas',                          price: 27, image: 'assets/bananitas.jpeg',             category: 'sortidos' },
  { id: 'doce-leite',        name: 'Doce de Leite',                     price: 27, image: 'assets/doce_leite.jpeg',            category: 'barras' },
  { id: 'fondant-leite-po',  name: 'Fondant de Leite em Pó',             price: 28, image: 'assets/fondant_leite_po.jpeg',      category: 'barras' },
  { id: 'fondant-chocolate', name: 'Fondant Leite em Pó com Chocolate',  price: 28, image: 'assets/fondant_chocolate.jpeg',    category: 'barras' },
  { id: 'pacoca-rolha-choc', name: 'Paçoca Rolha com Chocolate',         price: 26, image: 'assets/pacoca_rolha_choc.jpeg',     category: 'amendoim' },
  { id: 'pacoca-rolha-trad', name: 'Paçoca Rolha Tradicional',           price: 24, image: 'assets/pacoca_rolha_trad.jpeg',     category: 'amendoim' },
  { id: 'pe-moleque-croc',   name: 'Pé de Moleque Crocante',            price: 27, image: 'assets/pe_moleque_crocante.jpeg',   category: 'amendoim' },
  { id: 'choco-mole-branco', name: 'Choco Mole Branco',                  price: 35, image: 'assets/choco_mole_branco.jpeg',     category: 'especiais' },
  { id: 'choco-mole',        name: 'Choco Mole',                          price: 35, image: 'assets/choco_mole.jpeg',            category: 'especiais' },
  { id: 'maria-bonita',      name: 'Maria Bonita',                       price: 35, image: 'assets/maria_bonita.jpeg',          category: 'especiais' },
];

/* ---------- Storage helpers ---------- */
function getCart() {
  try {
    return JSON.parse(localStorage.getItem('dudota_cart')) || [];
  } catch { return []; }
}

function saveCart(cart) {
  localStorage.setItem('dudota_cart', JSON.stringify(cart));
  updateCartBadge();
}

/* ---------- Cart actions ---------- */
function addToCart(productId) {
  const cart = getCart();
  const existing = cart.find(item => item.id === productId);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ id: productId, qty: 1 });
  }
  saveCart(cart);
  window.location.href = 'carrinho.html';
}

function removeFromCart(productId) {
  let cart = getCart().filter(item => item.id !== productId);
  saveCart(cart);
  if (typeof renderCartPage === 'function') renderCartPage();
}

function updateQty(productId, delta) {
  const cart = getCart();
  const item = cart.find(i => i.id === productId);
  if (!item) return;
  item.qty += delta;
  if (item.qty <= 0) {
    cart.splice(cart.indexOf(item), 1);
  }
  saveCart(cart);
  if (typeof renderCartPage === 'function') renderCartPage();
}

function clearCart() {
  localStorage.removeItem('dudota_cart');
  updateCartBadge();
  if (typeof renderCartPage === 'function') renderCartPage();
}

/* ---------- Badge ---------- */
function updateCartBadge() {
  const badge = document.getElementById('cart-count');
  if (!badge) return;
  const cart = getCart();
  const total = cart.reduce((s, i) => s + i.qty, 0);
  badge.textContent = total;
  badge.style.display = total > 0 ? 'grid' : 'none';
}

/* ---------- Add-to-cart animation ---------- */
function animateAddToCart(productId) {
  const btn = document.querySelector(`[data-product-id="${productId}"] .add-cart-btn, [data-product-id="${productId}"]`);
  if (btn) {
    btn.classList.add('added');
    setTimeout(() => btn.classList.remove('added'), 800);
  }
}

/* ---------- WhatsApp message ---------- */
function generateWhatsAppMessage() {
  const cart = getCart();
  if (cart.length === 0) return '';
  let msg = 'Olá, gostaria de fazer o seguinte pedido:\n\n';
  let total = 0;
  cart.forEach(item => {
    const product = PRODUCTS.find(p => p.id === item.id);
    if (product) {
      const subtotal = product.price * item.qty;
      msg += `• ${product.name} x${item.qty} — R$ ${subtotal.toFixed(2).replace('.', ',')}\n`;
      total += subtotal;
    }
  });
  msg += `\nTotal: R$ ${total.toFixed(2).replace('.', ',')}`;
  return encodeURIComponent(msg);
}

/* ---------- Init ---------- */
document.addEventListener('DOMContentLoaded', updateCartBadge);