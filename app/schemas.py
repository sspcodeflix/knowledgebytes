from marshmallow import Schema, fields

class QuestionBaseSchema(Schema):
    text = fields.Str()
    options = fields.Str()
    answer = fields.Str()

class QuestionCreateSchema(QuestionBaseSchema):
    pass

class QuestionSchema(QuestionBaseSchema):
    id = fields.Int()
    quiz_id = fields.Int()
    answer = fields.Str()

class QuizBaseSchema(Schema):
    title = fields.Str()
    active = fields.Bool()

class QuizCreateSchema(QuizBaseSchema):
    pass

class QuizSchema(QuizBaseSchema):
    id = fields.Int()
    questions = fields.Nested(QuestionSchema, many=True)

class ResultBaseSchema(Schema):
    user_id = fields.Int()
    quiz_id = fields.Int()
    score = fields.Int()
    rank = fields.Int()

class ResultCreateSchema(ResultBaseSchema):
    pass

class ResultSchema(ResultBaseSchema):
    id = fields.Int()
