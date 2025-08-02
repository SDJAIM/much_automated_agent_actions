{
    "name": "Odoo AI Automated Actions",
    "summary": "Odoo AI Automated Actions with "
    "generative AI (ChatGPT, Claude, Gemini)",
    "version": "18.0.1.0.0",
    "category": "Productivity",
    "author": "much. GmbH",
    "website": "https://muchconsulting.de",
    "license": "OPL-1",
    "depends": [
        "base",
        "base_automation",
        "web_notify",
    ],
    "external_dependencies": {
        "python": [
            "openai",
            "anthropic",
            "google-genai",
            "markdown-it-py",
        ]
    },
    "data": [
        "security/ir_module_category.xml",
        "security/res_groups.xml",
        "security/ir_rule.xml",
        "security/ir.model.access.csv",
        "data/ai_provider_data.xml",
        "views/menus.xml",
        "views/ai_provider.xml",
        "views/ai_model.xml",
        "views/ir_actions_server.xml",
        "wizards/preview_prompt.xml",
    ],
    "images": [
        "static/description/banner.gif",
    ],
    "application": True,
}
