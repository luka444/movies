from odoo import fields, models



class MoviesMovies(models.Model):
    _name = "movies.movies"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Movies"

    name = fields.Char(string="Title")
    release_date = fields.Date()
    duration = fields.Float()
    description = fields.Text()
    language = fields.Selection([("geo", "Geo"),("eng", "Eng")])
    image = fields.Image(string='Poster', max_width=590, max_height=590)
    rating = fields.Char()
    actor_ids = fields.Many2many("res.partner")
    director_id = fields.Many2one("res.partner")
    movie_budget = fields.Float(string="Budget")
    movie_income = fields.Float(string="Income")