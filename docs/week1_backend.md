# Week 1 – Backend Mastery (Odoo ORM, Models, Security, Tests)

## 📅 Daily Log

### Day 1 – Environment Setup & First Module
- ✅ Set up Odoo 17 + PostgreSQL using Docker.
- ✅ Created GitHub repo with clean `.gitignore`.
- ✅ Built first custom module: `farmer_management`.
- ✅ Added model: `farmer.management` with fields (name, phone, age, village).
- ✅ Installed module successfully in Odoo.

**Learning Notes:**
- Odoo’s `addons/` folder is where c


### Day 2 – Relations & Computed Fields

✅ Added farmer.land model with fields (name, size, location) linked to Farmer (Many2one).

✅ Added farmer.crop model with fields (name, season, yield) linked to Land (Many2one).

✅ Extended Farmer model with One2many relation to Lands.

✅ Implemented computed field total_land_area that auto-sums the size of all farmer’s lands.

✅ Created menu, action, and form/tree view for Farmers.

✅ Verified that adding lands updates total_land_area correctly in Odoo UI.

✅ Pushed code changes to GitHub (week1_backend branch).

**Learning Notes:**

One2many is always the “reverse” of Many2one. (Farmer → Land, Land → Farmer).

@api.depends ensures computed fields update automatically when dependencies change.

Setting store=True on a computed field saves it in the database (better for performance).

Menus, actions, and views make the model accessible in the Odoo UI.

Good practice: put all views inside a views/ folder and declare them in __manifest__.py.


###  Day 3 – Security Rules & Access Control
🔑 Key Concepts

Access Rights are defined in ir.model.access.csv.

They control model-level permissions: Read, Write, Create, Delete.

Record Rules (ir.rule) provide record-level control (which records a user can access).

Odoo combines Access Rights + Record Rules to enforce security.

💡 Lessons Learned

Access rights apply per model, not per record.

Record rules can be added later for finer-grained access.

Always test permissions by logging in with users from different groups.

###  Day 4 – Menus & Actions
🔑 Key Concepts

Actions in Odoo determine what happens when you open a menu (tree view, form view, report, wizard, etc.).

Menu Items are linked to actions and provide navigation in the UI.

Types of actions:

Window Action (ir.actions.act_window) → opens tree/form views.

Server Action (ir.actions.server) → executes Python code.

Report Action (ir.actions.report) → prints reports.


💡 Lessons Learned

Menus only display navigation; real access is still controlled by security.

Use parent attribute to create hierarchy (root → submenus).

Actions can be reused in multiple menus.