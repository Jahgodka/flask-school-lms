from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, UTC
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class UserInfo(db.Model):
    __tablename__ = 'user_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.id}>'

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f'<Subject {self.subject_name}>'

class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.Integer, nullable=False)
    added_date = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    user = db.relationship('UserInfo', backref='grades')

    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    subject = db.relationship('Subject', backref='grades')

    attempt_id = db.Column(db.Integer, db.ForeignKey('student_attempts.id'), nullable=False)
    attempt = db.relationship('StudentAttempt', backref='grade')

    __table_args__ = (
        CheckConstraint('value >= 2 AND value <= 5', name='Limit_Ocen'),
    )

    def __repr__(self):
        return f'<Grade {self.id}>'

class Test(db.Model):
    __tablename__ = 'tests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    teacher = db.relationship('UserInfo', backref='tests')

    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
    subject = db.relationship('Subject', backref='tests')

    groups = db.relationship('Group', secondary='test_groups', backref='tests')

    @property
    def total_points(self):
        return sum(tq.points for tq in self.test_questions)

    def __repr__(self):
        return f'<Test {self.title}>'

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    added_date = db.Column(db.DateTime, default=lambda: datetime.now(UTC), nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    teacher = db.relationship('UserInfo', backref='owned_groups')

    students = db.relationship('UserInfo', secondary='group_students', backref='groups')

    def __repr__(self):
        return f'<Group {self.name}>'

class GroupStudent(db.Model):
    __tablename__ = 'group_students'
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), primary_key=True)

    def __repr__(self):
        return f'<GroupStudent group_id={self.group_id} user_id={self.user_id}>'
    
test_groups = db.Table('test_groups',
    db.Column('test_id', db.Integer, db.ForeignKey('tests.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Question {self.id}>'

class AnswerOption(db.Model):
    __tablename__ = 'answer_options'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', backref='answer_options')

    def __repr__(self):
        return f'<AnswerOption {self.id}>'

class TestQuestion(db.Model):
    __tablename__ = 'test_questions'
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable=False)

    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)
    test = db.relationship('Test', backref='test_questions')

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', backref='test_questions')

    def __repr__(self):
        return f'<TestQuestion {self.id}>'

class StudentAttempt(db.Model):
    __tablename__ = 'student_attempts'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float, nullable=True)

    student_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    student = db.relationship('UserInfo', backref='attempts')

    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'), nullable=False)
    test = db.relationship('Test', backref='attempts')

    def __repr__(self):
        return f'<StudentAttempt {self.id}>'

class AttemptAnswer(db.Model):
    __tablename__ = 'attempt_answers'
    id = db.Column(db.Integer, primary_key=True)

    attempt_id = db.Column(db.Integer, db.ForeignKey('student_attempts.id'), nullable=False)
    attempt = db.relationship('StudentAttempt', backref='answers')

    answer_option_id = db.Column(db.Integer, db.ForeignKey('answer_options.id'), nullable=False)
    answer_option = db.relationship('AnswerOption')

    def __repr__(self):
        return f'<AttemptAnswer {self.id}>'