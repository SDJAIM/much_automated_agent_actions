from odoo import fields, models


class AiProvider(models.Model):
    _name = "ai.provider"
    _description = "AI Provider"
    _order = "id, sequence"

    sequence = fields.Integer(default=1)
    name = fields.Char(required=True)
    code = fields.Char(
        required=True,
        help="Technical code (e.g., openai, anthropic)",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        default=lambda self: self.env.company,
        ondelete="cascade",
    )
    api_key = fields.Char(
        string="API Key",
    )
    active = fields.Boolean(default=True)


class AiModel(models.Model):
    _name = "ai.model"
    _description = "AI Model"
    _order = "id, sequence"

    sequence = fields.Integer(default=1)
    name = fields.Char(
        required=True,
        help="Human-readable model name",
    )
    provider_id = fields.Many2one(
        comodel_name="ai.provider",
        required=True,
        ondelete="cascade",
    )
    technical_name = fields.Char(
        required=True,
        help="Model identifier in the provider's API",
    )
    files_allowed = fields.Boolean(
        default=False,
        help="Whether the model supports file attachments",
    )
    images_allowed = fields.Boolean(
        default=False,
        help="Whether the model supports image attachments",
    )
    max_files = fields.Integer(
        help="Maximum number of files supported",
    )
    active = fields.Boolean(default=True)
