"set expandtab
set number
syntax on
"set autoindent shiftwidth=4
"set smartindent
"set tabstop=4
"set smartcase
colorscheme elflord
set incsearch
set hlsearch
au BufWritePost * if getline(1) =~ "^#!" | if getline(1) =~ "/bin/" | silent !chmod +x <afile> | endif | endif
au BufWritePost * if getline(1) =~ "^#!" | if getline(1) =~ "/bin/" | silent execute "!chmod a+x <afile>" | endif | endif
" Tell vim to remember certain things when we exit
"  '10  :  marks will be remembered for up to 10 previously edited files
"  "100 :  will save up to 100 lines for each register
"  :20  :  up to 20 lines of command-line history will be remembered
"  %    :  saves and restores the buffer list
"  n... :  where to save the viminfo files
set viminfo='10,\"100,:20,%,n~/.viminfo
function! ResCur()
	if line("'\"") <= line("$")
	normal! g`"
	return 1
	endif
	endfunction

	augroup resCur
	autocmd!
autocmd BufWinEnter * call ResCur()
	augroup END
filetype plugin on
  let g:pydiction_location = '/usr/share/pydiction/complete-dict'
