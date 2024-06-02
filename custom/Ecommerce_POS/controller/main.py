# controllers/main.py
from odoo import http
from odoo.http import request

class CustomUserController(http.Controller):

    @http.route('/create_user', type='http', auth='public', website=True)
    def create_user_form(self, **post):
        return request.render('Ecommerce_POS.create_user_form')

    @http.route('/create_user', type='http', auth='public', website=True, methods=['POST'])
    def create_user(self, **post):
        name = post.get('name')
        username = post.get('username')

        if not name:
            return request.render('Ecommerce_POS.error_template', {
                'error': 'Name is required.'
            })

        if not username:
            return request.render('Ecommerce_POS.error_template', {
                'error': 'Username is required.'
            })

        existing_user = request.env['custom.user'].sudo().search([('username', '=', username)])
        if existing_user:
            return request.render('Ecommerce_POS.error_template', {
                'error': 'Username already exists.'
            })

        new_user = request.env['custom.user'].sudo().create({
            'name': name,
            'username': username,
        })

        return request.redirect('/web#id=%s&view_type=form&model=custom.user' % new_user.id)
