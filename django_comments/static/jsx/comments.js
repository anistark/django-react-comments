var CommentBox = React.createClass({
		getInitialState: function() {
			// $.ajax({
			// 	url : "getcomments/",
			// 	type : "POST",
			// 	success : function(data) {
			// 		console.log('success - '+ JSON.stringify(data));
			// 		return data;
			// 	},
			// 	error : function(xhr,errmsg,err) {
			// 		console.log('err');
			// 		console.log(xhr.status + ": " + xhr.responseText);
			// 		return {data: []};
			// 	}
			// });
			return {data: []};
		},
		loadCommentsFromServer: function() {
			$.ajax({
				url : this.props.url,
				dataType : 'json',
				success : function(data) {
					console.log('in - '+ data);
					this.setState({data: data});
				}.bind(this),
				error : function(xhr, status, err) {
					console.log('out');
					console.error(this.props.url, status, err);
				}.bind(this)
			});
		},
		handleCommentSubmit: function(comment) {
			var comments = this.state.data;
			var newComments = comments.concat([comment]);
			this.setState({data: newComments});
			$.ajax({
				type: 'POST',
				url: '/',
				dataType: 'json',
				data: comment,
				success: function(data) {
					this.setState({data: data});
				}.bind(this),
				error: function(xhr, status, err) {
					console.error(' ', status, err );
				}.bind(this)
			});
		},
		componentDidMount: function() {
			this.loadCommentsFromServer();
			setInterval(this.loadCommentsFromServer, this.props.pollInterval);
		},
		render: function() {
			return (
				<div className="commentBox">
					<h1>Comments</h1>
					<CommentList data={this.state.data} />
					<CommentForm onCommentSubmit={this.handleCommentSubmit} />
				</div>
			);
		}
	});
	var CommentList = React.createClass({
		render: function() {
			var commentNodes = this.props.data.map(function (comment) {
				return (
					<Comment author={comment.author}>
						{comment.text}
					</Comment>
				);
			});
			return (
				<div className="commentList">
					{commentNodes}
				</div>
			);
		}
	});
	var CommentForm = React.createClass({
		handleSubmit: function() {
			var author = this.refs.author.getDOMNode().value.trim();
			var text = this.refs.text.getDOMNode().value.trim();
			this.props.onCommentSubmit({author: author, text: text});
			if (!text || !author) {
				return false;
			}
			this.refs.author.getDOMNode().value = '';
			this.refs.text.getDOMNode().value = '';
			return false;
		},
		render: function() {
			return (
				<form className="commentForm" onSubmit={this.handleSubmit}>
					<input hidden type="text" placeholder="Your name" ref="author" value="Author" />
					<br />
					<input type="text" id="textName" placeholder="Say something..." ref="text" />
					<input type="submit" id="submitButton" value="Post" />
				</form>
			);
		}
	});
	var converter = new Showdown.converter();
	var Comment = React.createClass({
		render: function() {
			return (
				<div className="comment">
					<div className="row">
						<div className="commentAuthor col s2">
								{this.props.author}
						</div>
						<div className="commentText col s10">{this.props.children}</div>
					</div>
				</div>
			);
		}
	});
	React.render(
		<CommentBox url="getcomments/" pollInterval={2000} />,
		document.getElementById('content')
	);